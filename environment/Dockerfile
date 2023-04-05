# hash:sha256:4e09f98ba20f3e95271fda16776b39355377692cfa5f76c9b8400efddcf8c7a2
FROM registry.acmecorp-edge.codeocean.com/codeocean/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    streamlit==1.20.0
