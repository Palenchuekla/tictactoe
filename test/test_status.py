import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/status"


def tested_request(match_id):
    params = {"matchId": match_id} if match_id is not None else None
    return requests.get(f"{BASE_URL}{ENDPOINT}", params=params)

# Custom test case names (for verbosity)
test_cases = [
    (1, 200, {'board': '___X_____', 'id': 1, 'turn': 'O', 'winner': None}),
    (99, 404, {'detail': 'Match not found'}),
    (None, 422, {'detail': [{'input': None,
                             'loc': ['query', 'matchId'],
                             'msg': 'Field required',
                             'type': 'missing'}]}),
]

test_ids = [
    "existing_match",
    "non_existing_match",
    "missing_matchId",
]

@pytest.mark.parametrize(
    "match_id, expected_status, expected_json",
    test_cases,
    ids=test_ids
)
def test_get_status(match_id, expected_status, expected_json):
    response = tested_request(match_id)

    assert response.status_code == expected_status
    assert response.json() == expected_json
