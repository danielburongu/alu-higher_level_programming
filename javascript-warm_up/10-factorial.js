#!/usr/bin/node
// script that computes and prints a factorial
function factorial(n) {
    if (n === 0) return 1;
    return n * factorial(n - 1);
  }
  console.log(factorial(parseInt(process.argv[2])) || 1);
