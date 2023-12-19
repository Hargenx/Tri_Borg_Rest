const axios = require('axios');

// https://openweathermap.org/history#data
require('dotenv').config();

const API_KEY = process.env.API_KEY;

async function getWeather(city) {
  try {
    const resposta = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`);
    const dados = resposta.data;
    console.log(`Clima -> ${city}:`);
    console.log(`Temperatura: ${dados.main.temp}°C`);
    c = dados.main.temp;    
    //c = (f-32)/1.8;
    f = (c*1.8)+32;
    console.log(`Temperatura: ${f}°F`);
    console.log(`Descrição: ${dados.weather[0].description}`);
  } catch (error) {
    console.error('Erro ao obter informações meteorológicas:', error.message);
  }
}

getWeather('Rio de Janeiro');
