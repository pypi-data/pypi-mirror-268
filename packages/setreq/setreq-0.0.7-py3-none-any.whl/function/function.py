import requests as req
import re

def validate_email(email):
    pattern = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #insert email in pattern part
    if re.fullmatch(pattern, email):
        print("valid")  
        return True
    else:
        print("Invalid")  
        return False


def convert_temperature(temp, to_scale='F'):
    if to_scale.upper() == 'C':
        convert_temp = (temp - 32) * 5.0/9.0
        print(f"{temp}℉ is {convert_temp:.2f}°C")
    elif to_scale.upper() == 'F':
        convert_temp = temp * 9.0/5.0 + 32
        print(f"{temp}°C is {convert_temp:.2f}℉")
    else:
        raise ValueError("Unsupported scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

def download_file(url, computer_filename):
    response = req.get(url)
    response.raise_for_status()
    with open(computer_filename, 'wb') as f:
        f.write(response.content)
def get_options(url):
    """Send an OPTIONS request to the URL."""
    response = req.options(url)
    return response.headers['Allow']

def patch_resource(url, data):
    """Send a PATCH request to update resources at the URL."""
    response = req.patch(url, data=data)
    return response.json()

def download_image(url, path):
    """Download a binary file from the URL and save it to a path."""
    response = req.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)

def get_cookies(url):
    """Send a GET request and return any cookies set by the server."""
    response = req.get(url)
    return response.cookies
