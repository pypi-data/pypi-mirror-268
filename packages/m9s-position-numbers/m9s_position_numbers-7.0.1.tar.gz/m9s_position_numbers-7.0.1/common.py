# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelStorage, ModelView, fields


def line_mixin(prefix):
    class LineMixin(ModelStorage, ModelView):
        __slots__ = ()

        _numbered_types = ('line')

        item_number = fields.Function(fields.Char('Item number'),
            'get_item_number')

        @classmethod
        def get_item_number(cls, lines, name):
            numbers = {}
            numbered_lines = []
            if lines:
                if getattr(lines[0], prefix):
                    parent_lines = getattr(lines[0], prefix).lines
                    numbers = {id: None for id in [l.id for l in parent_lines]}
                    numbered_lines = [l for l in parent_lines
                        if l.type in cls._numbered_types]
                for nr, line in enumerate(numbered_lines, start=1):
                    numbers[line.id] = str(nr)
            return numbers

    return LineMixin
