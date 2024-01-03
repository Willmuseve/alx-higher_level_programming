#!/usr/bin/node

//declarations
const request = require('request');
const link = process.argv[2];

request.get(link, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const DoneT = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!DoneT[todo.userId]) {
        DoneT[todo.userId] = 1;
      } else {
        DoneT[todo.userId] += 1;
      }
    }
  });
  console.log(DoneT);
});
