#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];
const link = `https://swapi.dev/api/films/${filmID}/`;
let characters = [];

request(link, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const x = JSON.parse(body);
  characters = x.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterx = JSON.parse(body);
    console.log(characterx.name);
    getCharacters(index + 1);
  });
};
