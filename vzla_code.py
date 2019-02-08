# -*- coding: utf-8 -*-
#
#
#    SINAPSYS - Odoo Business Solutions
#
#
#    This software is developed by SINAPSYS GLOBAL S.A
#
#    For contact or information write to info@sinapsys.global
#    or Visit https://www.sinapsys.global
#
#    (C)2018
#
#############################################################################


class Vzla_code():
    local_code = [
        '0212', '0234', '0235', '0238', '0239', '0240', '0241', '0242',
        '0243', '0244', '0245', '0246', '0247', '0248', '0249', '0251',
        '0252', '0253', '0254', '0255', '0256', '0257', '0258', '0259',
        '0261', '0262', '0263', '0264', '0265', '0266', '0267', '0268',
        '0269', '0271', '0272', '0273', '0274', '0275', '0276', '0277',
        '0278', '0279', '0281', '0282', '0283', '0284', '0285', '0286',
        '0287', '0288', '0289', '0291', '0292', '0293', '0294', '0295',
    ]
    movil_code = ['0424', '0414', '0416', '0426', '0412']

    def verify_movil(self, numero):
        codigos = str(numero).split("-")
        code = str(codigos[0])
        if code in self.movil_code:
            return True
        else:
            return False

    def verify_local(self, numero):
        codigos = str(numero).split("-")
        code = str(codigos[0])
        if code in self.local_code:
            return True
        else:
            return False
