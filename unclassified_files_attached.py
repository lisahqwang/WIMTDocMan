import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
def send_email_with_attachments(file_paths, sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_user, smtp_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
 
    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))
 
    # Attach each file
    for file_path in file_paths:
        if os.path.isfile(file_path):
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
                msg.attach(part)
        else:
            print(f"File not found: {file_path}")
 
    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
 
# Example usage
if __name__ == "__main__":
    # Path to the .txt file containing the list of file names
    txt_file_path = '/path/to/your/file_list.txt'
 
    # Directory containing the files
    directory = '/usr/local/src/'
 
    # Read the list of file names from the .txt file
    with open(txt_file_path, 'r') as file:
        file_names = [line.strip() for line in file.readlines()]
 
    # Full paths to the files
    file_paths = [os.path.join(directory, file_name) for file_name in file_names]
 
    # Email configuration
    sender_email = "your_email@example.com"
    receiver_email = "test@xyz.com"
    subject = "Files Attached"
    body = "Please find the attached files."
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"
 
    # Send the email with attachments
    send_email_with_attachments(file_paths, sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_user, smtp_password)