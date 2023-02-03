#!/usr/bin/node
// a class Square that defines a square and inherits from Square of 5-square.js:
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
