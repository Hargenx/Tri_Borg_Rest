from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

tarefas = [
    {'id': 1, 'titulo': 'Estudar Python', 'feito': False},
    {'id': 2, 'titulo': 'Fazer compras', 'feito': False}
]

@app.get('/tarefas', response_model=List[dict])
async def busca_tarefas():
    return {'tarefas': tarefas}

@app.post('/tarefas', response_model=dict, status_code=201)
async def inclui_tarefa(titulo: str):
    try:
        nova_tarefa = {'id': len(tarefas) + 1, 'titulo': titulo, 'feito': False}
        tarefas.append(nova_tarefa)
        return {'tarefa_incluida': nova_tarefa}
    except KeyError as e:
        raise HTTPException(status_code=400, detail='Titulo da tarefa é obrigatório.')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/tarefas/{tarefa_id}', response_model=dict)
async def busca_tarefa(tarefa_id: int):
    try:
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                return {'tarefa': tarefa}
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put('/tarefas/{tarefa_id}', response_model=dict)
async def atualiza_tarefa(tarefa_id: int, titulo: Optional[str] = None, feito: Optional[bool] = None):
    try:
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                if titulo:
                    tarefa['titulo'] = titulo
                if feito is not None:
                    tarefa['feito'] = feito
                return {'Tarefa_alterada': tarefa}
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete('/tarefas/{tarefa_id}', response_model=dict)
async def apaga_tarefa(tarefa_id: int):
    try:
        global tarefas
        tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
        return {'message': 'Tarefa deletada'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
'''
pip install "uvicorn[standard]"
uvicorn fast_rest:app --reload
'''