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

    '''
    # Create the plain-text and HTML version of your message
    text = """\
    Scoring Report

    Job Description:
    """ +  description + """\

    Experience Required (years):""" + str(experience) + """\
    Primary skill: """ + primarySkill + """\
    Secondary skill: """ + secondarySkill + """\
    File Uploaded: """ + fileName + """\
    Skills Matched: """ + str(skillsFound)  + """\
    Skills Not Matched: """ + str(skillsNotFound)  + """\
    Experience of candidate (years): """ + str(experienceInYears) + """\
    Points Achieved: """ + str(pointsAchieved) + """\
    Points Lost: """ + str(pointsLost) + """\

    Scoring Methodology:
    Primary Skill - 50 points
    Secondary Skill - 25 points
    Additional Skills - 5 points * 10 (maximum)
    Total Score = 100

    Scoring: """ + str(matchPercent) + " % "
    '''
    #pdf = pdfkit.from_string(htmlPage, False)
    #response = make_response(pdf)
    #response.headers["Content-Type"] = "application/pdf"
    #response.headers["Content-Disposition"] = "inline; filename=output.pdf"

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
