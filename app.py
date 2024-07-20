from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ch*col4t3.@localhost/TABLAS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Gato(db.Model):
    __tablename__ = 'gatos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Perro(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Hurón(db.Model):
    __tablename__ = 'hurones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class BoaConstrictor(db.Model):
    __tablename__ = 'boas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gato', methods=['GET'])
def gato():
    return jsonify({"animal": "Gato", "comportamiento": "duerme mucho y es independiente"})

@app.route('/perro', methods=['GET'])
def perro():
    return jsonify({"animal": "Perro", "comportamiento": "es leal y juguetón"})

@app.route('/huron', methods=['GET'])
def huron():
    return jsonify({"animal": "Hurón", "comportamiento": "es curioso y activo"})

@app.route('/boa', methods=['GET'])
def boa():
    return jsonify({"animal": "Boa Constrictor", "comportamiento": "es silenciosa y sigilosa"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
