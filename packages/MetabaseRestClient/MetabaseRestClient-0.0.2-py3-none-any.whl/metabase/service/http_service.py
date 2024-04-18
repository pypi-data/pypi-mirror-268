import requests

from metabase.exception import MetabaseException
from metabase.serializer import Serializer


class HttpService:
    REST_URL = None

    def __init__(self, REST_URL):
        self.REST_URL = REST_URL

    @staticmethod
    def parse_result(r):
        res = r.text.encode('utf-8')
        if r.status_code != 200:
            raise MetabaseException(res)
        res = Serializer.loads(res)
        return res

    def post_request(self, url, request_body, headers):
        request_body = Serializer.dumps(request_body)
        r = requests.post(url, data=request_body, headers=headers)
        return self.parse_result(r)

    def get_request(self, url, headers):
        r = requests.get(url, headers=headers)
        return self.parse_result(r)

    def connect(self, method, url, request_body={}, headers=None):
        if method == 'GET':
            return self.get_request(self.REST_URL + url, headers)
        return self.post_request(self.REST_URL + url, request_body, headers)
