from flask import Flask, jsonify, request

aplicacao = Flask(__name__)

usuarios = []

# Consultar todos os usuarios cadastrados


@aplicacao.route('/usuarios', methods=['GET'])
def consultar_usuarios():
    return jsonify(usuarios)

# Consultar somente um usuario pelo cpf


@aplicacao.route('/usuarios/<int:cpf>', methods=['GET'])
def consultar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario.get('cpf') == cpf:
            return jsonify(usuario)

# Criar


@aplicacao.route('/usuarios', methods=['POST'])
def incluir_novo_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)

    return jsonify(usuarios)


aplicacao.run(port=5000, host='localhost', debug=True)
