#!/usr/bin/node

const fs = require('fs');

let content = fs.readFileSync(process.argv[2], { flag: 'r', encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.error(err);
  }
});
content += fs.readFileSync(process.argv[3], { flag: 'r', encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.error(err);
  }
});
fs.writeFileSync(process.argv[4], content, { flag: 'w', encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  }
});
