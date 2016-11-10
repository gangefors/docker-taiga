FROM nginx:1.11-alpine
MAINTAINER Stefan Gangefors <stefan@gangefors.com>

ARG TAIGA_VERSION=3.0.0-stable

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
COPY nginx/* /etc/nginx/
COPY init /taiga/init

EXPOSE 80 443

CMD ["/taiga/init"]
