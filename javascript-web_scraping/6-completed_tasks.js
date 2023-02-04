#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};
    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    });
    console.log(completedTasksByUser);
  }
});
