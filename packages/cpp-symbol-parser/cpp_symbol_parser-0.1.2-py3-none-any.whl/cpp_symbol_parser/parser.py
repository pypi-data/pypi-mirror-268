from pathlib import Path

from lark import Lark, Token
from lark.visitors import Transformer, Interpreter

from .transform import SourceNameTransform, SubstitutionTransform, AstTransform
from .transform import create_transforms

class Parser:
    def __init__(self):
        self.parser = Lark(open(Path(__file__).parent / 'grammar.lark').read())
        self.transforms = create_transforms()

    def parse(self, symbol):
        tree = self.parser.parse(symbol)

        for t in self.transforms:
            t.transform(tree)

        return tree.children[0]
