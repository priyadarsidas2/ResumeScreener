from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired
from flask import render_template,url_for,flash, redirect,request,Blueprint

class ResumeForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = TextAreaField('Job Title', validators=[DataRequired()])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    #experience = IntegerField('Minimum Experience', validators=[DataRequired()])
    #primarySkill = StringField('Primary Skill', validators=[DataRequired()])
    #secondarySkill = StringField('Secondary Skill', validators=[DataRequired()])
    emailid = StringField('Email Id for Report', validators=[DataRequired()])
    fileName = FileField('Resume', validators=[DataRequired()])
    submit = SubmitField('Submit')
