from flask import render_template,request, Blueprint, url_for

core = Blueprint('core',__name__)

@core.route('/about')
def info():
    return render_template('info.html')
