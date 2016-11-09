FROM nginx:1.11-alpine
MAINTAINER Stefan Gangefors <stefan@gangefors.com>

ARG TAIGA_FRONT_VERSION=3.0.0-stable

# Install build dependencies
RUN buildDeps=' \
        git \
    ' \
    && export DEBIAN_FRONTEND=noninteractive \
    && apk add --no-cache $buildDeps \
# Clone taiga-front-dist
    && git clone https://github.com/taigaio/taiga-front-dist.git /taiga/front \
    && cd /taiga/front \
    && git checkout $TAIGA_FRONT_VERSION \
# Remove build dependencies
    && apk del --no-cache $buildDeps

# Configure taiga-front-dist
RUN mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled
RUN rm /etc/nginx/conf.d/*
COPY mime.types /etc/nginx/mime.types
COPY nginx.conf /etc/nginx/nginx.conf
COPY server_defaults.conf /etc/nginx/server_defaults.conf
COPY http.conf /etc/nginx/sites-available/http.conf
COPY https.conf /etc/nginx/sites-available/https.conf
COPY init /taiga/init

EXPOSE 80 443

CMD ["/taiga/init"]
