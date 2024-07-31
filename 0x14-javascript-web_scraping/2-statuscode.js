#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
request(URL, (_error, response, _body) => {
  console.log('code:', response.statusCode);
});
