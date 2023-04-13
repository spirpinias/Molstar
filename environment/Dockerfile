# hash:sha256:1fdf516f0d2b6231c83e49039c2de0eb0ab16e240633b89f942e76055792490e
FROM registry.acmecorp-edge.codeocean.com/codeocean/mambaforge:22.11.1-4

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    pillow==9.5.0 \
    streamlit==1.21.0
