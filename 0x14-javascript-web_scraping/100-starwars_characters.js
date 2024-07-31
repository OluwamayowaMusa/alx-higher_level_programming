#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (_error, _response, body) => {
  const movie = JSON.parse(body);
  for (const character of movie.characters) {
    request(character, (_errr, _response, body) => {
      console.log(JSON.parse(body).name);
    });
  }
});
