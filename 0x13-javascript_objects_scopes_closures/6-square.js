#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let str = '';
    let tmp = 'X';
    if (c) {
      tmp = c;
    }
    for (let i = 0; i < this.width; i++) { str += tmp; }
    for (let i = 0; i < this.width; i++) { console.log(str); }
  }
}

module.exports = Square;
