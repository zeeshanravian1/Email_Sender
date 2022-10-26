import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('html_file.html').read_text())
email = EmailMessage()
email['from'] = 'Zeeshan Asim'
email['to'] = 'zeeshanravian1@gmail.com'
email['subject'] = 'Job Vacency'
email.set_content('hjftyc')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('honeybutt1995@gmail.com', '123456789@H')
    smtp.send_message(email)
    print('Done!')