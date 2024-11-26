import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import email
import email.mime.application
import time
 
#plain text version
 
text = "This is the plain text version."
MAIL_DATE = time.strftime("%B %d, %Y")
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
print(sys.argv[1])
SRC_FL_NAME=sys.argv[1].split('|')[0]
DEST_GRP=sys.argv[1].split('|')[1]
print(SRC_FL_NAME)
print(DEST_GRP)

# Arguments passed
print("\nName of Python script:", sys.argv[0])
#html body