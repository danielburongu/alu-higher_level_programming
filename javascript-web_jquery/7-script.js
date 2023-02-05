#!/usr/bin/node
//a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    type: 'GET',
    success: (result) => {
      $('#character').text(result.name);
    }
  });
  