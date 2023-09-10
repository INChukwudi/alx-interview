#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const outputMechanism = console.log;

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    outputCharacters(characters, 0, outputMechanism);
  }
});

function outputCharacters (characters, index, mechanism) {
  request(characters[index], (error, response, body) => {
    if (!error) {
      mechanism(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        outputCharacters(characters, index + 1, outputMechanism);
      }
    }
  });
}
