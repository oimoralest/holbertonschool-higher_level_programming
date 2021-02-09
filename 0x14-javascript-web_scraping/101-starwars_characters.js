#!/usr/bin/node
/**
 * This script prints all characters of a Star Wars movie
 */
'use strict';
const request = require('request');
const makeGetRequest = (url) => {
  return new Promise((resolve, reject) => {
    request
      .get(url, (err, response, body) => {
        if (err || response.statusCode !== 200) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
  });
};
async function main () {
  const result = await makeGetRequest(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`);
  for (const character of result.characters) {
    const { name } = await makeGetRequest(character);
    console.log(name);
  }
}
main();
