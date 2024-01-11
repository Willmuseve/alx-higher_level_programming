$(function () {
  const films = $('ul#list_movies');
  const link = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.ajax({
    link: link,
    dataType: 'json',
    success: function (data) {
      const results = data.results;

      $.each(results, function (index, film) {
        films.append(`<li>${film.title}</li>`);
      });
    }
  });
});
