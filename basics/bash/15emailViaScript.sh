#! /bin/bash

# to work with emails
# sudo apt install ssmtp

# than do to Icon (upRight) > google account > Seucrity > Less secure app access on

# configure the conf
# vim /etc/ssmtp/ssmtp.conf
# write the next:
: '
root=testemail@gmail.com
mailhub=smtp.gmail.com:587	587 is tls port
AuthUser=testemail@gmail.com
AuthPass=password
UseSTARTTLS=yes
'

ssmtp testemail@gmail.com
# when run the programm write this:
# To: testemail2@gmail.com
# From: testemail@gmail.com
# Cc: testemail@gmail.com
# Subject: TEST
# This it body
# ....






