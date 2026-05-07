import pytest
from pact import Verifier
import os

def test_verify_pact_against_provider():
    # 1. Path to the contract file you just downloaded/generated
    # Ensure this filename matches exactly what you downloaded
    pact_file = 'userapp-userservice.json' 
    
    # 2. Setup the Verifier
    verifier = Verifier(provider='UserService', provider_base_url='http://localhost:5001')

    # 3. Verify the contract
    # This will spin up a tool that calls your Flask app and compares it to the JSON
    output, logs = verifier.verify_pacts(pact_file)
    
    assert output == 0  # In Pact, an exit code of 0 means success!