import requests

def test_credentials(username, password, target_url):
    try:
        # Send a request to test credentials
        response = requests.get(target_url, auth=(username, password))
        if response.status_code == 200:
            print("Credentials are valid.")
        else:
            print("Invalid credentials.")
    except requests.exceptions.RequestException as e:
        print(f"Error during credential testing: {e}")

# Example usage
username = "testuser"
password = "testpassword"
target_url = "https://azure-target-url.com"
test_credentials(username, password, target_url)
