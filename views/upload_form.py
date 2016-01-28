from flask import Blueprint, render_template

upload_form = Blueprint('upload_form', __name__, subdomain='my')

@upload_form.route('/')
def index():
    return render_template('upload_form.html')
