from __future__ import annotations

from dataclasses import dataclass
import re
import time
from typing import Optional, Union

from allspice.utils.core import get_all_pcb_components

from ..allspice import AllSpice
from ..apiobject import Content, Ref, Repository
from ..exceptions import NotYetGeneratedException

PRJPCB_SCHDOC_REGEX = re.compile(r"DocumentPath=(.*?SchDoc)(\r\n|\n\r|\n)")


@dataclass
class SchematicComponent:
    description: str
    manufacturer: str
    part_number: str
    designator: str


@dataclass
class PcbComponent:
    designator: str
    schematic_link: str


@dataclass
class BomEntry:
    description: str
    manufacturer: str
    part_number: str
    designators: list[str]
    quantity: int


Bom = list[BomEntry]


@dataclass
class AttributesMapping:
    """
    Define how we map from attributes in the Altium SchDoc file to the fields of
    the BOM.

    For each field, we define a list of attribute names that we will check in
    the Altium SchDoc file. The *first* one found defined will be used.

    :param description: A list of attribute names in the Altium SchDoc file
        that contain the description of the part.
    :param manufacturer: A list of attribute names in the Altium SchDoc file
        that contain the manufacturer of the part.
    :param part_number: A list of attribute names in the Altium SchDoc file
        that contain the part number of the part.
    :param designator: A list of attribute names in the Altium SchDoc file
        that contain the designator of the part.
    """

    description: list[str]
    manufacturer: list[str]
    part_number: list[str]
    designator: list[str]

    @staticmethod
    def from_dict(dictionary: dict[str, list[str]]) -> AttributesMapping:
        """
        Create an AttributesMapping from a dictionary.

        Example Input::

            {
                "description": ["Description"],
                "manufacturer": ["Manufacturer", "MANUFACTURER"],
                "part_number": ["Part Number"],
                "designator": ["Designator"],
            }
        """
        return AttributesMapping(
            description=dictionary["description"],
            manufacturer=dictionary["manufacturer"],
            part_number=dictionary["part_number"],
            designator=dictionary["designator"],
        )


# TODO: We should make this generic for all PCBs and change all `pcbdoc` references to `pcb`
# TODO: We should default to generating a BOM using only the project file + schematics.
#   Using PCB to generate the BOM should be an option flag, but we shouldn't be combining
#   PCB and schematic BOMs.


def generate_bom_for_altium(
    allspice_client: AllSpice,
    repository: Repository,
    prjpcb_file: Union[Content, str],
    pcbdoc_file: Union[Content, str],
    attributes_mapping: AttributesMapping,
    ref: Ref = "main",
) -> Bom:
    """
    Generate a BOM for an Altium project.

    :param allspice_client: The AllSpice client to use.
    :param repository: The repository to generate the BOM for.
    :param prjpcb_file: The Altium project file. This can be a Content object
        returned by the AllSpice API, or a string containing the path to the
        file in the repo.
    :param pcbdoc_file: The Altium PCB document file. This can be a Content
        object returned by the AllSpice API, or a string containing the path to
        the file in the repo.
    :param attributes_mapping: A mapping of Altium attributes to BOM entry
        attributes. See the documentation for AttributesMapping for more
        information.
    :param ref: The ref, i.e. branch, commit or git ref from which to take the
        project files. Defaults to "main".
    :return: A list of BOM entries.
    """

    allspice_client.logger.info(
        f"Generating BOM for {repository.name=} on {ref=} using {attributes_mapping=}"
    )
    allspice_client.logger.info(f"Fetching {prjpcb_file=} and {pcbdoc_file=}")

    prjpcb_file = repository.get_raw_file(prjpcb_file, ref=ref).decode("utf-8")
    schdoc_files_in_proj = {x for x in _extract_schdoc_list_from_prjpcb(prjpcb_file)}

    allspice_client.logger.info("Found %d SchDoc files", len(schdoc_files_in_proj))

    schdoc_components = _extract_all_schdoc_components(
        repository,
        ref,
        schdoc_files_in_proj,
        attributes_mapping,
    )
    pcbdoc_components = _extract_all_pcbdoc_components(repository, ref, pcbdoc_file)

    ungrouped_bom_entries = _combine_components_to_ungrouped_bom(
        schdoc_components,
        pcbdoc_components,
    )

    return _group_bom_entries(ungrouped_bom_entries)


def _find_first_matching_key(
    alternatives: Union[list[str], str],
    attributes: dict,
) -> Optional[str]:
    """
    Search for a series of alternative keys in a dictionary, and return the
    value of the first one found.
    """

    if isinstance(alternatives, str):
        alternatives = [alternatives]

    for alternative in alternatives:
        if alternative in attributes:
            return attributes[alternative]["text"]

    return None


def _extract_schdoc_list_from_prjpcb(prjpcb_file_content) -> list[str]:
    """
    Get a list of SchDoc files from a PrjPcb file.
    """

    # Sometimes the SchDoc file can use \n\r instead of CRLF line endings.
    # Unfortunately, it looks like $ even with re.M doesn't(?) match \n\r.
    return [match.group(1) for match in PRJPCB_SCHDOC_REGEX.finditer(prjpcb_file_content)]


def _schdoc_component_from_attributes(
    attributes: dict,
    mapper: AttributesMapping,
) -> SchematicComponent:
    """
    Make a SchDoc Component object out of the JSON for it in the SchDoc file.

    :param attributes: The attributes for the component in the SchDoc
    :param mapper: An AttributesMapping object, see the documentation for
        AttributesMapping for more information.
    :returns: A SchodocComponent object representing that component.
    """

    return SchematicComponent(
        description=_find_first_matching_key(mapper.description, attributes),
        designator=_find_first_matching_key(mapper.designator, attributes) or "",
        manufacturer=_find_first_matching_key(mapper.manufacturer, attributes),
        part_number=_find_first_matching_key(mapper.part_number, attributes),
    )


def _extract_components_from_schdoc(
    schdoc_file_content: dict,
    attributes_mapper: AttributesMapping,
) -> list[SchematicComponent]:
    """
    Extract all the components from a schdoc file. To see what attributes are
    available, print the schdoc_file_content variable.

    :param schdoc_file_content: The content of the SchDoc file. This should be a
    dictionary.
    """

    components_list = []

    for value in schdoc_file_content.values():
        if isinstance(value, dict):
            if value.get("type") == "Component":
                attributes = value["attributes"]
                components_list.append(
                    _schdoc_component_from_attributes(
                        attributes,
                        attributes_mapper,
                    )
                )

    return components_list


def _extract_all_schdoc_components(
    repository: Repository,
    ref: Ref,
    schdoc_files_in_proj: set[str],
    attributes_mapping: AttributesMapping,
) -> list[SchematicComponent]:
    """
    Fetch all the components from all the SchDoc files in the repo that are in
    the project.
    """

    files_in_repo = repository.get_git_content(ref=ref)
    all_components = []
    for repo_file in files_in_repo:
        if repo_file.name in schdoc_files_in_proj:
            # If the file is not yet generated, we'll retry a few times.
            retry_count = 0
            while True:
                retry_count += 1

                try:
                    schdoc_file_json = repository.get_generated_json(repo_file, ref=ref)
                    all_components.extend(
                        _extract_components_from_schdoc(
                            schdoc_file_json,
                            attributes_mapping,
                        )
                    )

                    break
                except NotYetGeneratedException:
                    if retry_count > 20:
                        break

                    # Wait a bit before retrying.
                    time.sleep(0.5)
                    continue

    return all_components


def _extract_all_pcbdoc_components(
    repository: Repository,
    ref: Ref,
    pcbdoc_file: str,
) -> list[PcbComponent]:
    """
    Extract all the components from a PcbDoc file in the repo.
    """

    components = []

    component_instances = get_all_pcb_components(repository, ref, pcbdoc_file)

    for component in component_instances.values():
        try:
            schematic_link = component["schematic_link"]
        except KeyError:
            exit(f"Error: Component {component['designator']} in PCB with no schematic link.")
        components.append(
            PcbComponent(
                designator=component["designator"],
                schematic_link=schematic_link,
            )
        )

    return components


def _combine_components_to_ungrouped_bom(
    schdoc_components: list[SchematicComponent],
    pcbdoc_components: list[PcbComponent],
) -> list[BomEntry]:
    """
    Link the designators in the PcbDoc to a designator in the SchDocs, and
    generate a list of BOM entries. These BOM entries are not yet grouped by
    part number, and therefore have multiple rows for each part number.
    """

    schdoc_components_by_designator = {
        component.designator: component for component in schdoc_components
    }

    pcb_designators_for_schdoc_designators = {
        component.designator: [] for component in schdoc_components
    }
    orphan_pcb_components = []

    for pcbdoc_component in pcbdoc_components:
        if pcbdoc_component.schematic_link in schdoc_components_by_designator:
            schdoc_designator = pcbdoc_component.schematic_link
            pcb_designator = pcbdoc_component.designator

            pcb_designators_for_schdoc_designators[schdoc_designator].append(pcb_designator)
        else:
            orphan_pcb_components.append(pcbdoc_component)

    bom = []
    for (
        schdoc_designator,
        pcb_designators,
    ) in pcb_designators_for_schdoc_designators.items():
        schdoc_component = schdoc_components_by_designator[schdoc_designator]

        bom.append(
            BomEntry(
                description=schdoc_component.description,
                manufacturer=schdoc_component.manufacturer,
                part_number=schdoc_component.part_number,
                designators=pcb_designators,
                quantity=len(pcb_designators),
            )
        )
    for orphan_pcb_component in orphan_pcb_components:
        bom.append(
            BomEntry(
                description="",
                manufacturer="",
                part_number="",
                designators=[orphan_pcb_component.designator],
                quantity=1,
            )
        )

    return bom


def _group_bom_entries(bom_entries: list[BomEntry]) -> list[BomEntry]:
    """
    Group BOM Entries by the part number, combining the designators and
    quantities.
    """

    bom_entries_by_part_number = {}

    for bom_entry in bom_entries:
        if bom_entry.part_number != "":
            if bom_entry.part_number not in bom_entries_by_part_number:
                bom_entries_by_part_number[bom_entry.part_number] = bom_entry
            else:
                bom_entries_by_part_number[bom_entry.part_number].designators.extend(
                    bom_entry.designators
                )
                bom_entries_by_part_number[bom_entry.part_number].quantity += bom_entry.quantity

    return list(bom_entries_by_part_number.values())
