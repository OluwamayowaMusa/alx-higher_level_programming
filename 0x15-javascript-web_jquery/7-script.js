$(() => {
  const requestUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(requestUrl, (data) => {
    $('#character').text(data.name);
  });
});
