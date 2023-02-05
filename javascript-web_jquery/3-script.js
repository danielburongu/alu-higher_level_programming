#!/usr/bin/node
// a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header
$('div#red_header').click(() => {
    $('header').addClass('red');
  });
