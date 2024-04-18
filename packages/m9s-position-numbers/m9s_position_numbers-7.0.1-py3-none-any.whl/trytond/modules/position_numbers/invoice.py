# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

from .common import line_mixin


class Line(line_mixin('invoice'), metaclass=PoolMeta):
    __name__ = 'account.invoice.line'

    custom_item_number = fields.Char("Custom item number",
        states={
            'invisible': ((Eval('type') != 'line')
                | (Eval('invoice_type') != 'in'))
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
