
from odoo import http
from odoo.http import request


class RatingProject(http.Controller):

    @http.route(['/curso/test'], type='http', auth="public", website=True)
    def curso_test(self, **kw):
        values = {'name': 'Prueba Curso'}
        return request.render('website_curso.website_curso_webform', values)

    @http.route(['/curso/test_submit'], type='http', auth="public", website=True)
    def curso_test_submit(self, **kw):
        # codigo para crear ...
        lead = request.env['crm.lead'].sudo().create({
            'name': kw.get('nombre')
        })
        values = {'result': 'Creado lead con id %d'%(lead.id)}
        return request.render('website_curso.website_curso_webform_submit', values)
