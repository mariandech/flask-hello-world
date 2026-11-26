from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Computacion en la Nube</h1>
    <h2>Practica PaaS</h2>
    <p>Aplicacion desplegada mediante Render.</p>
    """
