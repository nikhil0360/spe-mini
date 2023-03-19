import math
import pytest
from calculator import app
import calculator

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_sqrt():
    assert math.isclose(calculator.sqrt(4), 2.0)
    assert math.isclose(calculator.sqrt(0), 0.0)
    assert math.isclose(calculator.sqrt(2), 1.4142135623730951)

def test_fact():
    assert calculator.fact(0) == 1
    assert calculator.fact(1) == 1
    assert calculator.fact(5) == 120

def test_ln():
    assert math.isclose(calculator.ln(1), 0.0)
    assert math.isclose(calculator.ln(2.718281828459045), 1.0)
    assert math.isclose(calculator.ln(10), 2.302585092994046)

def test_power():
    assert math.isclose(calculator.power(2, 3), 8.0)
    assert math.isclose(calculator.power(2, -3), 0.125)
    assert math.isclose(calculator.power(0, 0), 1.0)

