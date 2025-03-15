import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000/api"


def test_jwt_auth():
    """
    Test the JWT authentication flow:
    1. Login to get tokens
    2. Use access token to access protected endpoint
    3. Refresh the token
    4. Verify the token
    """
    print("Testing JWT Authentication Flow\n" + "-" * 30)

    # 1. Login to get tokens
    print("\n1. Login to get tokens")
    login_data = {"username": "admin@admin.com", "password": "12345"}

    login_response = requests.post(f"{BASE_URL}/auth/login/", data=login_data)

    if login_response.status_code == 200:
        print("Login successful!")
        tokens = login_response.json()
        access_token = tokens["access"]
        refresh_token = tokens["refresh"]
        print(f"Access Token: {access_token[:20]}...")
        print(f"Refresh Token: {refresh_token[:20]}...")
    else:
        print(f"Login failed: {login_response.status_code}")
        print(login_response.text)
        return

    # 2. Use access token to access protected endpoint
    print("\n2. Accessing protected endpoint (user profile)")
    headers = {"Authorization": f"Bearer {access_token}"}
    profile_response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)

    if profile_response.status_code == 200:
        print("Profile access successful!")
        print(f"User data: {json.dumps(profile_response.json(), indent=2)}")
    else:
        print(f"Profile access failed: {profile_response.status_code}")
        print(profile_response.text)

    # 3. Refresh the token
    print("\n3. Refreshing token")
    refresh_data = {"refresh": refresh_token}
    refresh_response = requests.post(
        f"{BASE_URL}/auth/token/refresh/", data=refresh_data
    )

    if refresh_response.status_code == 200:
        print("Token refresh successful!")
        new_access_token = refresh_response.json()["access"]
        print(f"New Access Token: {new_access_token[:20]}...")
    else:
        print(f"Token refresh failed: {refresh_response.status_code}")
        print(refresh_response.text)

    # 4. Verify the token
    print("\n4. Verifying token")
    verify_data = {"token": new_access_token}
    verify_response = requests.post(f"{BASE_URL}/auth/token/verify/", data=verify_data)

    if verify_response.status_code == 200:
        print("Token verification successful!")
    else:
        print(f"Token verification failed: {verify_response.status_code}")
        print(verify_response.text)


if __name__ == "__main__":
    test_jwt_auth()
