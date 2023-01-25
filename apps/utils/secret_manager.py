import json

from google.cloud import secretmanager

SECRET_PROJECT_ID = "406548712110"
SECRET_SECRET_ID = "roomer-api-secrets"
SECRET_VERSION_ID = "latest"


class SecretManagerClient:
    def __init__(self):
        self.client = secretmanager.SecretManagerServiceClient()
        self.project_id = SECRET_PROJECT_ID
        self.secret_id = SECRET_SECRET_ID
        self.version_id = SECRET_VERSION_ID

    def get_secret_data(self, secret_id=SECRET_SECRET_ID):
        secret_detail = self._generate_secret_manager_url(secret_id)
        response = self.client.access_secret_version(request={"name": secret_detail})
        data = response.payload.data.decode("UTF-8")
        return json.loads(data)

    def _generate_secret_manager_url(self, secret_id):
        secret_detail = f"projects/{self.project_id}/secrets/{secret_id}/versions/{self.version_id}"
        return secret_detail
