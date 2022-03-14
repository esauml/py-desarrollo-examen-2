from flask import Blueprint
from flask import  redirect, render_template, request, url_for
from app.Forms import userForm as Form
from app.Operations import Filer, Operations


site = Blueprint('site', __name__, url_prefix="/site")

@site.route('/formulario', methods=['GET', 'POST'])
def form():
    form = Form(request.form)
    
    if request.method == 'POST':
        # form inputs
        matricula = form.matricula.data
        nombre = form.nombre.data
        apaterno = form.apaterno.data
        amaterno = form.amaterno.data
        grupo = form.grupo.data
        dia = int(form.dia.data)
        mes = int(form.mes.data)
        anio = int(form.ano.data)
        sexo = form.sexo.data
        edad = Operations().calcularEdad(anio, mes, dia)
        
        # user creation
        user = {
            'matricula': matricula, 
            'nombre': nombre, 
            'apaterno': apaterno, 
            'amaterno': amaterno, 
            'grupo': grupo, 
            'dia': dia, 
            'mes': mes, 
            'anio': anio,
            'sexo': sexo,
            'edad': edad
        }
        
        print(user)
        
        # user storage
        Filer().save(user)
        
        return redirect(url_for('index'))
    
    return render_template('form.html', form = form)
