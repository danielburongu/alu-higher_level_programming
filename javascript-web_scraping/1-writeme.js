#!/usr/bin/node
// a script that writes a string to a file.
const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log('C is fun');
  }
});
