#!/usr/bin/node
// a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header
$('div#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
