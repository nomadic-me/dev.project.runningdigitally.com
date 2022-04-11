import sys, os
from dotenv import load_dotenv 
load_dotenv()

INTERP = os.path.join(os.environ['HOME'], 'dev.project.runningdigitally.com', 'venv2', 'bin', 'python3')
# Uncomment the below line and replace it with the output of your "which python" output
# INTERP = "/Users/user/opt/anaconda3/envs/dev.project.runningdigitally.com/bin/python"
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flask import Flask
application = Flask(__name__)

###### commenting this section to now load 'app'
#@application.route('/')
#def index():
#    return 'Hello from Passenger (and Fintech Group 11), - Something awesome is brewing! Standby for more updates!'


sys.path.append('app')
from app import app as application



from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}