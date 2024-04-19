from dataclasses import dataclass, field
from typing import List

@dataclass(frozen = True)
class BuiltinType:
    name: str

    def __str__(self):
        return self.name

@dataclass(frozen = True)
class Array:
    type: BuiltinType # TODO: any type
    count: int

    def __str__(self):
        return f'({self.type!s} [{self.count}])'

@dataclass(frozen = True)
class Literal:
    type: BuiltinType
    value: int

    def __str__(self):
        return f'({self.type!s}){self.value}'

@dataclass(frozen = True)
class AggregateInit:
    type: any # TODO
    values: tuple[any] # TODO

    def __str__(self):
        values = ', '.join(str(v) for v in self.values)
        return f'{self.type!s} {{{values}}}'

@dataclass(frozen = True)
class Function:
    name: 'Name'
    return_type: any # TODO
    argument_types: tuple[any] # TODO

    def __str__(self):
        args = ', '.join(str(a) for a in self.argument_types)
        signature = f'{self.name}({args})'

        if self.return_type is not None:
            signature = f'{self.return_type!s} {signature})'

        return signature

@dataclass(frozen = True)
class Name:
    name: str
    parent: 'Name | None' = None
    template_args: tuple[any] = None # TODO

    def __str__(self):
        s = self.name

        if self.parent is not None:
            s = f'{self.parent!s}::{s}'

        if self.template_args is not None:
            args = ', '.join(str(a) for a in self.template_args)
            s = f'{s}<{args}>'

        return s

    def __contains__(self, item):
        match item:
            case Name():
                return item.parent == self
            case Function():
                return item.name.parent == self

        return False

    @classmethod
    def from_string(cls, str):
        res = None
        for element in str.split('::'):
            res = cls(element, res)
        return res
