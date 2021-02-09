#!/usr/bin/node
/**
 * This script gets the contents of a webpage and stores it in a file
 */
'use strict';
const fs = require('fs');
const request = require('request');
request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
