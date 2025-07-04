from msal import ConfidentialClientApplication

def get_access_token(config):
    app = ConfidentialClientApplication(
        client_id=config['client_id'],
        client_credential=config['client_secret'],
        authority=f"https://login.microsoftonline.com/{config['tenant_id']}"
    )
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    if "access_token" in result:
        return result['access_token']
    raise Exception("Could not acquire token")
