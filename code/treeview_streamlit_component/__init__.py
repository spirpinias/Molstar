from pathlib import Path
from typing import Optional

import streamlit.components.v1 as components

frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "treeview_streamlit_component", path=str(frontend_dir)
)


def create_node(path):
    """Create a node object for a given path"""
    node = {'id': str(path.resolve()), 'text': path.name}
    if path.is_dir():
        node['children'] = [create_node(child) for child in path.iterdir()]
    return node


def treeview_streamlit_component(
        params: str,
        key: Optional[str] = None,
):
    component_value = _component_func(
        params=create_node(Path(params)),
        key=key,
    )

    return component_value


def main():
    return


if __name__ == "__main__":
    main()
