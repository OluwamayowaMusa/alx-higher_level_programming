#!/usr/bin/node
const request = require('request');
const fs = require('node:fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, _response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(filename, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
