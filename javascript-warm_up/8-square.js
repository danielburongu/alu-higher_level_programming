#!/usr/bin/node
// a script that prints a square
const num = parseInt(process.argv[2]);
if (num) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else if (num < 0) {
  console.log();
} else {
  console.log('Missing size');
}
