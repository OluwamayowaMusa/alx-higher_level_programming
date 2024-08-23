$(() => {
  const requestUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(requestUrl, (data) => {
    $.each(data.results, (_index, movies) => {
      $('#list_movies').append(`<li>${movies.title}</li>`);
    });
  });
});
