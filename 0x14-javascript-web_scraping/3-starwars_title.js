#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (_error, _response, body) => {
  console.log(JSON.parse(body).title);
});
