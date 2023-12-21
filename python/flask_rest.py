from flask import Flask, jsonify, request
from flask_cors import CORS #pip install -U flask-cors

app = Flask(__name__)
CORS(app)

tarefas = [
    {'id': 1, 'titulo': 'Estudar Python', 'feito': False},
    {'id': 2, 'titulo': 'Fazer compras', 'feito': False}
]

@app.route('/tarefas', methods=['GET'])
def busca_tarefas():
    return jsonify({'tarefas': tarefas})

@app.route('/tarefas', methods=['POST'])
def inclui_tarefa():
    try:
        nova_tarefa = {'id': len(tarefas) + 1, 'titulo': request.json['titulo'], 'feito': False}
        tarefas.append(nova_tarefa)
        return jsonify({'tarefa_incluida': nova_tarefa}), 201
    except KeyError:
        return jsonify({'error': 'Titulo da tarefa é obrigatório.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tarefas/<int:tarefa_id>', methods=['GET'])
def busca_tarefa(tarefa_id):
    try:
        tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == tarefa_id), None)
        if tarefa:
            return jsonify({'tarefa': tarefa})
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualiza_tarefa(tarefa_id):
    try:
        tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == tarefa_id), None)
        if tarefa:
            tarefa['titulo'] = request.json.get('titulo', tarefa['titulo'])
            tarefa['feito'] = request.json.get('feito', tarefa['feito'])
            return jsonify({'Tarefa_alterada': tarefa})
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def apaga_tarefa(tarefa_id):
    try:
        global tarefas
        tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
        return jsonify({'message': 'Tarefa deletada'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
