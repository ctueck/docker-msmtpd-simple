#!/usr/bin/env python

import sys
import smtplib
import os
import argparse

from ansi2html import Ansi2HTMLConverter

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

Ansi2HTML = Ansi2HTMLConverter()

parser = argparse.ArgumentParser()
parser.add_argument("TO",               default=os.environ.get('ANSI_MAILER_TO'),
                                        nargs='*',
                                        help="Email recipient/s (default: ANSI_MAILER_TO)")
parser.add_argument("-s", "--subject",  default=os.environ.get('ANSI_MAILER_SUBJECT', 'ANSI mailer'),
                                        help="Subject (default: ANSI_MAILER_SUBJECT or 'ANSI mailer')")
parser.add_argument("-f", "--sender",   default=os.environ.get('ANSI_MAILER_FROM', 'noreply@example.org'),
                                        help="Sender address (default: ANSI_MAILER_FROM or 'noreply@example.org')")
parser.add_argument("-r", "--relay",    default=os.environ.get('ANSI_MAILER_RELAY', 'localhost'),
                                        help="SMTP mail relay (default: ANSI_MAILER_RELAY or localhost)")
parser.add_argument("-p", "--port",     default=os.environ.get('ANSI_MAILER_PORT', 587),
                                        type=int,
                                        help="SMTP mail relay (default: ANSI_MAILER_PORT or 587)")
args = parser.parse_args()

# check environment/parameters
if not args.TO:
    raise Exception("Sorry, I cannot send an email without To: address")

# convert stdin to HTML
html = Ansi2HTML.convert("".join(sys.stdin.readlines()))

# create the email
msg = EmailMessage()
msg['Subject'] = args.subject
msg['From'] = args.sender
msg['To'] = args.TO
msg.set_content(html, subtype='html')

# send the message via SMTP server
with smtplib.SMTP(args.relay, port=args.port) as relay:
    relay.send_message(msg)

