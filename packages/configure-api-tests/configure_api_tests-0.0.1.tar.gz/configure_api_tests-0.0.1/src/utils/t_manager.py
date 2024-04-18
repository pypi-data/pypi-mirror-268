# Import necessary libraries
from dotenv import load_dotenv
import requests
import logging
import os

logging.basicConfig(level=logging.INFO)

load_dotenv()

production_url = os.environ.get('PRODUCTION_URL')
testing_url = os.environ.get('TESTING_URL')

activation_codes = {
    production_url: 'apitesting_production',
    testing_url: 'apitesting_test'
}

auth_tokens = {}

def authenticate_api(url, data):
    """
    Calls the API with the given URL and data payload to authenticate.

    :param url: The URL of the authentication API endpoint.
    :param data: The data payload to send with the request.
    :return: The bearer token obtained from the API call.
    """
    try:
        # Log the request details
        logging.info(f"Making authentication request to {url} with payload: {data}")
        
        # Make the API call
        response = requests.post(url, json=data)
        response.raise_for_status()
        auth_token = response.json().get('auth_token')  # Extract the auth_token from the response
        
        # Log the response details
        logging.info(f"Authentication response from {url}: {response.content}")
        
        return auth_token
    except requests.RequestException as e:
        # Handle any HTTP request errors
        logging.error(f"Error occurred during API call to {url}: {e}")
        return None

def prepare_auth_payload(activation_code):
    return {
        "activation_code": activation_code,
        "device": {
            "app_version": "1.0",
            "device_id": "some-randmom-string",
            "device_type": "TEST",
            "os_version": "0.0.0",
        }
    }

def authenticate_and_store_tokens():
    """
    Function to authenticate and store tokens.
    """
    global auth_tokens  # Access the global auth_tokens dictionary

    # Get authentication token for each environment
    for base_url, activation_code in activation_codes.items():
        url = f"{base_url}/app/authenticate"  # Construct the full URL with "/app/authenticate"
        data = prepare_auth_payload(activation_code)  # Get data with the correct activation code
        token = authenticate_api(url, data)
        if token:
            logging.info(f"Authentication successful for {url}. Bearer token: {token}")
            auth_tokens[base_url] = token
        else:
            logging.error(f"Failed to authenticate for {url}.")
    
    return auth_tokens

def retrieve_token(environment):
    """
    Function to retrieve the token based on the specified environment.

    :param environment: The environment for which the token is requested, either 'production' or 'testing'.
    :return: The authentication token for the specified environment.
    """
    global auth_tokens
    
    if environment == 'production':
        return auth_tokens.get(production_url)
    elif environment == 'testing':
        return auth_tokens.get(testing_url)
    else:
        logging.error("Invalid environment specified.")
        return None

# Call authenticate_and_store_tokens() to retrieve tokens
authenticate_and_store_tokens()

# Get authentication token for production environment
production_token = retrieve_token('production')

# Get authentication token for testing environment
testing_token = retrieve_token('testing')

# Log the tokens
logging.info(f"\nProduction Bearer Token: {production_token}\n")
logging.info(f"\nTesting Bearer Token: {testing_token}\n")
