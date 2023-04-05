# hash:sha256:b06dc509f25e812c3fadb16ce9e413408596350a2830eb59f3856a4c3b6b7b78
FROM registry.acmecorp-edge.codeocean.com/codeocean/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    streamlit
