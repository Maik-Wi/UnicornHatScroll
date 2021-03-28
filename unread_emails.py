#!/usr/bin/env python
# -*- coding: utf-8 -*-


#This script displays unread emails


import imaplib
from UHScroll import *

IMAPSERVER = 'YOUR_SERVER'
USER = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'

mail = imaplib.IMAP4_SSL(IMAPSERVER)
mail.login(USER, PASSWORD)
mail.select('inbox', True) # connect to inbox.
return_code, mail_ids = mail.search(None, 'UnSeen')
count = len(mail_ids[0].split(' '))
mail.close()
mail.logout()

#konvertiert den Wert in Text um
converted_count = '% s' % count
print count,' ungelesene E-Mail'

if count > 0:
  unicorn_scroll(converted_count+' ~email','cyan',120,0.15)
else:
  print("keine ungelesenen Mails")
