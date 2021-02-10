/**
 * This script adds, removes and clears LI elements from a list when the user
 * clicks
 */
window.addEventListener('load', () => {
  $('DIV#add_item').click(() => {
    $('<li>Item</li>').appendTo('UL.my_list');
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list LI').last().remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
