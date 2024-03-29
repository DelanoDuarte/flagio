
from flask import jsonify


def test_index_api(client):
    result = client.get('/api')
    expected = {"data":"Api Running"}
    assert result.get_json() == expected

def test_empty_flags_get(client):
    result = client.get('/api/flags')
    assert result.status_code == 200

def test_insert_flag(client):
    result = client.post('/api/flags', json={
        "name": "Feature Flag",
        "description": "Something"
    })
    assert result.status_code == 200
