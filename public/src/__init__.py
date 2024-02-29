from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Dados fictícios de alunos
alunos = [
    {"id": 1, "nome": "João", "idade": 20},
    {"id": 2, "nome": "Maria", "idade": 22},
    {"id": 3, "nome": "Pedro", "idade": 21}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/alunos')
def get_alunos():
    return jsonify(alunos)


