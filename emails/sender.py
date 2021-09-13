import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "devuay@gmail.com"
you = "albhuan@nuevaschool.org"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "repl.it"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
with open('./notes club/build_production/promotional.html', 'r') as rf:
    html = rf.read()

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText("terriffic amazing stuff yo\n", 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('devuay', 'password')
mail.sendmail(me, you, msg.as_string())
mail.quit()

