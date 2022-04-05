from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello from Passenger (and Fintech Group 11) via 'app folder', - Something awesome is brewing! Standby for more updates!"