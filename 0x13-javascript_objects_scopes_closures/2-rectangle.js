#!/usr/bin/bash

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      this = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
