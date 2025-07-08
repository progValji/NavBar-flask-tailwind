from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    seccion = "inicio"
    return render_template('index.html', seccion = seccion)

@app.route('/agenda')
def agenda():
    seccion = "agenda"
    return render_template('agenda.html', seccion = seccion)

@app.route('/reseña')
def reseña():
    seccion = "reseña"
    return render_template('reseña.html', seccion = seccion)

@app.route('/beneficios')
def beneficios():
    seccion = "beneficios"
    return render_template('beneficios.html', seccion = seccion)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)