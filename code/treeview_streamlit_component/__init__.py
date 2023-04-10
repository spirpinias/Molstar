from pathlib import Path
from typing import Optional, Dict

import streamlit.components.v1 as components

frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "treeview_streamlit_component", path=str(frontend_dir)
)


def create_node(path, file_extensions):
    """Create a node object for a given path"""
    node = {'id': str(path.resolve()), 'text': path.name}
    if path.is_dir():
        node['children'] = [create_node(child) for child in path.iterdir() if child.suffix in file_extensions]
    return node


def treeview_streamlit_component(
        params: Dict(str),
        key: Optional[str] = None,
):
    component_value = _component_func(
        params=create_node(Path(params.get("path", "")), params.get("ext", None)),
        key=key,
    )

    return component_value


def main():
    return


if __name__ == "__main__":
    main()
