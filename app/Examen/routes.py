from crypt import methods
from flask import Blueprint
from flask import  redirect, render_template, request, url_for
from app.Operations import Filer, Operations
from app.Forms import examenForm as Form

examen = Blueprint('examen', __name__, url_prefix='/examen')

@examen.route('/', methods=['POST', 'GET'])
def examenForm():
    form = Form()
    
    if request.method == 'POST':
        # inputs
        matricula = request.form.get('matricula')
        grupo = request.form.get('grupo')
        
        # calificación de examen
        calificacion = (
            int(request.form.get('p1'))+
            int(request.form.get('p2'))+
            int(request.form.get('p3'))+
            int(request.form.get('p4'))+
            int(request.form.get('p5'))
        )
        calificacion*=2
        
        registro = {
            'matricula': matricula,
            'grupo': grupo,
            'calificacion': calificacion
        }

        # save score
        Filer().saveScore(registro)
        
        return redirect(url_for('index'))
    
    return render_template('examen.html', form = form)

@examen.route('/buscar', methods=['POST', 'GET'])
def buscar():
    
    if request.method=='POST':
        matricula = request.form.get('matricula')
        grupo = request.form.get('grupo')
        
        if matricula:
            criteria = matricula
        else:
            criteria = grupo
        
        users = Filer().readCriteria(criteria)
        scores = Filer().readScore(criteria)
        
        result = Operations().bind(users, scores)
        
        return render_template('buscar.html', done = 1, result = result)
    
    return render_template("buscar.html")
    