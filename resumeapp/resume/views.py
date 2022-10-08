import os
from flask import Flask, flash, request, redirect, url_for
from resumeapp.resume.forms import ResumeForm
from flask import Blueprint, render_template
from resumeapp.resume.readpdf import extractTextFromPDF
from resumeapp.resume.scoringAndExperience import scoringAndExperienceCheck
from resumeapp.resume.email import sendEmail

resume = Blueprint('resume',__name__)

UPLOAD_FOLDER = 'F:\Python\1. Flask\1. Resume Screening\1. Final'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@resume.route('/', methods=['GET','POST'])
def create_post():
    form = ResumeForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        #experience = form.experience.data
        #primarySkill = form.primarySkill.data
        #secondarySkill = form.secondarySkill.data
        emailid = form.emailid.data
        fileName = form.fileName.data
        fileName.save(fileName.filename)
        extractedText = extractTextFromPDF(fileName.filename)
        (relevantSkills,skillsMatched, skillsNotFound, pointsFromProfile, primarySkillsInRelevantSkills,
            secondarySkillsInRelevantSkills, pointsFromPrimarySkills, pointsFromSecondarySkills, matchPercent) = scoringAndExperienceCheck(
                                                                            title, extractedText, description)
        #experienceInYears = round(experienceInYears, 2)
        profileStatus = "Match" if pointsFromProfile == 20 else "Mismatch"
        #fileName.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        htmlPage = render_template('output.html',form=form,
                                    title = title,
                                    description = description,
                                    fileName = fileName.filename,
                                    relevantSkills = ", ".join(relevantSkills),
                                    primarySkillsInRelevantSkills = ", ".join(primarySkillsInRelevantSkills),
                                    secondarySkillsInRelevantSkills = ", ".join(secondarySkillsInRelevantSkills),
                                    skillsMatched = ", ".join(skillsMatched),
                                    skillsNotFound = ", ".join(skillsNotFound),
                                    profileStatus = profileStatus,
                                    pointsFromProfile = pointsFromProfile,
                                    pointsFromPrimarySkills = pointsFromPrimarySkills,
                                    pointsFromSecondarySkills = pointsFromSecondarySkills,
                                    matchPercent = matchPercent,
                                    emailid = emailid
                                )
        sendEmail(emailid, fileName.filename, htmlPage)
        #deleteOutputFiles()
        return htmlPage
    return render_template('index.html',form=form)
