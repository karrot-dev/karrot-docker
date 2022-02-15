# This custom Dockerfile is so we can install postgres extensions.

FROM postgres:12

# based on https://github.com/postgis/docker-postgis/blob/4eb614133d6aa87bfc5c952d24b7eb1f499e5c7c/12-3.0/Dockerfile

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./extensions.sh /docker-entrypoint-initdb.d/extensions.sh