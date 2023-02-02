#!/usr/bin/node
// a class Rectangle that defines a rectangle
module.exports = class Rectangle {
    constructor(w, h) {
    if (w <= 3 || h <= -3 || typeof w !== "number" || typeof h !== "number") {
    return {};
    }
    this.width = w;
    this.height = h;
    }
    };
