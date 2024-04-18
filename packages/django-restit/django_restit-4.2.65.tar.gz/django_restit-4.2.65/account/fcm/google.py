import json
import requests
import time
from jwt import JWT, jwk_from_dict
from datetime import datetime, timedelta


def oauthLogin(service_account_info):
    # Token endpoint
    token_uri = service_account_info["token_uri"]

    # The current time and expiration time for the assertion
    issued_at_time = datetime.utcnow()
    expiration_time = issued_at_time + timedelta(minutes=60)

    # JWT Header
    jwt_header = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": service_account_info["private_key_id"]
    }

    # JWT Payload
    jwt_payload = {
        "iss": service_account_info["client_email"],
        "sub": service_account_info["client_email"],
        "aud": token_uri,
        "iat": int(issued_at_time.timestamp()),
        "exp": int(expiration_time.timestamp()),
        "scope": "https://www.googleapis.com/auth/firebase.messaging"
    }

    # Create a JWT
    jwt_instance = JWT()
    private_key = jwk_from_dict({"k": service_account_info["private_key"], "kty": "RSA"})
    assertion = jwt_instance.encode(jwt_header, jwt_payload, private_key)

    # Exchange the JWT for an access token
    response = requests.post(token_uri, data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion
    })

    response_data = response.json()

    access_token = response_data.get("access_token")
    expires_in = response_data.get("expires_in")  # Seconds until the token expires

    # You can now use this access_token to authenticate requests to Google APIs.
    # Remember to refresh the token using a similar process once it's close to expiration.

    print("Access Token:", access_token)
    print("Expires In:", expires_in)
