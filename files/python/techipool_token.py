from google.auth.transport import requests
from google.oauth2 import service_account

CREDENTIAL_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
CREDENTIALS_KEY_PATH = "files/serviceaccounts/abdvp.pem"

def get_service_account_token():
  credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_KEY_PATH, scopes=CREDENTIAL_SCOPES)
  credentials.refresh(requests.Request())
  return credentials.token

print(get_service_account_token())