# hash:sha256:cfc1a17be3b6d7f657f3c8702d98b0a01cf15b7691075f70c858be048ce444d6
FROM registry.acmecorp-edge.codeocean.com/codeocean/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    pillow==9.5.0 \
    streamlit==latest
