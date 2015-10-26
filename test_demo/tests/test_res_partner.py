from openerp.tests import common
from openerp.addons.test_demo.models import res_partner


class testResPartner(common.TransactionCase):

# The "setup"
    def setUp(self):
        #stuff run before all the tests
        super(testResPartner, self).setUp()
        self.partner = self.env['res.partner'].create({'name':'Bob', 'age':25, 'increase_age':True})

# The first test function (success)
    def test__onchange_increase_age(self):
        print("First test:")
        self.partner._onchange_increase_age()
        self.assertEqual(self.partner.age, 26, "The test #1 has failed!")

# The second test (failure)
    # @common.expectedFailure()
    def test__onchange_increase_age_fail(self):
        print("Second test:")
        self.partner._onchange_increase_age()
        self.assertEqual(self.partner.age, 29, "The test #2 has failed!")
