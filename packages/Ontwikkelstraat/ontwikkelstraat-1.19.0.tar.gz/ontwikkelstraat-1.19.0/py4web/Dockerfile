FROM python:3.11
# Py4web uses Bjoern, which requires uv-loop (using apt install libev-dev) and gcc: therefor the `python:3.11-slim`
# image isn't a fit because it lacks the compiler.


ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
# aria2 is required for downloading at highspeed and more protocols
# pzip-full is required to unpack the database files
# postgresql-client is used for psql to restore backups
RUN apt-get update && \
    apt-get install --yes apt-utils curl p7zip-full aria2 postgresql-client wget libev-dev sqlite3

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# p7zip-full and aria2 are fully optional a.t.m.
RUN groupadd --gid 1050 microservices && useradd --uid 1050 -g microservices microservices
RUN mkdir /home/microservices
RUN chown -R microservices:microservices /home/microservices

ARG PIP_INDEX_URL
RUN export PIP_INDEX_URL=${PIP_INDEX_URL}
RUN pip install uv pipx

# uv specific (requires venv):
ENV VIRTUAL_ENV="/opt/venv"
RUN uv venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

WORKDIR  /p4w
# expose py4web on it's default port
EXPOSE 8000
EXPOSE 7999

# install all the applicatoin requirements in the global environment. it's a container, so no need to use venv
COPY py4web/requirements.txt /p4w/requirements.txt
RUN uv pip install --upgrade --no-cache -r /p4w/requirements.txt

# run py4web and have it bind to the outside ip addresses
# CMD ["py4web", "run", "-H", "0.0.0.0", "-p", "./password.txt", "apps", "--watch","sync", "--server","waitress","--number_workers","16"]
# for --thunder-lock see https://uwsgi-docs.readthedocs.io/en/latest/articles/SerializingAccept.html
# RUN pip install pydevd-pycharm~=221.6008.17

USER microservices
ENV PATH=/home/microservices/.local/bin:$PATH
CMD ["uwsgi", "--http", ":8000", "--wsgi-file", "py4web_wsgi.py", "--master", "--processes", "1", "--threads", "12", "--stats", "0.0.0.0:7999","--thunder-lock", "--touch-reload", "/p4w/reload.uwsgi"]
# dev:
# CMD ["py4web", "run", "-H", "0.0.0.0", "-p", "./password.txt", "apps", "--watch", "sync", "--server", "tornado"]
