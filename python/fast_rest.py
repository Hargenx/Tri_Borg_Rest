import uuid
import logging
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*",
           "http://localhost:19000",
           "http://192.168.1.10:19000",
           "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tarefas = []


@app.get('/tarefas', response_model=List[dict])
async def busca_tarefas():
    print("Buscando todas as tarefas...")
    return tarefas

logger = logging.getLogger(__name__)

@app.post('/tarefas', response_model=dict, status_code=201)
async def incluir_tarefa(titulo: str) -> dict:
    try:
        logger.info(f"Incluindo nova tarefa com o título: {titulo}")
        nova_tarefa = {'id': str(uuid.uuid4()),
                       'titulo': titulo, 'feito': False}
        tarefas.append(nova_tarefa)
        return JSONResponse(content=nova_tarefa, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get('/tarefas/{tarefa_id}', response_model=dict)
async def busca_tarefa(tarefa_id: str):
    try:
        print(f"Buscando tarefa com ID: {tarefa_id}")
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                return {'tarefa': tarefa}
        raise HTTPException(status_code=404, detail='Tarefa não encontrada')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put('/tarefas/{tarefa_id}', response_model=dict)
async def atualiza_tarefa(tarefa_id: int, titulo: Optional[str] = None, feito: Optional[bool] = None):
    try:
        print(f"Atualizando tarefa com ID: {tarefa_id}")
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
        print(f"Deletando tarefa com ID: {tarefa_id}")
        global tarefas
        tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
        return {'message': 'Tarefa deletada'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
'''
pip install "uvicorn[standard]"
uvicorn fast_rest:app --reload
'''