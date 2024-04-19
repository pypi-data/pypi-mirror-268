import os
import sys

from jinja2 import Environment, FileSystemLoader, Template


class PACObject:
    template_filename: str
    template: Template

    def __init__(self):
        self.environment = Environment(loader=FileSystemLoader(os.path.join(
            os.path.dirname(sys.modules[PACObject.__module__].__file__), 'templates/'))
        )
        self.template = self.environment.get_template(self.template_filename)

    def validate(self):
        pass

    def render(self, **kwargs) -> str:
        raise NotImplemented
