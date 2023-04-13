# hash:sha256:46a8ac7eb0a53ed291f07088029cf70209073ba952f3c6e52ea482b301d3ed01
FROM registry.acmecorp-edge.codeocean.com/codeocean/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    pillow \
    streamlit
