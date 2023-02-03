#!/usr/bin/node
// a function that returns the number of occurrences in a list:
exports.esrever = function (list = []) {
    const newList = [];
    for (let i = list.length; i >= 0; i--) {
      newList.push(list[i]);
    }
    newList.shift();
    return newList;
  };
