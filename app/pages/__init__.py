from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename


page_bp = Blueprint('pages', __name__, template_folder='templates')


@page_bp.route('/', defaults={'page': 'index'})
@page_bp.route('/<path:page>')
def show(page):
    page = secure_filename(page)

    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
