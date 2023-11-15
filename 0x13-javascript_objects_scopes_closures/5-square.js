#!/usr/bin/node
/**
 * a class that defines Square class that inherits from rectangle class
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
