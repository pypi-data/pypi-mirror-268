#!/usr/bin/env python

from PACBlock import *
from PACExceptions import *


class PACFile(PACObject):
    name: str
    version: str
    blocks: List[PACBlock]
    default: PACReturn
    docs: str

    # Declare template file to be used in render.  Required by PACObject
    template_filename = "pac-file.template"

    def __init__(self,
                 file_name: str,
                 file_version: str,
                 blocks: List[PACBlock] = None,
                 default: PACReturn = None,
                 docs: str = None
                 ):
        if file_name.find('.pac') < 0 and file_name != "":
            file_name += ".pac"
        self.name = file_name
        self.version = file_version
        self.blocks = blocks if blocks else []
        self.default = default if default else ""
        self.docs = docs if docs else ""
        super(PACFile, self).__init__()

    def set_default_return(self, default: PACReturn):
        self.default = default

    def add_block(self, block: PACBlock):
        self.blocks.append(block)

    def render(self, compress: bool = False, obfuscate: bool = False):
        if not self.default:
            raise InvalidPACFileException("No default case given. Please add a default and try again!")

        output = self.template.render(
            file_name=self.name,
            file_version=self.version,
            file_body="".join(block.render() for block in self.blocks),
            file_default=self.default.render(),
            file_documentation=self.docs
        )
        if compress:
            output = output.strip()
        if obfuscate:
            output = _obfuscate(output)
        return output


def _obfuscate(code: str):
    return code
