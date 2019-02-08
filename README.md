----------------------------------------------

Prefijos telefónicos de Venezuela
=================

----------------------------------------------

### Para Instanciar en odoo:
`from odoo.addons.your_addons.tools.vzla_code import Vzla_code`

### Para Verificar prefijo de Local CANTV:                    
    code_phone = Vzla_code()
        resp = code_phone.verify_local(self.local_phone)
        if not resp:
        	raise ValidationError(
        		u'Por favor coloque un código de área valido para el Teléfono loca de Venezuela')

### Para Verificar prefijo de Movil:                    
    code_phone = Vzla_code()
        resp = code_phone.verify_movil(self.movil_phone)
        if not resp:
        	raise ValidationError(
        		u'Por favor coloque un código de área valido para el Teléfono Movil de Venezuela')

### Formatos Esperados:
`xxxx | xxxx-xxxxxxx | xxxxxxxxxxx `

### Más Información:
- rhe@sinapsys.global

