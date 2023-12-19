# Exemplos de Uso de API e CRUD com Node.js, Go e Python

Este repositório contém exemplos de implementações simples de comunicação com APIs (como a Weather API) e operações CRUD usando Node.js, Go e Python.

## Node.js

### Weather API
- **Descrição:** Exemplo de comunicação com a Weather API para obter dados meteorológicos.
- **Arquivo:** `nodejs/weather-api.js`
- **Instruções de Uso:**
  - Instale as dependências: `npm install`
  - Execute o código: `node tempoApp.js`

### CRUD com Insomnia
- **Descrição:** Implementação básica de CRUD (Create, Read, Update, Delete) usando Node.js com Insomnia.
- **Arquivo:** `nodejs/app_rest.js`
- **Instruções de Uso:**
  - Execute o servidor: `node app_rest.js`
  - Use o Insomnia para testar as operações CRUD: 
    - Criar: POST `http://localhost:3000/tarefas`
    - Ler: GET `http://localhost:3000/tarefas`
    - Atualizar: PUT `http://localhost:3000/tarefas/:id`
    - Deletar: DELETE `http://localhost:3000/tarefas/:id`

## Go

### Weather API
- **Descrição:** Exemplo de comunicação com a Weather API para obter dados meteorológicos.
- **Arquivo:** `golang/tempoApp.go`
- **Instruções de Uso:**
  - Execute o código: `go run tempoApp.go`

### CRUD com Insomnia
- **Descrição:** Implementação básica de CRUD usando Go com Insomnia.
- **Arquivo:** `golang_rest/app_rest.go`
- **Instruções de Uso:**
  - Execute o servidor: `go run app_rest.go`
  - Utilize o Insomnia para testar as operações CRUD:
    - Criar: POST `http://localhost:8080/tarefas`
    - Ler: GET `http://localhost:8080/tarefas`
    - Atualizar: PUT `http://localhost:8080/tarefas/:id`
    - Deletar: DELETE `http://localhost:8080/tarefas/:id`

## Python

### Weather API
- **Descrição:** Exemplo de comunicação com a Weather API para obter dados meteorológicos.
- **Arquivo:** `python/tempoApp.py`
- **Instruções de Uso:**
  - Execute o código: `python tempoApp.py`

### CRUD com Insomnia
- **Descrição:** Implementação básica de CRUD usando Python com Insomnia.
- **Arquivo:** `python/app_rest.py`
- **Instruções de Uso:**
  - Execute o servidor: `python app_rest.py`
  - Utilize o Insomnia para testar as operações CRUD:
    - Criar: POST `http://localhost:5000/tarefas`
    - Ler: GET `http://localhost:5000/tarefas`
    - Atualizar: PUT `http://localhost:5000/tarefas/:id`
    - Deletar: DELETE `http://localhost:5000/tarefas/:id`
