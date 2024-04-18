# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import invoice
from . import purchase
from . import sale

__all__ = ['register']


def register():
    Pool.register(
        invoice.Line,
        module='position_numbers', type_='model', depends=['account_invoice'])
    Pool.register(
        purchase.Line,
        module='position_numbers', type_='model', depends=['purchase'])
    Pool.register(
        sale.Line,
        module='position_numbers', type_='model', depends=['sale'])
    Pool.register(
        module='position_numbers', type_='model')
    Pool.register(
        module='position_numbers', type_='wizard')
    Pool.register(
        module='position_numbers', type_='report')
