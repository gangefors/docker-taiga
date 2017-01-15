Taiga docker images
===================

This repository contains everything you need to build taiga-back and
taiga-front docker images and set up your own Taiga server.

To start your own Taiga instance just use the docker-compose file available.

    docker-compose up -d

Taiga will be available on [https://localhost](1)

Default user / password is `admin` / `123123`

For details on configuring the [backend](2) or [frontend](3), see their
respective README.

[1]: https://localhost
[2]: ./taiga-back/README.md
[3]: ./taiga-front/README.md
