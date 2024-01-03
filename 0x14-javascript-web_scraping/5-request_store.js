#!/usr/bin/node

const request = require('request');
const filesx = require('fs');
const link = process.argv[2];
const p = process.argv[3];

request(link, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    filesx.writeFile(p, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
