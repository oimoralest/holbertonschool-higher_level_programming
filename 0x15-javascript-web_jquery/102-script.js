/**
 * This script fetches and prints how to say “Hello” depending on the language
 */
window.addEventListener('load', () => {
  $('INPUT#btn_translate').click(() => {
    $.get(
      `https://fourtonfish.com/hellosalut/?lang=${$('INPUT#language_code').val()}`,
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});
