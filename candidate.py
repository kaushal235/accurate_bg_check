from mixin.crud import BaseCrud


class Candidate(BaseCrud):
    resource = 'candidate'
    client = None

    def __init__(self, client=None):
        if not client:
            raise Exception('accurate_bg_check client instance required')
        self.client = client