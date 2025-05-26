import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/move"
OPERATION = requests.post

def _tested_request(input_json):
    return OPERATION(f"{BASE_URL}{ENDPOINT}", json=input_json)

test_cases = [
    ({"matchId":2, "playerId":"X", "square":{"x":3, "y":2}}, 200, {'match': {'board': 'O____X_X_', 'id': 2, 'turn': 'O', 'winner': None},
 'posted_move': {'id': 22, 'matchId': 2, 'playerId': 'X', 'x': 3, 'y': 2}}),
    ({"matchId":5, "playerId":"X", "square":{"x":3, "y":2}}, 400, {'detail': 'Match ID (5) is over. Player ID (X) won.'}),
    ({"matchId":2, "playerId":"X", "square":{"x":1, "y":2}}, 400, {'detail': 'Move player ID (X) does not match the turn (O).'}),
    ({"matchId":2, "playerId":"O", "square":{"x":3, "y":2}}, 400 , {'detail': 'Square (3,2) is occupied. Current board: (O____X_X_)'})
]

test_ids = [
    "allowed_move",
    "finished_match_move",
    "not_your_turn",
    "occupied_square"
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
