import base64
from pathlib import Path

from molstar_streamlit_component import molstar_streamlit_component
from treeview_streamlit_component import treeview_streamlit_component

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CodeOcean Streamlit Components",
    layout="wide",
    initial_sidebar_state="expanded"
)


def local_url(path, out_type, encode=True):
    if encode:
        return f'data:@file/{out_type};base64,{base64.b64encode(open(path, "r").read().encode("UTF-8")).decode()}'
    else:
        return f'data:@file/{out_type};base64,{base64.b64encode(open(path, "rb").read())}'


def main():
    st.write("Select a `.pdb` file from `data` folder")
    if paths := treeview_streamlit_component({'path': '../data'}):
        pdbs = [path for path in paths if Path(path).suffix == '.pdb']
        file_tabs = st.tabs([pdb.replace('.pdb', '').replace('/root/capsule/data/', '') for pdb in pdbs])
        for i, pdb_name in enumerate(file_tabs):
            with file_tabs[i]:
                molstar_streamlit_component(params={
                    'url': local_url(pdbs[i], 'x-pdb'),
                    'format': 'pdb'}, key=f"{pdbs[i]}")


if __name__ == '__main__':
    main()
