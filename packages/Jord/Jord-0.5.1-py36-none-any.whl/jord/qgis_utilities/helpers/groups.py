from typing import Optional, Any

# noinspection PyUnresolvedReferences
from qgis.core import QgsLayerTreeGroup

__all__ = ["duplicate_groups"]


def duplicate_groups(
    group_to_duplicate, *, group_parent: Optional[Any] = None, appendix: str = " (Copy)"
) -> QgsLayerTreeGroup:
    assert (
        group_to_duplicate is not None
    ), f"{group_to_duplicate=} is required to create a duplicate group"

    if group_parent is None:
        group_parent = group_to_duplicate.parent()

    if group_parent is None:
        raise ValueError(f"Group parent was not found for {group_to_duplicate}")

    new_group_parent = group_parent.addGroup(f"{group_to_duplicate.name()}{appendix}")
    for original_group_child in group_to_duplicate.children():
        if isinstance(original_group_child, QgsLayerTreeGroup):
            new_child_group = duplicate_groups(
                original_group_child, group_parent=new_group_parent, appendix=""
            )  # Only top level
        else:
            new_group_parent.addChildNode(original_group_child.clone())

    return new_group_parent
