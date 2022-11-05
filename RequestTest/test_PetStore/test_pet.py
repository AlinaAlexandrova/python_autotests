import pytest
import requests

url = "https://petstore.swagger.io/v2/pet/111"

def test_status_code():
    response = requests.get(url)
    assert response.status_code == 200
    
def test_name():
    response = requests.get(url)
    response = response.json()
    assert response ["name"] == "Petr"
