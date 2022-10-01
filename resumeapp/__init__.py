import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


###########################
#### BLUEPRINT CONFIGS #######
#########################

# Import these at the top if you want
# We've imported them here for easy reference
from resumeapp.core.views import core
from resumeapp.resume.views import resume
from resumeapp.error_pages.handlers import error_pages

# Register the apps
app.register_blueprint(resume)
app.register_blueprint(core)
app.register_blueprint(error_pages)
