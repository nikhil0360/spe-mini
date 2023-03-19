import math
from flask import Flask, request, render_template

app = Flask(__name__)

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


# def test_calculate_sqrt(client):
#     response = client.post('/', data={'operation': 'sqrt', 'num1': '4'})
#     assert response.status_code == 200
#     print(response.data.decode('utf-8'))
#     assert math.isclose(float(response.data.decode('utf-8')), 2.0)

# def test_calculate_fact(client):
#     response = client.post('/', data={'operation': 'fact', 'num1': '5'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == '120'

# def test_calculate_ln(client):
#     response = client.post('/', data={'operation': 'ln', 'num1': '2.718'})
#     assert response.status_code == 200
#     assert math.isclose(float(response.data.decode('utf-8')), 1.0)

# def test_calculate_power(client):
#     response = client.post('/', data={'operation': 'power', 'num1': '2', 'num2': '3'})
#     assert response.status_code == 200
#     assert math.isclose(float(response.data.decode('utf-8')), 8.0)