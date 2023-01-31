#!/usr/bin/node
// a script that prints the addition of 2 integers
function add (a, b) {
  console.log(a + b);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
