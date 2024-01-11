$(function () {
  const link = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const SayHello = $('div#hello');

  $.ajax({
    link: link,
    dataType: 'json',
    success: function (data) {
      SayHello.text(data.Sayhello);
    }
  });
});
