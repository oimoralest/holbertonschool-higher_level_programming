#!/usr/bin/node
/**
 * This script prints the number of movies where the character “Wedge Antilles”
 * is present - Wedge Antilles is character ID 18
 */
'use strict';
const request = require('request');
request({
  method: 'GET',
  url: process.argv[2]
}, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let counter = 0;
    for (const movie of JSON.parse(body).results) {
      const string = movie.characters.toString();
      if (string.includes('/18/')) {
        counter++;
      }
    }
    console.log(counter);
  }
});
