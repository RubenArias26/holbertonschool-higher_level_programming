document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.text())
    .then(data => {
      document.getElementById('hello').textContent = data;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
