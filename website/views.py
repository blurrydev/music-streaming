from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', text="Mitthu Raani Gili Gili Paani", boolean=False)