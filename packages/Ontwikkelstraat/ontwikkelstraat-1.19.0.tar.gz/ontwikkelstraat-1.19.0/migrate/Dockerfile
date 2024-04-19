# https://code.dutveul.nl/EducationWarehouse/Docker/straat/files/tip/netwerktest/Dockerfile?at=tip
# base on ubuntu LTS as it's faster than python3 image
# use unbuffered mode, and disable prompts for tzdata during install
# might require a later `dpkg reconfigure tzdata`
#FROM ubuntu:22.04 as base
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
# aria2 is required for downloading at highspeed and more protocols
# pzip-full is required to unpack the database files
# postgresql-client is used for psql to restore backups
RUN apt-get update && \
    apt-get install --yes apt-utils curl p7zip-full aria2 postgresql-client wget

#RUN python3 -m pip install --upgrade pip
#RUN python3 -m pip install --upgrade setuptools

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN groupadd --gid 1050 microservices && useradd --uid 1050 -g microservices microservices

# onderstaande wordt telkens overschreven vanuit de docker-compose file
# om de bewuste microservice te starten, maar wel allemaal op basis van deze image.
ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN mkdir /home/microservices && chown microservices:microservices /home/microservices

RUN pip install pipx uv

# uv specific (requires venv):
ENV VIRTUAL_ENV="/opt/venv"
RUN uv venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

USER microservices
# install as the microservices user, and authenticate accordingly
RUN pipx install b2
ARG B2_ATTACHMENTS_KEYID
ARG B2_ATTACHMENTS_KEY
RUN if [ "${B2_ATTACHMENTS_KEYID}" ]; then ~/.local/bin/b2 authorize-account ${B2_ATTACHMENTS_KEYID} ${B2_ATTACHMENTS_KEY}; fi;

USER root
COPY migrate/requirements.txt /home/microservices
RUN uv pip install -r /home/microservices/requirements.txt

USER microservices
## expects a config file, use EDWH_MICROSERVICES_CONFIG in the environment, or use --config=filename
CMD python3 /shared_code/edwh/core/migrate.py

