
document.getElementById('formulario').addEventListener('submit', function(event) {
  var email = document.getElementById('InputEmail1').value;
  var comentarios = document.getElementById('Textarea1').value;

  // Verifica si los campos están vacíos
  if (email === '') {
    swal('El campo de correo electrónico no puede estar vacío');
    event.preventDefault();
  } else if (comentarios === '') {
    swal('El campo de comentarios no puede estar vacío');
    event.preventDefault();
  }
});




