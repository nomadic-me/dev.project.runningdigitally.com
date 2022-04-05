from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Group 11'}
    posts = [{'author': {'username': 'John'},'body': 'Beautiful day in Toronto!'},{'author': {'username': 'Jane'},'body': 'Python Class was so cool!'}]
    return render_template('index.html', title='Home', user=user, posts=posts)



