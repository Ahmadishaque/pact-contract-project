import pytest
from pact import Consumer, Provider
import requests

# 1. Define the Pact between the "UserApp" and the "UserService"
pact = Consumer('UserApp').has_pact_with(Provider('UserService'))

@pytest.fixture(scope='session')
def pact_setup():
    # Start the Pact mock server
    pact.start_service()
    yield
    # Stop the service and generate the JSON Pact file
    pact.stop_service()

def test_get_user_contract(pact_setup):
    """Define the expectation for the User Profile API"""
    expected_body = {
        'id': 1,
        'name': 'Ahmad Ishaque'
    }

    # 2. Describe the interaction
    (pact
     .given('User 1 exists')
     .upon_receiving('a request for user 1')
     .with_request('get', '/users/1')
     .will_respond_with(200, body=expected_body))

    # 3. Run the test against the mock server
    with pact:
        # The mock server runs on localhost:1234 by default
        result = requests.get('http://localhost:1234/users/1')
        assert result.status_code == 200
        assert result.json() == expected_body
    
    # After this test finishes, a .json file is created in your project root!