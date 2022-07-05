# dev.project.runningdigitally.com

## Demo Page

Go to this page for live Demonstration: [https://millennialinvesting.runningdigitally.com/](https://millennialinvesting.runningdigitally.com/)

### Screenshots:

![Homepage](images/homepage.png)
![Portfolio Returns Page](images/portfolio-returns-Portfolio1.png)
![Portfolio Individul Stock Page](images/portfolio-individual-stocks-Portfolio1.png)

## Prepare Local Python Environment

### Clone this project and go to the working directory

```bash
git clone git@github.com:nomadic-me/millennialinvesting.runningdigitally.com.git
cd millennialinvesting.runningdigitally.com
```


### Create Conda Enviroment for Project
```bash
conda create -n millennialinvesting.runningdigitally.com python=3.8 anaconda
activate millennialinvesting.runningdigitally.com
```

### Install Packages

```bash
pip install flask
pip install python-dotenv
pip install flask-wtf
pip install flask-mail
pip install pyjwt
pip install flask-bootstrap
pip install dash
pip install pandas
pip install plotly
pip install yfinance
pip install email_validator
pip install alpaca_trade_api
```

### Setup local .env file

First create a .env file via ```vim editor``` or your text editor

```bash
vi .env
```

Here is a sample of the .env file

``` bash
FLASK_APP=passenger_wsgi.py
FLASK_ENV=production
MAIL_SERVER='smtp.yourmailserver.com'
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME='info@yourserver.com'
MAIL_PASSWORD='SMTP Password'
SECRET_KEY='This_should_be_really_hard_to_guess'
SQLALCHEMY_DATABASE_URI='mysql://sql_username:Secure_DB_password@mysql.dev.yourSQLserver.com/dev_project_runningdigitally'
```
