from odoo import http
from odoo.http import request
import logging

class SaleData(http.controller):
    @http.route("/bigcommerce",auth="public", type='json')
    def sale_data(self, **post):
        logging.info(f"=======================Insiade{post}")
        return True

    @http.route("/load", auth="public")
    def sale(self, **post):
        logging.info(f"=======================Insiade")
        return True