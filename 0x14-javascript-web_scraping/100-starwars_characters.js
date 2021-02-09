#!/usr/bin/node
/**
 * This script prints all characters of a Star Wars movie
 */
'use strict';
const request = require('request');
request
  .get(
    `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
    (err, response, body) => {
      if (err) {
        console.log(err);
      } else if (response.statusCode === 200) {
        for (const character of JSON.parse(body).characters) {
          request
            .get(character, (err, response, body) => {
              if (err) {
                console.log(err);
              } else if (response.statusCode === 200) {
                console.log(JSON.parse(body).name);
              }
            });
        }
      }
    });
