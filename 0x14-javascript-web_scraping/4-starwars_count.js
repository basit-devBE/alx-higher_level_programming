#!/usr/bin/node
/**
 * A script that prints the number of movies where
 *  the character "Wedge Antilles" is present.
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
