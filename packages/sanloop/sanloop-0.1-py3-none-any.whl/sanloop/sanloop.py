import requests

def send_api_request(username, password, api_key, python_code):
    url = "http://127.0.0.1:5000/apiCall"  # Update the URL as needed

    data = {
        "username": username,
        "password": password,
        "apiKey": api_key,
        "pythonCode": python_code 
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error: {response.status_code} - {response.text}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


