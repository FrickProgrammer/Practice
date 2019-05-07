import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('XXXXXXXXXXXXXXXXX@gmail.com', 'XXXXXXXXXXXXXXXXXXXXXX')

from_mail = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
to = 'XXXXXXXXXXXXXXXXXXXXXXXX'
body = 'Stock Algo Test Text Message'
message = ("From: %s\r\n" % from_mail + "To: %s\r\n" % to + "Subject: %s\r\n" % '' + "\r\n" + body)
server.sendmail(from_mail, to, message)
