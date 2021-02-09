#!/usr/bin/node
/**
 * This script  prints the title of a Star Wars movie where the episode number
 * matches a given integer
 */
'use strict';
const request = require('request');
request({
  method: 'GET',
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`
}, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
