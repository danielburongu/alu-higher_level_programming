#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const req = require('request');

const getCompletedTasks = (data, userId) =>
  data.filter(({ userId: id, completed }) => id === userId && completed).length;

req(process.argv[2], (err, res, body) => {
  if (err) throw err;
  console.log(
    JSON.parse(body)
      .reduce((res, { userId }) => {
        if (!res[userId]) {
          const completed = getCompletedTasks(JSON.parse(body), userId);
          if (completed) res[userId] = completed;
        }
        return res;
      }, {})
  );
});
