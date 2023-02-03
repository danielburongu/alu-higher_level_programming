#!/usr/bin/node
// a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  return list.filter((n) => n === searchElement).length;
};
