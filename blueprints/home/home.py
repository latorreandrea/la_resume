from flask import Blueprint, render_template, redirect, url_for
# create blueprint
home_bp = Blueprint('home', __name__, template_folder='templates',
                    static_folder='static', static_url_path='/home/static')

@home_bp.route('/')
def home():
    return render_template('home/home.html')