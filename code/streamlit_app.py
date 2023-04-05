import base64
from io import StringIO

import streamlit as st

from molstar_streamlit_component import molstar_streamlit_component
from igv_streamlit_component import igv_streamlit_component

st.set_page_config(
    page_title="CodeOcean Streamlit Components",
    layout="wide",
    initial_sidebar_state="expanded"
)

def local_url(path):
    return f'data:@file/x-pdb;base64,{base64.b64encode(open(path, "r").read().encode("UTF-8")).decode()}'

def main():
    molstar, igv = st.tabs(["Mol*", "IGV"])
    with molstar:
        molstar_streamlit_component(params={
            'url': 'https://gist.githubusercontent.com/maxim-k/4722a862190a1ec609c61185f07589e8/raw/95cd818d8c4297544ac8d98df450f6380501c648/example.pdb',
            'format': 'pdb'}, key="url")

        molstar_streamlit_component(params={
            'url': local_url('../data/molstar_example/example.pdb'),
            'format': 'pdb'}, key="local")        

    with igv:
        igv_streamlit_component(params={
            'genome': 'hg38',
            'locus': 'chr8:127,736,588-127,739,371',
            'tracks': [
                {
                    'name': 'BAM',                  
                    'url': local_url('../data/HaplotypeCaller/inputs/NA12878_wgs_20.bam'),
                    'indexURL': local_url('../data/HaplotypeCaller/inputs/NA12878_wgs_20.bai'),
                    'format': 'bam',
                    'type': 'alignment'
                }
            ]
        })        

if __name__ == '__main__':
    main()