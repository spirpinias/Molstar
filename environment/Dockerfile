# hash:sha256:46c9cc66356c52c68d982514671567cce4f0982db23dc64b17166ba5867cbf52
FROM registry.acmecorp-edge.codeocean.com/codeocean/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    pillow==9.5.0 \
    streamlit==1.25.0
