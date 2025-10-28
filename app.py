from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inicio')
def inicio():
    if 'usuario' not in session:
        return redirect(url_for('iniciarsession'))
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
        email = request.form.get("email")
        password = request.form.get("password")

        if not nombre or not apellido or not email or not password:
            flash("Por favor, completa todos los campos obligatorios.")
        else:
            flash(f"¡Registro exitoso para {nombre} {apellido}! Email: {email}")

    return render_template('registro.html')


@app.route('/iniciarsession', methods=['GET', 'POST'])
def iniciarsession():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            session['usuario'] = username
            return redirect(url_for('inicio'))  
        else:
            flash('Por favor, completa ambos campos.')

    return render_template('iniciarsession.html')


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('iniciarsession'))


if __name__ == '__main__':
    app.run(debug=True)

