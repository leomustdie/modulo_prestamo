from flask import Flask, render_template, request
import uuid

app = Flask(__name__)
app.secret_key = 'clave_secreta_total_segura_iti'

@app.route('/prestar_equipo', methods=['GET', 'POST'])
def prestar_equipo():
    resultado = None
    error = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        equipo = request.form.get('equipo')
        adeudos = request.form.get('adeudos')
        
        try:
            cuatrimestre = int(request.form.get('cuatrimestre', 0))
        except ValueError:
            cuatrimestre = 0

        if adeudos == 'Si':
            error = "Préstamo denegado: El estudiante cuenta con adeudos previos."
        
        elif equipo == 'Laptop de Pruebas' and cuatrimestre < 4:
            error = "Préstamo denegado: Requiere ser de 4to cuatrimestre o superior."
        
        else:
            folio = f"FOLIO-{uuid.uuid4().hex[:6].upper()}"
            resultado = {
                'folio': folio,
                'nombre': nombre,
                'equipo': equipo,
                'cuatrimestre': cuatrimestre
            }
            
    return render_template('prestar_equipo.html', resultado=resultado, error=error)

if __name__ == '__main__':
    print("Servidor corriendo en: http://127.0.0.1:5000/prestar_equipo")
    app.run(debug=True)