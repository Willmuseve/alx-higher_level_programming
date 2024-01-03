#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
const charID = '18';
let c = 0;

request.get(link, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const x = JSON.parse(body);
    x.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charID)) {
          c += 1;
        }
      });
    });
    console.log(c);
  }
});
