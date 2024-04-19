from PACObject import PACObject


class PACReturn(PACObject):
    path: str
    ip: str
    port: int

    template_filename = "pac-return.template"

    def __init__(self, path: str, ip: str = None, port: int = None):
        self.path = path
        self.ip = ip
        self.port = port
        super(PACReturn, self).__init__()

    def render(self):
        return self.template.render(
            ret_path=self.path,
            ret_ip=self.ip,
            ret_port=self.port
        )
