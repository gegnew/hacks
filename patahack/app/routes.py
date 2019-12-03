##
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app.forms import InputForm
#from patahack import Patahack
#from bs4 import BeautifulSoup
##

@app.route('/')
@app.route('/index')
def index():
    return(render_template('index.html', title='Home'))

@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    return(render_template('input.html', title='Cop?', form=form))
    if form.validate_on_submit():
        data = form['userinput']
        return(redirect(url_for('input')))
    return(render_template('input.html', title='What u tryna cop?', form=form))

@app.route('/my-form')
def my_form():
    return(render_template('my-form.html'))
@app.route('/my-form', methods=['POST'])
def get_input():
    text = request.form['userinput']
    processed_text = text.upper()
    return(processed_text)

# TODO: get input from form, somehow

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return(redirect(url_for('index')))
    return(render_template('login.html', title='Sign In', form=form))

