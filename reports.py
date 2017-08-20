class Report(object):
    resource = 'report'
    client = None

    def __init__(self, client=None):
        if not client:
            raise Exception('accurate_bg_check client instance required')
        self.client = client

    def get(self, resource=None):
        """
            resource base url present in order api
        """
        if not resource:
            raise Exception('Base url required in report')

        url = self.client.get_url(resource)
        response = self.client.send_get_request(url)
        return response
