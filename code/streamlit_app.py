import streamlit as st

from molstar_streamlit_component import molstar_streamlit_component
from igv_streamlit_component import igv_streamlit_component

st.set_page_config(
    page_title="CodeOcean Streamlit Components",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    molstar, igv = st.tabs(["Mol*", "IGV"])
    with molstar:
        molstar_streamlit_component(params={
            'url': 'https://gist.githubusercontent.com/maxim-k/4722a862190a1ec609c61185f07589e8/raw/95cd818d8c4297544ac8d98df450f6380501c648/example.pdb',
            'format': 'pdb'})

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

if __name__ == '__main__':
    main()