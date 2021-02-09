#!/usr/bin/node
/**
 * This script reads and prints the content of a file
 */
'use strict';
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
