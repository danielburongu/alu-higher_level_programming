#!/usr/bin/node
// script that computes and prints a factorial
function factorial(num) {
  if (isNaN(num) || num < 0) {
    return 1;
   } else if (num === 0) {
    return 1;
   } else {
    return num * factorial(num - 1);
   }
}
const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
