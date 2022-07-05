import sys, os

INTERP = os.path.join(os.environ['HOME'], 'millennialinvesting.runningdigitally.com', 'venv', 'bin', 'python3')


if os.environ['HOME'] != '/home/dh_hkej5d':
    from dotenv import load_dotenv 
    load_dotenv()
    if (os.environ.get('INTERP')):
        INTERP = os.environ.get('INTERP')

if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flask import Flask
application = Flask(__name__)

sys.path.append('app')
from app import app as application



from app import app