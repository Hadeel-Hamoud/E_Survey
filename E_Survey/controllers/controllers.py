from odoo import http
from odoo.http import request


class Hayyak(http.Controller):
    @http.route(['/hayyak_survey'], type='http', auth='public', website=True)
    def my_route(self, **kw):
        return request.render('hayyak_survey.custom_welcome_layout')

    @http.route(['/survey_form'], type='http', auth='public', website=True)

    def button_action(self, **kw):
        return request.render('hayyak_survey.custom_survey_layout')

    @http.route('/survey_submitted', type='http', auth='public', website=True, methods=['POST'])
    def submit_form(self, **kw):
        request.env['hayyak.survey'].sudo().create(kw)
        return request.render('hayyak_survey.custom_thanks_layout')
