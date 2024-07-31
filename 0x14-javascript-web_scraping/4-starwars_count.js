#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (_error, _response, body) => {
  const results = JSON.parse(body).results;
  let count = 0;

  for (const result of results) {
    const characters = result.characters;
    for (const character of characters) {
      if (character.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
