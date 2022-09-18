Simple dockerized msmtpd
========================

The main point of this container is to run one single [msmtpd](https://marlam.de/msmtp/) that relays outgoing mail to an external SMTP server. It could be used by several other services/containers, while the outgoing SMTP credentials are saved in one single place only, the `.env` file for this container.

Configuration
-------------

The template `msmtprc` file is parsed by envsubst(1) on container start.

- `MSMTP_PORT`: local (address:)port on which to listen (default: `2525`)
- `MSMTP_TLS`: turn TLS on or off (default: `on`)
- `MSMTP_DOMAIN`: email domain (default: `example.com`)
- `MSMTP_FROM`: envelope-from address (default: `no-reply@$MSMTP_DOMAIN`)
- `MSMTP_RELAY`: SMTP relay hostname
- `MSMTP_RELAY_PORT`: SMTP relay port (default: `587`)
- `MSMTP_RELAY_USER` and `MSMTP_RELAY_PASSWORD`: SMTP relay credentials

Envelope-from addresses
-----------------------

The default configuration tries to ensure that envelope-from addresses are useful:

1. If the application provides an envelope-from address with `MSMTP_DOMAIN` as the domain part, it remains unchanged.
2. Any other envelope-from addresses are rewritten to `MSMTP_FROM`.

