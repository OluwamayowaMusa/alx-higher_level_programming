$(() => {
  $('#language_code').on('keypress', (event) => {
    if (event.charCode === 13) {
      getTranlation();
    }
  });

  $('#btn_translate').on('click', () => {
    getTranlation();
  });
});

function getTranlation () {
  const requestUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const lang = $('#language_code').val();
  $.get(requestUrl + lang, (data) => {
    $('#hello').text(data.hello);
  });
}
