from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Datos de ejemplo almacenados localmente
gatos = [
    {"id": 1, "nombre": "Pelusa"},
    {"id": 2, "nombre": "Garfield"},
    # Agrega más gatos según sea necesario
]

perros = [
    {"id": 1, "nombre": "Firulais"},
    {"id": 2, "nombre": "Rex"},
    # Agrega más perros según sea necesario
]

hurones = [
    {"id": 1, "nombre": "Fuzzy"},
    {"id": 2, "nombre": "Canela"},
    # Agrega más hurones según sea necesario
]

boas = [
    {"id": 1, "nombre": "Slinky"},
    {"id": 2, "nombre": "Monty"},
    # Agrega más boas según sea necesario
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gato', methods=['GET'])
def gato():
    return jsonify({"animal": "Gato", "comportamiento": "duerme mucho y es independiente", "ejemplos": gatos})

@app.route('/perro', methods=['GET'])
def perro():
    return jsonify({"animal": "Perro", "comportamiento": "es leal y juguetón", "ejemplos": perros})

@app.route('/huron', methods=['GET'])
def huron():
    return jsonify({"animal": "Hurón", "comportamiento": "es curioso y activo", "ejemplos": hurones})

@app.route('/boa', methods=['GET'])
def boa():
    return jsonify({"animal": "Boa Constrictor", "comportamiento": "es silenciosa y sigilosa", "ejemplos": boas})

if __name__ == '__main__':
    app.run(debug=True)