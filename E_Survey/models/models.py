from odoo import fields, models


class HayyakSurvey(models.Model):
    _name = 'hayyak.survey'
    _description = 'Survey hayyak'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile Number')
    flight = fields.Char(string='Flight Number')
    text_area = fields.Text(string='Customer Suggestions')

    submission_date = fields.Datetime(string='Submission Date', default=fields.Datetime.now, readonly=True)

    rating1 = fields.Selection(
        [('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Fair'), ('4', 'Good'), ('5', 'Excellent')],
        string='Question 1: Food and beverage?')
    rating2 = fields.Selection(
        [('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Fair'), ('4', 'Good'), ('5', 'Excellent')],
        string='Question 2: Staff Service?')
    rating3 = fields.Selection(
        [('1', 'Very Poor'), ('2', 'Poor'), ('3', 'Fair'), ('4', 'Good'), ('5', 'Excellent')],
        string='Question 3: Facilities?')

    dropdown = fields.Selection(
        [('airline', 'Airline'), ('credit_card', 'Credit Card'), ('priority_pass', 'Priority Pass'),
         ('lounge_pass', 'Lounge Pass'), ('voucher', 'Voucher'), ('walk_in', 'Walk-in'),
         ('diners_club', 'Diners Club'), ('others', 'Others')],
        string='How do you normally gain entry to our lounge?')
