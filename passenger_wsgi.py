import sys, os
INTERP = os.path.join(os.environ['HOME'], 'dev.project.runningdigitally.com', 'venv2', 'bin', 'python3')
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