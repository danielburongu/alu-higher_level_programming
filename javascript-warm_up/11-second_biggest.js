#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
console.log(Math.max(...process.argv.slice(2).sort((a,b) => b-a).slice(1,2)) || 0);
