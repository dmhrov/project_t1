import requests

def test_status_endpoint():
    response = requests.get('http://localhost:5000/api/status')
    assert response.status_code == 200
    data = response.json()
    assert 'status' in data
    assert data['status'] == 'ok'
