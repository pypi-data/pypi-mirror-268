# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase


class PositionNumbersTestCase(ModuleTestCase):
    "Test Position Numbers module"
    module = 'position_numbers'
    extras = ['account_invoice', 'purchase', 'sale']


del ModuleTestCase
