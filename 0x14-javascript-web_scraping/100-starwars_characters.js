#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];
const link = `https://swapi.dev/api/films/${filmID}/`;

request.get(link, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const x = JSON.parse(body);
  const characters = x.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
