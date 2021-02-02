#!/usr/bin/node
const len = process.argv.length - 2;
const data = process.argv.slice(2);
if (len <= 1) {
  console.log('0');
} else {
  data.sort((a, b) => {
    return a - b;
  });
  console.log(data[len - 2]);
}
