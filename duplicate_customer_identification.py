from openerp.osv import fields, osv
import csv
import os


class res_partner(osv.osv):
    _inherit = "res.partner"


    def duplicate_customer_identification(self, cr, uid, ids=None, context=None):

        absolute_path = os.path.dirname(os.path.abspath(__file__))

        file_list = ['/duplicate_customer_0.csv', '/duplicate_customer_1.csv', '/duplicate_customer_2.csv']

        # for file in file_list:
        res_partner_list = list()

        with open(absolute_path + file_list[2], 'r+') as csv_file:

            csv_reader = csv.reader(csv_file)
            for data in csv_reader:

                res_partner_list.append(int(data[0]))

        partners = self.browse(cr, uid, res_partner_list, context=context)

        for partner in partners:
            # customer's order quantity finding and status change on this part
            if partner.sale_order_count < 1 and partner.active is True:
                self.write(cr, uid, partner.id, {'active': False}, context=context)

        return True


