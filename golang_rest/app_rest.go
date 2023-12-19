package main

import (
	"encoding/json"
	"log"
	"net/http"
	"strconv"

	//go get -u github.com/gorilla/mux
	"github.com/gorilla/mux"
)

type Tarefa struct {
	ID     int    `json:"id"`
	Titulo string `json:"titulo"`
	Feito  bool   `json:"feito"`
}

var tarefas = []Tarefa{
	{ID: 1, Titulo: "Estudar Go", Feito: false},
	{ID: 2, Titulo: "Fazer compras", Feito: false},
}

func pegaTarefa(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(tarefas)
}

func criaTarefa(w http.ResponseWriter, r *http.Request) {
	var newtarefa Tarefa
	_ = json.NewDecoder(r.Body).Decode(&newtarefa)
	newtarefa.ID = len(tarefas) + 1
	tarefas = append(tarefas, newtarefa)
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(newtarefa)
}

func pegaTarefas(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	tarefaID, _ := strconv.Atoi(params["tarefaID"])
	for _, tarefa := range tarefas {
		if tarefa.ID == tarefaID {
			json.NewEncoder(w).Encode(tarefa)
			return
		}
	}
	json.NewEncoder(w).Encode(map[string]string{"message": "Tarefa não encontrada"})
}

func atualizaTarefa(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	tarefaID, _ := strconv.Atoi(params["tarefaID"])

	for index, tarefa := range tarefas {
		if tarefa.ID == tarefaID {
			var updatedtarefa Tarefa
			_ = json.NewDecoder(r.Body).Decode(&updatedtarefa)
			tarefas[index].Titulo = updatedtarefa.Titulo
			tarefas[index].Feito = updatedtarefa.Feito
			json.NewEncoder(w).Encode(tarefas[index])
			return
		}
	}
	json.NewEncoder(w).Encode(map[string]string{"message": "Tarefa não encontrada"})
}

func apagaTarefa(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	tarefaID, _ := strconv.Atoi(params["tarefaID"])

	for index, tarefa := range tarefas {
		if tarefa.ID == tarefaID {
			tarefas = append(tarefas[:index], tarefas[index+1:]...)
			json.NewEncoder(w).Encode(map[string]string{"message": "Tarefa deletada"})
			return
		}
	}
	json.NewEncoder(w).Encode(map[string]string{"message": "Tarefa não encontrada"})
}

func main() {
	router := mux.NewRouter()

	router.HandleFunc("/tarefas", pegaTarefas).Methods("GET")
	router.HandleFunc("/tarefas", criaTarefa).Methods("POST")
	router.HandleFunc("/tarefas/{tarefaID}", pegaTarefas).Methods("GET")
	router.HandleFunc("/tarefas/{tarefaID}", atualizaTarefa).Methods("PUT")
	router.HandleFunc("/tarefas/{tarefaID}", apagaTarefa).Methods("DELETE")

	log.Fatal(http.ListenAndServe(":8080", router))
}
