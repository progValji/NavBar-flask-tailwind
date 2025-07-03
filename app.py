from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

@app.route('/anfitrion')
def anfitrion():
    return render_template('anfitrion.html')

@app.route('/reseña')
def reseña():
    return render_template('reseña.html')

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)