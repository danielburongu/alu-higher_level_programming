#!/usr/bin/node
// a JavaScript script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: (json) => {
      $('div#hello').text(json);
    }
  });
