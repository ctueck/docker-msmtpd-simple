#!/bin/sh
#
# entrypoint.sh - create configuration file from environment variables
#

# configuration defaults (because envsubst doesn't support default values)
set -a
MSMTP_DOMAIN="${MSMTP_DOMAIN:-example.com}"
MSMTP_FROM="${MSMTP_FROM:-no-reply@$MSMTP_DOMAIN}"
MSMTP_RELAY_PORT="${MSMTP_RELAY_PORT:-587}"
MSMTP_TLS="${MSMTP_TLS:-on}"
set +a

# generate configs
echo -n "Generating /etc/msmtprc: "
envsubst < /usr/local/share/etc-templates/msmtprc > /etc/msmtprc
chmod 0600 /etc/msmtprc
echo "Done."

exec "$@"

