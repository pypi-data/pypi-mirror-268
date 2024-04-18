import os

from metabase.exception import ErrorCodes, MetabaseException
from metabase.service.http_service import HttpService


class MetabaseService(HttpService):
    params = dict()

    def __init__(self, api_url=None, api_key=None):
        self.api_key = os.environ.get('METABASE_API_KEY', api_key)
        if self.api_key is None:
            raise ValueError(ErrorCodes.API_KEY_ERROR)
        self.api_url = os.environ.get('METABASE_API_URL', api_url)
        if self.api_url is None:
            raise ValueError(ErrorCodes.API_URL_ERROR)
        super().__init__(self.api_url)
        self.headers = {
            'x-api-key': self.api_key,
            'content-type': 'application/json',
            'accept': 'application/json'
        }

    def get_dashboards(self):
        return self.connect('GET', f'/api/dashboard/', headers=self.headers)

    def get_dashboard(self, dashboard_id: int = 0):
        if dashboard_id is 0:
            raise MetabaseException(ErrorCodes.INVALID_ATTRIBUTE)
        return self.connect('GET', f'/api/dashboard/{dashboard_id}', headers=self.headers)

    def get_collections(self):
        return self.connect('GET', f'/api/collection/', headers=self.headers)

    def get_collection(self, collection_id: int = 0):
        if collection_id is 0:
            raise MetabaseException(ErrorCodes.INVALID_ATTRIBUTE)
        return self.connect('GET', f'/api/collection/{collection_id}', headers=self.headers)

    def get_collection_items(self, collection_id: int = 0):
        if collection_id is 0:
            raise MetabaseException(ErrorCodes.INVALID_ATTRIBUTE)
        return self.connect('GET', f'/api/collection/{collection_id}/items', headers=self.headers)

    def get_cards(self):
        return self.connect('GET', f'/api/card/', headers=self.headers)
