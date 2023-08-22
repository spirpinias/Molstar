import base64
from pathlib import Path

from molstar_streamlit_component import molstar_streamlit_component
from treeview_streamlit_component import treeview_streamlit_component

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="CodeOcean Streamlit Mol* Demo",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.image(Image.open("code/static/CO_logo_135x72.png"), caption="Code Ocean")


def local_url(path, out_type, encode=True):
    if encode:
        return f'data:@file/{out_type};base64,{base64.b64encode(open(path, "r").read().encode("UTF-8")).decode()}'
    else:
        return f'data:@file/{out_type};base64,{base64.b64encode(open(path, "rb").read())}'


def main():
    pdbs = []
    with st.sidebar:
        st.title("Mol* Viewer")

        st.write("Select a `.pdb` file from `data` folder")
        if paths := treeview_streamlit_component({'path': 'data'}):
            pdbs = [path for path in paths if Path(path).suffix == '.pdb']

        st.sidebar.write("Or upload a `.pdb` file from your local folder")
        # Upload from a local machine
        local_upload = st.sidebar.file_uploader(
            """
            Upload a protein structure in PDB format""",
            type=["pdb"],
            key="pdb",
            label_visibility="collapsed"
        )
        if local_upload:
            with open(f"../data/{local_upload.name}", "wb") as local_pdb:
                local_pdb.write(local_upload.getvalue())
            pdbs.append(f"../data/{local_upload.name}")

    if pdbs:
        file_tabs = st.tabs(
            [pdb.replace('.pdb', '').replace('../data/', '')
             for pdb in pdbs])
        for i, pdb_name in enumerate(file_tabs):
            with file_tabs[i]:
                molstar_streamlit_component(params={
                    'url': local_url(pdbs[i], 'x-pdb'),
                    'format': 'pdb'}, key=f"{pdbs[i]}")


if __name__ == '__main__':
    main()
