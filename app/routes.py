from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User
from flask import request
from datetime import datetime

from app.forms import RegistrationForm
from app.forms import LoginForm
from app.forms import EditProfileForm
from app.forms import EmptyForm
from app.forms import PostForm
from app.models import Post
from app.forms import ResetPasswordRequestForm
from app.email import send_password_reset_email
from app.forms import ResetPasswordForm

#Adding simple Plotly Graph
import pandas as pd
import json
import plotly
import plotly.express as px


@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

#Adding simple Plotly Graph
@app.route('/Graph1')
def graph1():
    df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('graph.html', graphJSON=graphJSON1, title='Graph')
        
    
    
#Adding Plotly Graph with Callback





@app.route('/Graph2')
def graph2():
    return render_template('graph2.html')#,  graphJSON=gm())


def gm(country='United Kingdom'):
    df = pd.DataFrame(px.data.gapminder())
    fig = px.line(df[df['country']==country], x="year", y="gdpPercap", title=country)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
    
    