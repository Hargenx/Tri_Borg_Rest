from flask import Flask, jsonify, request
from flask_cors import CORS  # pip install -U flask-cors

app = Flask(__name__)
CORS(app, resources={r"/tarefas/*": {"origins": "*"}})

tarefas = []

import uuid

@app.route('/tarefas', methods=['POST'])
def inclui_tarefa():
    try:
        novo_id = str(uuid.uuid4())  # Gera um UUID único
        nova_tarefa = {'id': novo_id, 'titulo': request.json['titulo'], 'feito': False}
        tarefas.append(nova_tarefa)
        return jsonify({'tarefa_incluida': nova_tarefa}), 201
    except KeyError:
        return jsonify({'error': 'Titulo da tarefa é obrigatório.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/tarefas', methods=['GET'])
def busca_tarefas():
    return jsonify({'tarefas': tarefas})

@app.route('/tarefas/<uuid:tarefa_id>', methods=['GET'])
def busca_tarefa_id(tarefa_id):
    try:
        global tarefas
        tarefa_id_str = str(tarefa_id)
        tarefa = next((tarefa for tarefa in tarefas if str(tarefa['id']) == tarefa_id_str), None)
        if tarefa:
            return jsonify({'tarefa': tarefa})
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/tarefas/<nome_tarefa>', methods=['GET'])
def busca_tarefa_por_nome(nome_tarefa):
    try:
        global tarefas
        tarefa_encontrada = next((tarefa for tarefa in tarefas if tarefa['titulo'] == nome_tarefa), None)
        if tarefa_encontrada:
            return jsonify({'tarefa': tarefa_encontrada})
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/tarefas/<uuid:tarefa_id>', methods=['PUT'])
def atualiza_tarefa(tarefa_id):
    try:
        global tarefas
        tarefa_id_str = str(tarefa_id)
        tarefa = next((tarefa for tarefa in tarefas if str(tarefa['id']) == tarefa_id_str), None)
        if tarefa:
            tarefa['titulo'] = request.json.get('titulo', tarefa['titulo'])
            tarefa['feito'] = request.json.get('feito', tarefa['feito'])
            return jsonify({'Tarefa_alterada': tarefa})
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tarefas/<uuid:tarefa_id>', methods=['DELETE'])
def apaga_tarefa(tarefa_id):
    try:
        global tarefas
        tarefa_id_str = str(tarefa_id)
        tarefas = [tarefa for tarefa in tarefas if str(tarefa['id']) != tarefa_id_str]
        return jsonify({'message': 'Tarefa deletada'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
