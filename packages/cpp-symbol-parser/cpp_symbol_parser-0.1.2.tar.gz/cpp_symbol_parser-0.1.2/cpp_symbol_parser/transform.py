from lark import Token, Tree
from lark.visitors import Transformer, Interpreter, Transformer_InPlaceRecursive, v_args

from dataclasses import replace

from .ast import *

class SourceNameTransform(Transformer_InPlaceRecursive):
    def source_name(self, items):
        return ''.join(items)

    def source_name_inner(self, items):
        return ''.join(items)

class SubstitutionTransform(Interpreter):
    def transform(self, tree):
        self._substitutions = []
        return super().visit(tree)

    def _get_substitution(self, id):
        match id:
            case None:
                return self._substitutions[0]
            case Token(type='SEQ_ID'):
                return self._substitutions[1 + int(id, 36)]
            case _:
                assert False # TODO

    def _is_template(self, tree):
        if not isinstance(tree, Tree):
            return False
        if tree.data == 'template':
            return True
        return any(self._is_template(child) for child in tree.children)

    def _substitutable(self, tree):
        match tree.children[0].data:
            case 'builtin_type':
                pass

            case 'substitution':
                tree.children = self._get_substitution(tree.children[0].children[0])

            case 'class_enum_type' if not self._is_template(tree):
                self.visit_children(tree)

            case _:
                self.visit_children(tree)
                self._substitutions.append(tree.children)

    template_prefix = _substitutable
    prefix = _substitutable
    unscoped_template_name = _substitutable
    type = _substitutable

@v_args(inline = True)
class AstTransform(Transformer_InPlaceRecursive):
    def builtin_type(self, token):
        return BuiltinType({
            'v': 'void',
            'w': 'wchar_t',
            'b': 'bool',
            'c': 'char',
            'a': 'signed char',
            'h': 'unsigned char',
            's': 'short',
            't': 'unsigned short',
            'i': 'int',
            'j': 'unsigned int',
            'l': 'long',
            'm': 'unsigned long',
            'x': 'long long',
            'y': 'unsigned long long',
            'n': '__int128',
            'o': 'unsigned __int128',
            'f': 'float',
            'd': 'double',
            'e': 'long double',
            'g': '__float128',
            'z': '...',
        }[token])

    def array_type(self, count, type):
        return Array(type, count)

    def literal(self, type, value):
        return Literal(type, int(value))

    def aggregate_init(self, type, *values):
        return AggregateInit(type, values)

    def template_arg(self, item):
        return [item,]

    def template_args(self, *items):
        args = []
        for l in items:
            args.extend(l)
        return args

    template_parameter_pack = template_args

    def function(self, name, types):
        return_type, *argument_types = (None, *types) if name.template_args is None else types
        if argument_types == [BuiltinType('void')]:
            argument_types = []
        return Function(name, return_type, tuple(argument_types))

    def unqualified_name(self, name):
        assert isinstance(name, Name) == False
        return Name(name)

    def std_scoped_name(self, name):
        return replace(name, parent = Name('std'))

    def prefix(self, *args):
        match args:
            case (parent, name):
                return replace(name, parent = parent)
            case (name,):
                return name

    def template(self, name, template_args):
        return replace(name, template_args = tuple(template_args))

    def _fold(self, child):
        return child

    def _list(self, *children):
        return children

    name = _fold
    type = _fold
    expression = _fold
    braced_expression = _fold
    unscoped_name = _fold
    unscoped_template_name = _fold
    template_prefix = _fold

    class_enum_type = _fold

    bare_function_type = _list

def create_transforms():
    return [
        SourceNameTransform(),
        SubstitutionTransform(),
        AstTransform(),
    ]
