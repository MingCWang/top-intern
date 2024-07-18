import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import os

def send_email(job_data):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'deiseval26@gmail.com'
    sender_password = os.environ.get('GMAIL_PASSWORD')
    receiver_email = 'mingshihwang@brandeis.edu'
    # Create the email content
    subject = 'Meta Job'
    if len(job_data) == 0:
        subject += 'No new jobs found!'
        body = '=='
    elif job_data[-1]['status'] == 'completed':
        subject += 'Collected!'
        job_data.pop()
        for job in job_data:
            body += f"\nJob Name: {job['jobName']}\nJob URL: {job['jobURL']}"
    else:
        subject = 'Meta Job data scraping failed!'
        body = ':('
    
  
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')




def main():
    
    with open("new.json", "r") as file:
        # Send the email after scraping
        data = json.load(file)
        send_email(data)


main()

