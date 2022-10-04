import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import pdfkit
import email

def sendEmail(emailid, fileName, htmlPage):
    #emailid, fileName, description, experience, primarySkill, secondarySkill, skillsFound,
    #                skillsNotFound, experienceInYears, pointsAchieved, pointsLost, matchPercent,
    sender_email = "priyadarsidas7@gmail.com"
    receiver_email = emailid
    password = 'gzhjwebpkwkewzyd'

    candidateName = fileName.split('.')[0]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Scoring Report - " + candidateName
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "Hi, the report is as follows:"

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(htmlPage, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string())
    return
