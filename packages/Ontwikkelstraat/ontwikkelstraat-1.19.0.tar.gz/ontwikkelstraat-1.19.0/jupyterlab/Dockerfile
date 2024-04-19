FROM jupyter/base-notebook:latest
#FROM jupyter/scipy-notebook:latest

# install gcc and dependencies useful to build some libraries/wheels
USER root
RUN apt update && apt install build-essential -y --no-install-recommends
RUN groupadd --gid 1050 microservices && usermod -aG microservices jovyan

USER ${NB_UID}
ARG PIP_INDEX_URL
RUN pip install pipx uv

# uv specific (requires venv):
ENV VIRTUAL_ENV="/home/jovyan/.venv"
RUN uv venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

COPY jupyterlab/requirements.txt .
RUN uv pip install -r ~/requirements.txt
