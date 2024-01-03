#!/usr/bin/node

const filesx = require('fs');
const fName = process.argv[2];
const Info = process.argv[3];

filesx.writeFile(fName, Info, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
