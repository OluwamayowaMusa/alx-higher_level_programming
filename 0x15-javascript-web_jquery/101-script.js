$(() => {
  $('#add_item').on('click', () => {
    const item = '<li>Item</li>';
    $('ul.my_list').append(item);
  });

  $('#remove_item').on('click', () => {
    const updatedList = $('ul.my_list li').toArray();
    updatedList.pop();

    $('ul.my_list').empty();

    $.each(updatedList, (_index, item) => {
      $('ul.my_list').append(item);
    });
  });

  $('#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
});
