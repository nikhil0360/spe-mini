import math
from flask import Flask, request, render_template
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='demo.log', 
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    )

def sqrt(num1):
    return math.sqrt(float(num1))

def fact(num1):
    return math.factorial(int(num1))

def ln(num1):
    return math.log(float(num1))

def power(num1, num2):
    return math.pow(float(num1), float(num2))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate():
    operation = request.form['operation']
    num1 = request.form['num1']
    result = None
    query = None

    app.logger.info(f'Processing {operation} request')
    if operation == 'sqrt':
        result = sqrt(num1)
    elif operation == 'fact':
        result = fact(num1)
    elif operation == 'ln':
        result = ln(num1)
    elif operation == 'power':
        num2 = request.form['num2']
        result = power(num1, num2)

    query = f'{operation}({num1}'

    if operation == 'power':
        query += f', {num2})'
    else:
        query += ')'

    return render_template('index.html', result=result, query=query)

if __name__ == '__main__':
    app.run(debug=True)