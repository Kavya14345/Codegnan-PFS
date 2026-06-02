'''
SMTP(Simple Mail Transfer Protocol)
====================================
-->This is used to send emails from server to another server......
Note:
-----
1.SMTP SSL Port:
465

2.SMTP TLS Port:
587

import smtplib

EmailMessage Class
------------------
msg['Subject']='SMTP ON Mail'
msg['From']='sender@mail.com'
msg['To']='Receiver@mail.com'

app password:xdaoaougczguxubs

import smtplib
from email.message import EmailMessage
sender='kavs14345@gmail.com'
password='hjjzuvkmgsijigvw'
msg=EmailMessage()
msg['Subject']=''
msg['From']=sender
msg['To']='rohansai4645@gmail.com'
msg.set_content('hi')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()


'''
import smtplib
from email.message import EmailMessage
sender='kavs14345@gmail.com'
password='hjjzuvkmgsijigvw'
receiver=['rohansai4645@gmail.com','deepthiseerapu2004@gmail.com','reshmanaguru30@gmail.com']
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    msg=EmailMessage()
    msg['Subject']='Infosys'
    msg['From']=sender
    msg['To']=email
    msg.set_content('You are successfully rejected for the interview')
    server.send_message(msg)
server.quit()
