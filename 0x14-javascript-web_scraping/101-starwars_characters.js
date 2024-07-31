#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (_error, _response, body) => {
  const movie = JSON.parse(body);
  const names = {};
  for (const character of movie.characters) {
    request(character, (_errr, _response, body) => {
      const characterId = character.slice(43, -1);
      names[characterId] = JSON.parse(body).name;
      if (Object.keys(names).length === movie.characters.length) {
        for (const key of Object.keys(names)) {
          console.log(names[key]);
        }
      }
    });
  }
});
