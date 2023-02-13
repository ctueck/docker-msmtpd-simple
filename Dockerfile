FROM alpine:latest

ARG LC_ALL=C

# Install msmtpd
RUN apk add --no-cache msmtp gettext

# empty the default configuration & create empty dirs
RUN rm -f /etc/msmtprc

ADD entrypoint.sh /bin/
ADD msmtprc /usr/local/share/etc-templates/

ENTRYPOINT [ "/bin/entrypoint.sh" ]

CMD [ "/usr/bin/msmtpd", "--interface=0.0.0.0" ]

