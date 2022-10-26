import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('html_file.html').read_text())
email = EmailMessage()
email['from'] = 'Sender Name'
email['to'] = 'Receiver Email'
email['subject'] = 'Job Vacency'
email.set_content('hjftyc')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Sender Email', 'Sender Email Password')
    smtp.send_message(email)
    print('Done!')
