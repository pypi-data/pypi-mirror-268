# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

from .common import line_mixin


class Line(line_mixin('purchase'), metaclass=PoolMeta):
    __name__ = 'purchase.line'

    custom_item_number = fields.Char("Custom item number",
        states={
            'invisible': Eval('type') != 'line',
            },
        help='Put a value in this field to be used instead '
        'of the automatic numbering.')

    @classmethod
    def get_item_number(cls, lines, name):
        numbers = super().get_item_number(lines, name)

        for line in lines:
            if line.custom_item_number:
                numbers[line.id] = '%s *' % line.custom_item_number
        return numbers

    def get_invoice_line(self):
        lines = super().get_invoice_line()
        for line in lines:
            if self.custom_item_number:
                line.custom_item_number = self.custom_item_number
        return lines
