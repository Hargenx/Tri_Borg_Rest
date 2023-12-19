package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

// const apiKey = "sua_chave_da_api"
type Config struct {
	APIKey string `json:"API_KEY"`
}

func loadConfig() (Config, error) {
	configFile, err := os.Open("../config.json")
	if err != nil {
		return Config{}, err
	}
	defer configFile.Close()

	var config Config
	jsonParser := json.NewDecoder(configFile)
	if err = jsonParser.Decode(&config); err != nil {
		return Config{}, err
	}

	return config, nil
}

type WeatherData struct {
	Main struct {
		Temp float64 `json:"temp"`
	} `json:"main"`
	Weather []struct {
		Description string `json:"description"`
	} `json:"weather"`
}

func getWeather(city string) {
	config, err := loadConfig()
	if err != nil {
		fmt.Println("Erro ao carregar configurações:", err)
		return
	}
	apiKey := config.APIKey
	url := fmt.Sprintf("http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=%s", city, apiKey)
	response, err := http.Get(url)
	if err != nil {
		fmt.Println("Erro ao obter informações meteorológicas:", err)
		return
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Println("Erro ao ler a resposta:", err)
		return
	}

	var data WeatherData
	err = json.Unmarshal(body, &data)
	if err != nil {
		fmt.Println("Erro ao decodificar a resposta:", err)
		return
	}

	fmt.Printf("Clima -> %s:\n", city)
	fmt.Printf("Temperatura: %.2f°C\n", data.Main.Temp)
	fmt.Printf("Descrição: %s\n", data.Weather[0].Description)
}

func main() {
	getWeather("Rio de Janeiro")
}
