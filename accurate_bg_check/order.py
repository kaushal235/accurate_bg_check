from accurate_bg_check.mixin.crud import BaseCrud


class Order(BaseCrud):
    resource = 'order'
    client = None

    def __init__(self, client=None):
        if not client:
            raise Exception('accurate_bg_check client instance required')
        self.client = client
