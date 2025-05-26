import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/create"
OPERATION = requests.post

def _tested_request(input_json):
    return OPERATION(f"{BASE_URL}{ENDPOINT}", json=input_json)

test_cases = [
    (None, 200, {'idMatch': 1}),
    ({"id":900, "turn":"X","board":"_________"}, 200, {'idMatch': 900}),
    ({"turn":"O"}, 200, {'idMatch': 901}),
    ({"id":900}, 400, {'detail': 'Match ID already exists.'}),
    ({"turn":"a"}, 422, {'detail': [{'ctx': {'pattern': '^(X|O)$'},
             'input': 'a',
             'loc': ['body', 'turn'],
             'msg': "String should match pattern '^(X|O)$'",
             'type': 'string_pattern_mismatch'}]}),
    ({"board":"_"}, 422, {'detail': [{'ctx': {'pattern': '^[XO_]{9}$'},
             'input': '_',
             'loc': ['body', 'board'],
             'msg': "String should match pattern '^[XO_]{9}$'",
             'type': 'string_pattern_mismatch'}]}),
    
]

test_ids = [
    "none_body",
    "complete_good_body",
    "only_turn",
    "repeated_id",
    "bad_turn",
    "bad_board",
]

@pytest.mark.parametrize(
    "input_json, expected_status, expected_json",
    test_cases,
    ids=test_ids
)
def test_get_status(input_json, expected_status, expected_json):
    response = _tested_request(input_json=input_json)
    assert response.status_code == expected_status
    assert response.json() == expected_json
