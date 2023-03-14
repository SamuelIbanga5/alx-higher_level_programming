#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let height = 0; height < this.height; height++) {
      let x = 'X';
      for (let width = 0; width < this.width - 1; width++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}
module.exports = Rectangle;
