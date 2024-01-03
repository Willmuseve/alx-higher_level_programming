#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request.get(link, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const taskDone = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!taskDone[todo.userId]) {
        taskDone[todo.userId] = 1;
      } else {
        taskDone[todo.userId] += 1;
      }
    }
  });
  console.log(taskDone);
});
