#!/usr/bin/node

const oldSq = require('./5-square');
class Square extends oldSq {
  charPrint (C) {
    if (!C) {
      C = 'X';
    }
    for (let k = 0; k < this.width; k++) {
      console.log(C.repeat(this.width));
    }
  }
}
module.exports = Square;
