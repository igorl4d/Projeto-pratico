from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_script import *
from sqlalchemy.sql import select
import banco
from banco import init, inserir, query_all

# inicia aplicação
app = Flask(__name__)

# inicia banco de dados
banco.init()

# Rota GET


@app.route("/info", methods=['GET'])
def get():

    resultado_query = banco.query_all()
    return jsonify({"Usuarios": resultado_query})

# ROTA POST


@app.route("/send/<nome>/<sobrenome>/<id_telegram>", methods=['POST'])
def post(nome, sobrenome, id_telegram):

    # Insere informações no banco de dados
    info = banco.inserir(usuario_nome=nome, usuario_sobrenome=sobrenome,
                         id_telegram=id_telegram)

    return jsonify({"text": "Obrigado por se cadastrar no sistema Wedev! Agradecemos pela confiança! Segue informações cadastradas:", "Nome": nome, "Sobrenome": sobrenome, "id_telegram": id_telegram})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
