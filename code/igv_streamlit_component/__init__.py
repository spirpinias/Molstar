from pathlib import Path
from typing import Optional, Dict

import streamlit.components.v1 as components

frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "igv_streamlit_component", path=str(frontend_dir)
)


def igv_streamlit_component(
        params: Dict,
        key: Optional[str] = None,
):
    component_value = _component_func(
        params=params,
        key=key,
    )

    return component_value


def main():
    return


if __name__ == "__main__":
    main()
