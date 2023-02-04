#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

req.get(url, (err, res) => {
  if (err) throw err;
  fs.writeFile(file, res.body, 'utf8', (err) => {
    if (err) throw err;
  });
});
