# -*- coding: utf-8 -*-
"""secretSanta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vh3OSSn7YkGTtGMxLnmXrL-9v15_AddB
"""

import numpy as np
import random

def check (senders, receivers):
  for i in range(len(senders)):
    if receivers[i] == senders[i]:
      return False
  return True

receivers = ["andre", "borghe", "saraC"]#, "roby", "auri", "ste", "giuli"] #receivers
senders = ["andre", "borghe", "saraC"]#, "roby", "auri", "ste", "giuli"] #senders

print (receivers)
print (senders)

while check(senders, receivers) == False:
  random.shuffle(receivers)

print (receivers)
print (senders)

import smtplib
from email.message import EmailMessage
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("bla@gmail.com", "bla")

for i in range(len(senders)):
  msg = EmailMessage()
  msg.set_content("Ciao "+senders[i]+",\nDovrai fare il regalo per "+receivers[i]+".\nBuon Natale con largo anticipo, e non ridurti all'ultimo!\n\nBabbo Secret Natale Santa")
  msg['Subject'] = 'secret santa :) '
  msg['From'] = "bla@gmail.com"
  msg['To'] = mails[i]
  server.send_message(msg)

server.quit()
