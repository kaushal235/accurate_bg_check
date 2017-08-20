import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import requests
from exception import ValidationException
from requests.auth import HTTPBasicAuth


class BgCheck(object):
    base_url = 'https://api.accuratebackground.com/v3/'
    client_id = None
    client_sec = None

    def __init__(self, client_id, client_sec):
        if not (client_id or client_sec):
            raise Exception('CLIENT KEY/CLIENT KEY SECRETE required')

        self.client_id = client_id
        self.client_sec = client_sec

    def get_url(self, resource, pk=None):
        if pk:
            return '{0}{1}/{2}'.format(self.base_url, resource, pk)
        else:
            return '{0}{1}'.format(self.base_url, resource)

    def parse_response(self, response, **kwargs):
        response = json.loads(response.text)
        if kwargs.get('log', True):
            print("#" * 50)
            print("response data for {0}".format(kwargs.get('resource')))
            print(response)

        if 'errors' in response:
            raise ValidationException(json.dumps(response), response['errors'])

        return response

    def send_get_request(self, url, **kwargs):
        response = requests.get(url, auth=HTTPBasicAuth(self.client_id, self.client_sec))
        return self.parse_response(response, **kwargs)

    def send_post_request(self, url, payload, headers=None, **kwargs):
        if not headers:
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            data = urlencode(payload)
        else:
            data = json.dumps(payload)

        if kwargs.get('log', True):
            print("request data")
            print(data)

        response = requests.post(url, data=data, headers=headers,
                                 auth=HTTPBasicAuth(self.client_id, self.client_sec))
        return self.parse_response(response, **kwargs)
