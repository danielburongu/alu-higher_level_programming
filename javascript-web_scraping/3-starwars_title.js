#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the episode number matches a given integer.
const req = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

req.get(url, (err, res) => {
  err ? console.log(err) : console.log(JSON.parse(res.body).title);
});
