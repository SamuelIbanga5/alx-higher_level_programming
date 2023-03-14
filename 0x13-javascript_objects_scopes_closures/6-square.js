#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      for (let height = 0; height < this.size; height++) {
        let x = 'X';
        for (let width = 0; width < this.size - 1; width++) {
          x += 'X';
        }
        console.log(x);
      }
    } else {
      for (let height = 0; height < this.size; height++) {
        let x = 'c';
        for (let width = 0; width < this.size - 1; width++) {
          x += 'c';
        }
        console.log(x);
      }
    }
  }
}
module.exports = Square;
