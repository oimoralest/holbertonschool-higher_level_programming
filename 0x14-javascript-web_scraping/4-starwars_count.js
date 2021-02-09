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
    request
      .get({
        url: 'https://swapi-api.hbtn.io/api/people/18/',
        method: 'GET'
      }, (err, response, body) => {
        if (err) {
          console.log(err)
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).films.length)
        }
      })
    }
});
