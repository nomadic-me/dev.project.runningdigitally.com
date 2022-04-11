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


#Adding import yfinance as 
import yfinance as yf

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
    df1 = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })
    fig1 = px.bar(df1, x='Fruit', y='Amount', color='City', barmode='group')
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('graph1.html', graphJSON=graphJSON1, title='Graph1 ')
        
    
    
#Adding Plotly Graph with Callback

@app.route('/Graph2')
def graph2():
    return render_template('graph2.html')#,  graphJSON=gm())


def gm(country='United Kingdom'):
    df = pd.DataFrame(px.data.gapminder())
    fig = px.line(df[df['country']==country], x="year", y="gdpPercap", title=country)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
    

    
@app.route('/callback2/<endpoint>', methods=['POST', 'GET'])
def cb2(endpoint):   
    if endpoint == "getStock":
        return gm(request.args.get('data'),request.args.get('period'),request.args.get('interval'))
    elif endpoint == "getInfo":
        stock = request.args.get('data')
        st = yf.Ticker(stock)
        return json.dumps(st.info)
    else:
        return "Bad endpoint", 400
    

# Return the JSON data for the Plotly graph
def gm(stock,period, interval):
    st = yf.Ticker(stock)
  
    # Create a line graph
    df_stock = st.history(period=(period), interval=interval)
    df_stock=  df_stock.reset_index()
    df_stock.columns = ['Date-Time']+list(df_stock.columns[1:])
    max = (df_stock['Open'].max())
    min = (df_stock['Open'].min())
    range = max - min
    margin = range * 0.05
    max = max + margin
    min = min - margin
    fig_stock = px.area(df_stock, x='Date-Time', y="Open",
        hover_data=("Open","Close","Volume"), 
        range_y=(min,max), template="seaborn" )

    # Create a JSON representation of the graph
    graphJSON_stock = json.dumps(fig_stock, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON_stock

@app.route('/Stock')
def stock():
    return render_template('stock.html')#,  graphJSON=gm())