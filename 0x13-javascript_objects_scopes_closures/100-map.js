#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map(number => number * list.indexOf(number));
console.log(newList);
