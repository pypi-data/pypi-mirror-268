import uuid

__all__ = ["randomize_field", "randomize_sub_tree_field"]


def randomize_sub_tree_field(selected_nodes, field_name: str) -> None:
    # noinspection PyUnresolvedReferences
    from qgis.core import QgsLayerTreeGroup, QgsLayerTreeLayer

    for group in selected_nodes:
        if isinstance(group, QgsLayerTreeLayer):
            randomize_field(group, field_name=field_name)
        elif isinstance(group, QgsLayerTreeGroup):
            randomize_sub_tree_field(group.children(), field_name=field_name)
        else:
            ...


def randomize_field(tree_layer, field_name: str) -> None:  #: QgsLayerTreeLayer
    """
        https://qgis.org/pyqgis/3.28/core/QgsVectorLayer.html#qgis.core.QgsVectorLayer.changeAttributeValues

    changeAttributeValues
    fid: int, newValues: Dict[int, Any], oldValues: Dict[int, Any] = {}, skipDefaultValues: bool = False

        :param field_name:
        :param tree_layer:
        :return:
    """
    layer = tree_layer.layer()

    field_idx = layer.fields().indexFromName(field_name)

    if field_idx >= 0:
        layer.startEditing()
        layer.beginEditCommand(f"Regenerate {field_name}")
        for i in range(layer.featureCount() + 1):
            layer.changeAttributeValue(i, field_idx, uuid.uuid4().hex)

        # layer.rollBack()
        layer.endEditCommand()
        layer.commitChanges()
