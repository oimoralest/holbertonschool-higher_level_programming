#!/usr/bin/node
/**
 * This script computes the number of tasks completed by user id
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
    const tasks = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (tasks[task.userId] === undefined) {
          tasks[task.userId] = 0;
        }
        tasks[task.userId] += 1;
      }
    }
    console.log(tasks);
  }
});
