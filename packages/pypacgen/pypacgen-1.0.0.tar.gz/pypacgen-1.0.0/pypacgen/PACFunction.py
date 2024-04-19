from PACExceptions import InvalidPACFunctionArgException
from PACObject import PACObject


class PACFunction(PACObject):
    template_filename: str
    host: str
    url: str
    nets: str
    mask: str
    earliest: int | str
    latest: int | str

    def __init__(self,
                 host: str = None,
                 url: str = None,
                 net: str = None,
                 mask: str = None,
                 earliest: int | str = None,
                 latest: int | str = None
                 ):
        self.host = host
        self.url = url
        self.net = net
        self.mask = mask
        self.earliest = earliest
        self.latest = latest
        if not self.validate():
            raise InvalidPACFunctionArgException
        super(PACFunction, self).__init__()

    def validate(self) -> bool:
        return True

    def render(self) -> str:
        return self.template.render(
            host=self.host,
            url=self.url,
            net=self.net,
            mask=self.mask,
            earliest=self.earliest,
            latest=self.latest
        )
