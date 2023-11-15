#!/usr/bin/node

//Check the parameters provided

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let numb = '';
      let p = 0;
      while (p < this.width) {
        numb += 'X';
        p++;
      }

      console.log(numb);
    }
  }

  rotate () {
    let y = 0;
    y = this.width;
    this.width = this.height;
    this.height = y;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
