/**
 * This script fetches and lists the title for all movies by using this URL:
 * https://swapi-api.hbtn.io/api/films/?format=json
 */
$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  (data) => {
    for (const movie of data.results) {
      $(`<li>${movie.title}</li>`).appendTo('UL#list_movies');
    }
  }
);
