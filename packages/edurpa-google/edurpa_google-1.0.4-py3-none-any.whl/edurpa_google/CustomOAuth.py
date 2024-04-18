import base64
import pickle
import google.oauth2.credentials
import io
import json
import os.path

VAULT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../devdata/vault.json'))

class CustomOAuth():
    def __init__(self):
        pass

    def _create_credentials(self, token_file_path):
        credentials = None
        with io.open(token_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            credentials = google.oauth2.credentials.Credentials(
                data['access_token'],
                refresh_token=data['refresh_token'],
                token_uri=data['token_uri'],
                client_id=data['client_id'],
                client_secret=data['client_secret'],
                scopes=data['scopes']
            )
        
        return credentials
    
    def _encode_oauth_token(self, credentials):
        oauth_token = base64.b64encode(pickle.dumps(credentials)).decode('utf-8')
        return oauth_token
    
    def _write_oauth_token(self, oauth_token):
        with io.open(VAULT_PATH, "w+", encoding="utf-8") as vault_file:
            vault = dict()
            vault['google'] = dict(oauth_token=oauth_token)
            json.dump(vault, vault_file)

    def set_up_oauth_token_file(self, token_file_path='../devdata/token.json'):
        credentials = self._create_credentials(token_file_path)
        oauth_token = self._encode_oauth_token(credentials)
        self._write_oauth_token(oauth_token)
        