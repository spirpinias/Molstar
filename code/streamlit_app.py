import base64
from pathlib import Path

from igv_streamlit_component import igv_streamlit_component
from molstar_streamlit_component import molstar_streamlit_component
from treeview_streamlit_component import treeview_streamlit_component

import streamlit as st

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
    igv, molstar, treeview = st.tabs(["IGV", "Mol*", "Treeview"])

    with igv:
        igv_streamlit_component(params={
            "genome": "hg38",
            "locus": "chr8:127,736,588-127,739,371",
            "tracks": [
                {
                    "name": "HG00103",
                    "url": "https://s3.amazonaws.com/1000genomes/data/HG00103/alignment/HG00103.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram",
                    "indexURL": "https://s3.amazonaws.com/1000genomes/data/HG00103/alignment/HG00103.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram.crai",
                    "format": "cram"
                }
            ]
        })

    with molstar:
        st.write('From URL')
        molstar_streamlit_component(params={
            'url': 'https://gist.githubusercontent.com/maxim-k/4722a862190a1ec609c61185f07589e8/raw/95cd818d8c4297544ac8d98df450f6380501c648/example.pdb',
            'format': 'pdb'}, key="url")
        st.write('From "data" folder')
        molstar_streamlit_component(params={
            'url': local_url('../data/molstar_example/example.pdb', 'x-pdb'),
            'format': 'pdb'}, key="local")

    with treeview:
        if paths := treeview_streamlit_component({'path': '../data/'}):
            for path in paths:
                if Path(path).suffix == '.pdb':
                    molstar_streamlit_component(params={
                        'url': local_url(path, 'x-pdb'),
                        'format': 'pdb'}, key=f"{path}")


if __name__ == '__main__':
    main()
