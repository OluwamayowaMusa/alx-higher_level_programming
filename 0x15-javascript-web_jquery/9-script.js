$(() => {
  const requestUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(requestUrl, (data) => {
    $('#hello').text(data.hello);
  });
});
