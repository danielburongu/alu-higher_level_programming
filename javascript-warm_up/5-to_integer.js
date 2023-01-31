#!/usr/bin/node
// Number(process.argv[2]) converts the string argument to a number.
// isNaN(Number(process.argv[2])) checks if the conversion failed (i.e., if the argument is not a number).
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log("Not a number");
} else {
  console.log("My number: " + arg);
}
