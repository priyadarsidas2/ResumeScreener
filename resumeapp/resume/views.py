import os
from flask import Flask, flash, request, redirect, url_for
from resumeapp.resume.forms import ResumeForm
from flask import Blueprint, render_template
from resumeapp.resume.readpdf import extractTextFromPDF
from resumeapp.resume.scoring import scoringAndExperienceCheck, findSubtextForExperienceSearch, cleanExperienceRange
from resumeapp.resume.email import sendEmail
from resumeapp.resume.cleanoutput import deleteOutputFiles

resume = Blueprint('resume',__name__)

UPLOAD_FOLDER = 'F:\Python\1. Flask\1. Resume Screening\1. Final'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#@resume.route('/')
#def index():
#    form = ResumeForm()
#    return render_template('index.html', form = form)

@resume.route('/', methods=['GET','POST'])
def create_post():
    form = ResumeForm()

    if form.validate_on_submit():
        description = form.description.data
        experience = form.experience.data
        primarySkill = form.primarySkill.data
        secondarySkill = form.secondarySkill.data
        emailid = form.emailid.data
        fileName = form.fileName.data
        fileName.save(fileName.filename)
        extractedText = extractTextFromPDF(fileName.filename)
        matchPercent, skillsFound, skillsNotFound, experienceInYears, pointsAchieved, pointsLost = scoringAndExperienceCheck(
                                                                            primarySkill, secondarySkill, extractedText)
        experienceInYears = round(experienceInYears, 2)

        #fileName.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        htmlPage = render_template('output.html',form=form,
                                description = description,
                                experience = experience,
                                primarySkill = primarySkill,
                                secondarySkill = secondarySkill,
                                fileName = fileName.filename,
                                matchPercent = matchPercent,
                                skillsFound = skillsFound,
                                skillsNotFound = skillsNotFound,
                                experienceInYears = experienceInYears,
                                pointsAchieved = pointsAchieved,
                                pointsLost = pointsLost,
                                emailid = emailid
                                )
        sendEmail(emailid, fileName.filename, htmlPage)
        #deleteOutputFiles()
        return htmlPage
    return render_template('index.html',form=form)
