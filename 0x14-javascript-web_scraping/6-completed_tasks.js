#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, _response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const totalTodos = JSON.parse(body);
  const completedTodo = {};
  for (const todo of totalTodos) {
    if (todo.completed === true) {
      if (!(todo.userId in completedTodo)) {
        completedTodo[todo.userId] = 1;
      } else {
        completedTodo[todo.userId] += 1;
      }
    }
  }
  console.log(completedTodo);
});
