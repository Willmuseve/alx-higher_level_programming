#!/usr/bin/node

const filesx = require('fs');

const filepath = process.argv[2];

filesx.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
