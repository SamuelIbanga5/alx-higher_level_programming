#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let height = 0; height < this.height; height++) {
        let x = 'X';
        for (let width = 0; width < this.width - 1; width++) {
          x += 'X';
        }
        console.log(x);
      }
    } else {
      for (let height = 0; height < this.height; height++) {
        let x = 'c';
        for (let width = 0; width < this.width - 1; width++) {
          x += 'c';
        }
        console.log(x);
      }
    }
  }
}
module.exports = Square;
