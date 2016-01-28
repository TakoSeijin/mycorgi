from flask import Blueprint, send_from_directory

static = Blueprint('static', __name__, subdomain='static')

@static.after_request
def after(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@static.route('/<path:path_to_static_resource>')
def static_function(path_to_static_resource):
    return send_from_directory('static', path_to_static_resource)

@static.errorhandler(404)
def static_404(error):
    return 'no static resource found', 404
