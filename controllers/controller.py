from app import app
from src.calculator import *

@app.route('/')
def index():
    return 'Hello calculator'

# @app.route('/calculator/<num_1>/<num_2>')
# add(num_1, num_2)


