import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import os
from companies.meta.meta import Meta
from companies.tiktok.tiktok import Tiktok

def send_email(job_data):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'deiseval26@gmail.com'
    sender_password = os.environ['GMAIL_PWD']
    receiver_email = 'mingshihwang@brandeis.edu'
    
    have_new_jobs = False
    body = ''
    subject = ''
    # Create the email content
    for job in job_data:
        company = job[-1]['company']
        if job[-2]['status'] == 'failed':
            body += f'<p style="font-family: Arial, sans-serif; font-size: 16px; color: red;">Scraping for {company} failed :(</p>'
            print(f'Scraping {company} failed!')
        elif len(job) - 2 == 0:
            body += f'<p style="font-family: Arial, sans-serif; font-size: 16px;">No new {company} jobs found</p>'
            print(f'No new jobs {company} found!')
        elif job[-2]['status'] == 'completed':
            job.pop()  # remove the status key
            job.pop()  # remove the company key
            body += f'<h2 style="font-family: Arial, sans-serif; font-size: 16px; color: #4CAF50;">New {company} jobs!</h2>'
            for j in job:
                body += f"<p style='font-family: Arial, sans-serif; font-size: 14px;'><strong>Job Name:</strong> {j['jobName']}<br><strong>Job URL:</strong> <a href='{j['jobURL']}'>{j['jobURL']}</a></p>"
            print(f'Found new {company} jobs!')
            have_new_jobs = True

    if have_new_jobs:
        subject = 'It\'s go time !'
    else:
        subject = 'No New Jobs Found'
        
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'html'))

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
    
    job_data = []
    meta = Meta()
    meta_list = meta.run()
    job_data.extend([meta_list])

    tiktok = Tiktok()
    tiktok_list = tiktok.run()
    job_data.extend([tiktok_list])	
 
    send_email(job_data)
 
 
    
    
main()

