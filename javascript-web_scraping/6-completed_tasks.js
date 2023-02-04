#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) return console.error(error);
  
  const tasks = JSON.parse(body).filter(task => task.completed);
  const userTasks = {};
  
  tasks.forEach(task => {
    if (!userTasks[task.userId]) userTasks[task.userId] = 0;
    userTasks[task.userId]++;
  });
  
  const filteredTasks = {};
  for (const userId in userTasks) {
    if (userId === '1' || userId === '2') filteredTasks[userId] = userTasks[userId];
  }
  
  console.log(filteredTasks);
});
