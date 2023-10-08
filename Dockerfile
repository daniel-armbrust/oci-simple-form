#
# Dockerfile
#
FROM container-registry.oracle.com/os/oraclelinux:8-slim

LABEL maintainer="Daniel Armbrust <darmbrust@gmail.com>"

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=0
ENV FLASK_ENV=production
ENV STATIC_URL=/static
ENV STATIC_PATH=/opt/oci-simple-form/static

WORKDIR /opt/oci-simple-form

COPY requirements.txt ./
COPY docker-entrypoint.sh ./

RUN microdnf update -y && \
    microdnf install -y python3.8 && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    microdnf clean all && rm -rf /var/cache/yum    

RUN adduser -l -d /opt/oci-simple-form webapp

COPY --chown=webapp:webapp ./app /opt/oci-simple-form/

USER webapp
EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]
