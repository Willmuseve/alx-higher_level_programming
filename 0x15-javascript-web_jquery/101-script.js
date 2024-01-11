$(function () {
  const addItem = $('div#add_item');
  const removeItem = $('div#remove_item');
  const clearList = $('div#clear_list');
  const ulList = $('ul.my_list');

  addItem.on('click', () => {
    ulList.append('<li>Item</li>');
  });
  removeItem.on('click', () => {
    $('li').last().removeItem();
  });
  clearList.on('click', () => {
    ulList.empty();
  });
});
