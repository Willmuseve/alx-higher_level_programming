$(function () {
  const link = 'https://www.fourtonfish.com/hellosalut';

  $('#btn_translate').on('click', () => {
    const x = $('#language_code').val();

    $.ajax({
      method: 'GET',
      link: link,
      dataType: 'json',
      data: {
        lang: x
      },
      success: (data) => {
        $('div#hello').text(data.hello);
      }
    });
  });
  $('#language_code').focus((e) => {
    const x = $('#language_code').val();
    const po = e.which;

    if (po == 13) {
      $.ajax({
        method: 'GET',
        link: link,
        dataType: 'json',
        data: {
          lang: x
        },
        success: (data) => {
          $('div#hello').text(data.hello);
        }
      });
    }
  });
});
