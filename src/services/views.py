"""
Services endpoints
"""
from flask import abort, Blueprint

blueprint = Blueprint('services', __name__)

@blueprint.route('/health')
def health():
    return "All is well :)"

@blueprint.route('/401')
def unauthorized():
    abort(401)

@blueprint.route('/403')
def forbidden():
    abort(403)

@blueprint.route('/404')
def not_found():
    abort(404)

@blueprint.route('/500')
def internal_error():
    abort(500)
