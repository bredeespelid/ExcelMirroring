import requests
import pandas as pd
from msal import ConfidentialClientApplication
from ..Utilities.Helper import get_access_token
from ..Models.FileMetadata import FileMetadata

class GraphAPIClient:
    def __init__(self, config):
        self.config = config
        self.token = get_access_token(config)

    def get_recent_files(self):
        endpoint = f"https://graph.microsoft.com/v1.0/sites/{self.config['site_id']}/drives/{self.config['drive_id']}/root:{self.config['folder_path']}:/children"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        files = []
        for item in response.json().get('value', []):
            if item['name'].endswith('.xlsx'):
                files.append(FileMetadata(item['id'], item['name'], item['lastModifiedDateTime']))
        return files

    def download_excel_as_dataframe(self, file):
        endpoint = f"https://graph.microsoft.com/v1.0/sites/{self.config['site_id']}/drives/{self.config['drive_id']}/items/{file.id}/content"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        excel_bytes = response.content
        df = pd.read_excel(excel_bytes, engine='openpyxl')
        return df
