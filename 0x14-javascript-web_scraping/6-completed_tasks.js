#!/usr/bin/node
/**
 * A script that prints the number of tasks completed by a user.
 * The user ID matches a given integer.
 */
const request = require('request');
const userId = process.argv[2];
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter(task => task.userId === parseInt(userId) && task.completed);
    console.log(completedTasks.length);
  }
});
