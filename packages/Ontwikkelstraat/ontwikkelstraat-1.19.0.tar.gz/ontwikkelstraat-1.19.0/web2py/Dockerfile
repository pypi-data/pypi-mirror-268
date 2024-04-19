# base on ubuntu LTS as it's faster than python3 image
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --yes curl p7zip-full aria2 git wget

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# p7zip-full and aria2 are fully optional a.t.m.
RUN groupadd --gid 1050 microservices && useradd --uid 1050 --gid microservices --create-home microservices

ARG PIP_INDEX_URL
RUN export PIP_INDEX_URL=${PIP_INDEX_URL}
RUN pip install uv pipx

# uv specific (requires venv):
ENV VIRTUAL_ENV="/opt/venv"
RUN uv venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# installeert web2py naar /src/web2py (normale pip want 'uv' crasht op web2py's rare versienummers)
RUN pip install --no-cache -e git+https://github.com/web2py/web2py@v2.22.5#egg=web2py

# keep app requirements in the project folder on the devel machine. p4w-test here in the screenshot below.
COPY web2py/requirements.txt /w2p/requirements.txt

# install all the applicatoin requirements in the global environment. it's a container, so no need to use venv
RUN uv pip install --no-cache -r /w2p/requirements.txt

# chdir to the directory where password and apps folder is, this is the base
# directory from which to start py4web.
WORKDIR  /src/web2py
RUN chown microservices:microservices -R /src/web2py
# expose py4web on it's default port
EXPOSE 8000

ENV PYTHON_PATH=/src/web2py
COPY web2py/routes.py /src/web2py/routes.py
# -K : run scheduled tasks  for specified apps
# -X : run scheduler alongside webserver
# both are required...
CMD ['python3','web2py.py','-a','\$WEB2PY_PASSWORD','-i','0.0.0.0','-p','8000','-K','init','-X']
