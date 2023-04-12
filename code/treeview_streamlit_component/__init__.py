from pathlib import Path
from typing import Optional, Dict

import streamlit.components.v1 as components

frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "treeview_streamlit_component", path=str(frontend_dir)
)


def get_file_extensions(path: Path):
    """
    Recursively walks over all folders, sub-folders, and files of a given directory path using pathlib
    and returns a list of file extensions from these folders.
    """
    extensions = []
    for element_path in path.rglob('*'):
        if element_path.is_file():
            extensions.append(element_path.suffix)
    return sorted(list(set(extensions)))


def create_node(path: Path):
    """Create a node object for a given path"""
    node = {'id': str(path.resolve()), 'text': path.name}
    if path.is_dir():
        node['children'] = [create_node(child) for child in path.iterdir()]
    return node


def treeview_streamlit_component(
        params: Dict,
        key: Optional[str] = None,
):

    path = Path(params.get('path', '.'))
    extensions = params.get('extensions') if params.get('extensions', []) else get_file_extensions(path)
    component_value = _component_func(
        path=create_node(path),
        extensions=extensions,
        key=key,
    )

    return component_value


def main():
    t = treeview_streamlit_component({
        'path': '/Users/codeocean/Temp/data'
    })


if __name__ == "__main__":
    main()
