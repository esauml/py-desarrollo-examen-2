from wtforms import Form 
from wtforms import StringField, RadioField, IntegerField
from wtforms import validators

class userForm(Form):
    matricula=StringField('Matricula',
        render_kw={'class':'form-control',"placeholder":"Ingresa tu matriucla"})
    
    grupo=StringField('grupo',
        render_kw={'class':'form-control',"placeholder":"Ingresa tu grupo"})
    
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.Length(min=3,max=30,message='Nombre no valido')
    ],
    render_kw={'class':'form-control',"placeholder":"Ingresa tu nombre"})
    
    apaterno=StringField('A. Paterno',[
        validators.DataRequired(message='El apellido es requerido'),
        validators.Length(min=3,max=30,message='Apellido no valido')
    ],
    render_kw={'class':'form-control',"placeholder":"Ingresa tu apellido materno"})
    
    amaterno=StringField('A. Materno',[
        validators.DataRequired(message='El apellido es requerido'),
        validators.Length(min=3,max=30,message='Apellido no valido')
    ],
    render_kw={'class':'form-control',"placeholder":"Ingresa tu apellido paterno"})
    
    sexo = RadioField('Sexo',
        choices = [(1, 'Maculino'), (2,'Femenino')],
        default='1',
        render_kw={'class':'input-radio100', 'required':'true'})
    
    dia=IntegerField('Dia',[
        validators.DataRequired(message='El dia es Invalido'),
        validators.NumberRange(min=1,max=31,message='Dia no valido')
    ],
    render_kw={'class':'form-control',"placeholder":"DD"})
    
    mes=IntegerField('Mes',[
        validators.DataRequired(message='El mes es invalido'),
        validators.number_range(min=1,max=12,message='Mes no valido')
    ],
    render_kw={'class':'form-control',"placeholder":"MM"})
    
    ano=IntegerField('Año',[
        validators.DataRequired(message='El año es invalido'),
        validators.NumberRange(min=1900,max=2050,message='Año no valido')
    ],
    render_kw={'class':'form-control',"placeholder":"YYYY"})
    
class examenForm(Form):
    p1 = RadioField('Pregunta 1',[validators.DataRequired(message='Es obligatorio marcar 1')],
        choices = [(0, '3.149215'), (1,'3.1416'), (0,'3.144492'), (0,'3.144123')],
        render_kw={'class':'form-check-input'})
    
    p2 = RadioField('Pregunta 2',[validators.DataRequired(message='Es obligatorio marcar 1')],
        choices = [(0, '26'), (1,'28'), (0,'-4'), (0,'64')],
        render_kw={'class':'form-check-input'})
    
    p3 = RadioField('Pregunta 3',[validators.DataRequired(message='Es obligatorio marcar 1')],
        choices = [(0, '-1'), (1,'1'), (0,'3'), (0,'6')],
        render_kw={'class':'form-check-input'})
    
    p4 = RadioField('Pregunta 4',[validators.DataRequired(message='Es obligatorio marcar 1')],
        choices = [(1, '5'), (0,'3'), (0,'10'), (0,'6')],
        render_kw={'class':'form-check-input'})
    
    p5 = RadioField('Pregunta 5',[validators.DataRequired(message='Es obligatorio marcar 1')],
        choices = [(0, '12'), (1,'27'), (0,'9'), (1,'27')],
        render_kw={'class':'form-check-input'})
    
    matricula=StringField('Matricula',
        render_kw={'class':'form-control',"placeholder":"Ingresa tu matriucla"})
    
    grupo=StringField('grupo',
        render_kw={'class':'form-control',"placeholder":"Ingresa tu grupo"})
    