#!/usr/bin/node
// a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done((json) => {
  json.results.forEach((title) => {
    $('ul#list_movies').append(`<li>${title}</li>`);
  });
});
