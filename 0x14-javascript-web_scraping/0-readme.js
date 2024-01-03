#!/usr/bin/node

const filesx = require('fs');

const p = process.argv[2];

filesx.readFile(P, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
