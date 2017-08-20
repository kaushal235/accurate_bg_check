class ListMixin(object):
    def list(self, **kwargs):
        url = self.client.get_url(self.resource)
        response = self.client.send_get_request(url, **kwargs)
        return response


class GetMixin(object):
    def get(self, pk=None, **kwargs):
        url = self.client.get_url(self.resource, pk)
        response = self.client.send_get_request(url, **kwargs)
        return response


class CreateMixin(object):
    def create(self, payload, **kwargs):
        url = self.client.get_url(self.resource)
        kwargs.update({'resource': self.resource})
        headers = {'content-type': 'application/json'}
        return self.client.send_post_request(url, payload, headers=headers, **kwargs)


class BaseCrud(ListMixin, GetMixin, CreateMixin):
    pass
