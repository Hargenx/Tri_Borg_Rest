const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

let tarefas = [
    { id: 1, titulo: 'Estudar Node.js', feito: false },
    { id: 2, titulo: 'Fazer compras', feito: false }
];

app.get('/tarefas', (req, res) => {
    res.json({ tarefas });
});

app.post('/tarefas', (req, res) => {
    try {
        const novaTarefa = { id: tarefas.length + 1, titulo: req.body.titulo, feito: false };
        tarefas.push(novaTarefa);
        res.status(201).json({ tarefa_adicionada: novaTarefa });
    } catch (error) {
        res.status(400).json({ error: 'Titulo da tarefa é obrigatório.' });
    }
});

app.get('/tarefas/:tarefaId', (req, res) => {
    const tarefa = tarefas.find(tarefa => tarefa.id === parseInt(req.params.tarefaId));
    if (tarefa) {
        res.json({ tarefa });
    } else {
        res.status(404).json({ message: 'Tarefa não encontrada' });
    }
});

app.put('/tarefas/:tarefaId', (req, res) => {
    const tarefa = tarefas.find(tarefa => tarefa.id === parseInt(req.params.tarefaId));
    if (tarefa) {
        tarefa.titulo = req.body.titulo || tarefa.titulo;
        tarefa.feito = req.body.feito || tarefa.feito;
        res.json({ tarefa_updated: tarefa });
    } else {
        res.status(404).json({ message: 'Tarefa não encontrada' });
    }
});

app.delete('/tarefas/:tarefaId', (req, res) => {
    tarefas = tarefas.filter(tarefa => tarefa.id !== parseInt(req.params.tarefaId));
    res.json({ message: 'Tarefa deletada' });
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
