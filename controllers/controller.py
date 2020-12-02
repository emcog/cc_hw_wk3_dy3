from app import app
from src.calculator import *

@app.route('/')
def index():
    return 'Hello calculator'

@app.route('/calc/<num_1>/<num_2>')
def add_url(num_1, num_2):
    return add(num_1, num_2)


