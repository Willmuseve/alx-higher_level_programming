#!/usr/bin/node

const request = require('request');
const filmID = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

request.get(link, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
