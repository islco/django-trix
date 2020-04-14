// document.addEventListener('trix-file-accept', function(ev) {
//   ev.preventDefault();
// });


document.addEventListener('trix-attachment-add', function(ev) {

  var data = {};

  var request = new XMLHttpRequest();
  request.open('POST', '/trix/attachment/', true);
  request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
  request.send(data);

});

addEventListener('trix-initialize', function(event) {
  var trixElement = event.target;
  var id_regex = new RegExp('.*-__prefix__-.*');
  if (id_regex.test(trixElement.getAttribute('input'))) {
    var inputElement = trixElement.parentElement.previousElementSibling;
    if (inputElement) {
      trixElement.setAttribute('input', inputElement.id);
    }
  }
});
