$(() => {
  const requestUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').on('click', () => {
    const lang = $('#language_code').val();
    $.get(requestUrl + lang, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
