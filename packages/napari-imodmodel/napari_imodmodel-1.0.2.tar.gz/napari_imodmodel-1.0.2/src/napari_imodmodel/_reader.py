from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)
from pathlib import Path

import numpy as np

from imodmodel import ImodModel

if TYPE_CHECKING:
    from typing import Iterable
    from napari.types import LayerDataTuple


def _obj_type(flags: int) -> str:
    if flags & 1<<9: # bit 9
        return "scattered"
    elif flags & 1<<3: # bit 3
        return "open"
    return "closed"

def napari_get_reader(path: Union[str, List[str]]) -> Optional[Callable]:
    if not isinstance(path, list):
        path = [path]
    print("getting reader")
    if not all(map(lambda p: p.endswith(".mod"), path)):
        return None
    return reader_function


def read_model(path: Path) -> "Iterable[LayerDataTuple]":
    model = ImodModel.from_file(path)
    for obj_num, obj in enumerate(model.objects, start=1):
        color = np.array([obj.header.red, obj.header.green, obj.header.blue])
        obj_type = _obj_type(obj.header.flags)
        layer_data = [
            contour.points[:, (2, 1, 0)]
            for contour in obj.contours
        ]
        kwargs = {
            "name": f"{path.stem} obj {obj_num}",
            "edge_color": "#" + ''.join([f'{int(c*255):0>2x}' for c in color]),
            }
        if obj_type == "scattered":
            layer_type = "points"
            layer_data = np.concatenate(layer_data)
        else:
            layer_type = "shapes"
            kwargs["shape_type"] = "path" if obj_type == "open" else "polygon"
        yield layer_data, kwargs, layer_type

        for mesh_num, mesh in enumerate(obj.meshes, start=1):
            vertex_colors = np.broadcast_to(color, (len(mesh.vertices), 3))
            if mesh.face_values is None:
                mesh_data = (mesh.vertices[:, (2, 1, 0)], mesh.indices)
            else:
                mesh_data = (mesh.vertices[:, (2, 1, 0)], mesh.indices, mesh.face_values)
            mesh_kwargs = {
                "name": f"{kwargs['name']} mesh {mesh_num}",
                "vertex_colors": vertex_colors,
                "shading": "smooth",
            }
            yield mesh_data, mesh_kwargs, "surface"


def reader_function(
    paths: Union[str, List[str]]
) -> List[Tuple[Any, Dict, str]]:
    if not isinstance(paths, list):
        paths = [paths]
    layers = list()
    for path in paths:
        layers += list(read_model(Path(path)))
    return layers
