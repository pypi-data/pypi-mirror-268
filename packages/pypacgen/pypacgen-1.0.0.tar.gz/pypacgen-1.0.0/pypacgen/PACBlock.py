from typing import List

from PACFunction import *
from PACReturn import PACReturn


class PACBlock(PACObject):
    ops: List[PACFunction]
    ret: PACReturn
    docs: str
    template_filename = "pac-block.template"

    def __init__(self, ret: PACReturn, ops: List[PACFunction], docs: str = "", join_or=True):
        self.ops = ops
        self.ret = ret
        self.docs = docs
        self.join_or = join_or
        super(PACBlock, self).__init__()

    def render(self, ):
        return self.template.render(
            block_operator=(" || " if self.join_or else " && ").join(op.render() for op in self.ops),
            block_return=self.ret.render(),
            block_documentatio=self.docs
        )
