Taiga backend Docker image
==========================

Use this Docker image to launch an instance of the Taiga backend.

    docker-compose run taiga-back

This will also launch the database container. Use `--no-deps` to ignore that
dependency.

Volumes
-------

- `/var/lib/postgresql/data`

  Database files. Used by taiga-db service. See the [docker-compose.yml][1]
  file for details.

- `/taiga/logs/`

  Application logs.

- `/taiga/media/`

  Django user-uploaded media files.

- `/taiga/static/`

  Django static files.


Ports
-----

- `8000`

  The REST API is exposed on this port.


Environment
-----------

### Taiga settings

- `HOSTNAME`, default: localhost

  Public hostname of the service.

- `API_SCHEME`, default: http

  Protocol scheme token for the REST API (http or https).

- `API_DOMAIN`, default $HOSTNAME

  Domain name for the REST API.

- `FRONT_SCHEME`, default: https

  Protocol scheme token for the frontend (http or https). Must be the same
  value as in the Taiga frontend.

- `FRONT_DOMAIN`, default $HOSTNAME

  Domain name for the frontend.

- `PUBLIC_REGISTER_ENABLED`, default: true

  Allow public registration.

- `USER_EMAIL_ALLOWED_DOMAINS`, default: no limit

  Limit user registration to a list of specific domains. Must be a comma
  separated string.

- `FEEDBACK_ENABLED`, default: false

  Allow feedback through the UI. Must be the same value as in the Taiga
  frontend.

- `FEEDBACK_EMAIL`, default: support@taiga.io

  Email to send feedback to.


### Django settings

See the Django settings [documentation][2] for more info.

- `DEBUG`, default: false

  A boolean that turns on/off debug mode.

- `LANGUAGE_CODE`, default: en-us

  A string representing the language code for this installation.

- `SECRET_KEY`, default: secretkey

  A secret key used to provide cryptographic signing. Should be set to a
  unique, unpredictable value.

- `TIME_ZONE`, default: UTC

  A string representing the time zone for this installation.

#### Email

- `DEFAULT_FROM_EMAIL`, default: no-reply@$HOSTNAME

  Default email address to use for various automated correspondence.

- `SERVER_EMAIL`, default: $DEFAULT_FROM_EMAIL

  The email address that error messages come from.

- `EMAIL_USE_TLS`, default: false

  Whether to use a TLS (secure) connection when talking to the SMTP server.

- `EMAIL_HOST`, default: $HOSTNAME

  The host to use for sending email.

- `EMAIL_PORT`, default: 25

  Port to use for the SMTP server defined in $EMAIL_HOST.

- `EMAIL_HOST_USER`, default: an empty string

  Username to use for the SMTP server defined in $EMAIL_HOST. If empty, Django
  won’t attempt authentication.

- `EMAIL_HOST_PASSWORD`, default: an empty string

  Password to use for the SMTP server defined in $EMAIL_HOST. If empty, Django
  won’t attempt authentication.


### Database settings

- `DB_HOST`, default: taiga-db

  Hostname of the database host.

- `DB_PORT`, default: 5432

  Port for the database.

- `DB_NAME`, default: taiga

  Name of the database.

- `DB_USER`, default: taiga

  Name of the database user.

- `DB_PASSWORD`, default: taiga

  Password for the database.


[1]: ../docker-compose.yml
[2]: https://docs.djangoproject.com/en/dev/ref/settings/
