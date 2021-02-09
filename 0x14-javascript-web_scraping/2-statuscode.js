#!/usr/bin/node
/**
 * This script display the status code of a GET request
 */
'use strict';
const request = require('request');
request
  .get(process.argv[2])
  .on('response', (response) => {
    console.log(`code: ${response.statusCode}`);
  });
