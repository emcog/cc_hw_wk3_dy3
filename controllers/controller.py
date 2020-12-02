from app import app
from src.calculator import *

@app.route('/')
def index():
    return 'Hello calculator'

@app.route('/add/<num_1>/<num_2>')
def add_url(num_1, num_2):
    return add(num_1, num_2)

@app.route('/subtract/<num_1>/<num_2>')
def subtract_url(num_1, num_2):
    return subtract(num_1, num_2)


@app.route('/multiply/<num_1>/<num_2>')
def multiply_url(num_1, num_2):
    return multiply(num_1, num_2)


@app.route('/divide/<num_1>/<num_2>')
def divide_url(num_1, num_2):
    return divide(num_1, num_2)

