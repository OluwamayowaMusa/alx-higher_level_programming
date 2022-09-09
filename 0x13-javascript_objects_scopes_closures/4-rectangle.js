#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let str = '';
      for (let i = 0; i < this.width; i++) { str += 'X'; }
      for (let i = 0; i < this.height; i++) { console.log(str); }
    }
  }

  rotate () {
    if (this.width > 0 && this.height > 0) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  double () {
    if (this.width > 0 && this.height > 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
