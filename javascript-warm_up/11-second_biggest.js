#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
console.log(process.argv.slice(2).sort((a, b) => b - a)[1] || 0);
