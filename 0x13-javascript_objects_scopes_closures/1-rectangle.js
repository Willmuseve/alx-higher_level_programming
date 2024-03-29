#!/usr/bin/node

/*
 * a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments w and h
*/

class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0 || w < 0 || h < 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
