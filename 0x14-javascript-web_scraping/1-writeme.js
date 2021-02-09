#!/usr/bin/node
/**
 * This script writes a string to a files
 */
'use strict';
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
