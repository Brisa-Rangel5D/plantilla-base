from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'  

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app.route('/animales')
def animales():
    return render_template('animales.html')


@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')


@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')


@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


@app.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        anio = request.form.get("anio")
        genero = request.form.get("genero")
        email = request.form.get("email")
        password = request.form.get("password")

    
        if len(password) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.")
        elif not nombre or not apellido or not email or not password:
            flash("Por favor, completa todos los campos obligatorios.")
        else:
            flash(f"¡Registro exitoso para {nombre} {apellido}! "
                f"Nacido el {dia} de {mes} de {anio}, Género: {genero}, Email: {email}")

    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)
