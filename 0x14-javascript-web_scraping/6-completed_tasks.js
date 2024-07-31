#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (_error, _response, body) => {
  const totalTodos = JSON.parse(body);
  const completedTodo = {};
  for (const todo of totalTodos) {
    if (!(todo.userId in completedTodo)) {
      completedTodo[todo.userId] = 0;
    }
    if (todo.completed === true) {
      completedTodo[todo.userId] += 1;
    }
  }
  console.log(completedTodo);
});
