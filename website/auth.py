from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    pass

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1> Logout </h1>"

@auth.route('/signup')
def signup():
    return render_template("signup.html")