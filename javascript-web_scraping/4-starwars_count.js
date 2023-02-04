#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present.
const req = require("request");
const url = "https://swapi-api.alx-tools.com/api/films/";

req.get(url, (err, res) => {
  if (err) throw err;
  let count = 0;
  JSON.parse(res.body).forEach((film) => {
    film.characters.forEach((char) => {
      if (char.includes("18")) count++;
    });
  });
  console.log(`Wedge Antilles appears in ${count} films`);
});
