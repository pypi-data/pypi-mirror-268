# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

from .common import line_mixin


class Line(line_mixin('sale'), metaclass=PoolMeta):
    __name__ = 'sale.line'
