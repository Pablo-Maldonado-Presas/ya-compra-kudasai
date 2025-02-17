

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 



$(document).ready(function() {

  // evento para ocultar el mensaje de alerta
  $('.alerta .cerrar').click(function() {
    $('.alerta').hide();
  });

  // función para agregar un producto al carrito
  function agregarAlCarrito(nombre, precio) {
    var producto = {
      nombre: nombre,
      precio: precio
    };
    carrito.push(producto);
    localStorage.setItem('carrito', JSON.stringify(carrito)); // almacenar carrito en el almacenamiento local
    mostrarCarrito();
    actualizarBotonComprar(); // actualizar el estado del botón "Comprar"
  }

  // función para mostrar los productos del carrito
  function mostrarCarrito() {
    var carritoUl = $('.carrito ul');
    var total = 0;
    carritoUl.empty();

    // leer el carrito desde el almacenamiento local
    carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    for (var i = 0; i < carrito.length; i++) {
      var producto = carrito[i];
      carritoUl.append('<li>' + producto.nombre + ' - $' + producto.precio + ' <button class="eliminar" data-indice="' + i + '">Eliminar</button></li>');
      total += producto.precio;
    }
    $('.carrito p').text('Total: $' + total);
  }

  // evento para agregar un producto al carrito al hacer clic en el botón "Agregar al carrito"
  $('.agregar').click(function() {
    var nombre = $(this).data('nombre');
    var precio = $(this).data('precio');
    agregarAlCarrito(nombre, precio);
  });

  // evento para eliminar un producto del carrito al hacer clic en el botón "Eliminar"
  $(document).on('click', '.eliminar', function() {
    var indice = $(this).data('indice');
    carrito.splice(indice, 1);
    localStorage.setItem('carrito', JSON.stringify(carrito)); // actualizar el carrito en el almacenamiento local
    mostrarCarrito();
    actualizarBotonComprar(); // actualizar el estado del botón "Comprar"
  });

  // evento para comprar los productos del carrito al hacer clic en el botón "Comprar"
  $('.carrito button').click(function() {
    if (carrito.length > 0) {
      alert('Gracias por su compra');
      carrito = [];
      localStorage.setItem('carrito', JSON.stringify(carrito)); // vaciar el carrito en el almacenamiento local
      mostrarCarrito();
      actualizarBotonComprar(); // actualizar el estado del botón "Comprar"
    } else {
      alert('No hay productos en el carrito');
    }
  });

  // cargar el carrito desde el almacenamiento local al cargar la página
  mostrarCarrito();
  actualizarBotonComprar(); // actualizar el estado del botón "Comprar"

  // función para actualizar el estado del botón "Comprar"
  function actualizarBotonComprar() {
    if (carrito.length > 0) {
      $('.carrito button').prop('disabled', false);
    } else {
      $('.carrito button').prop('disabled', true);
    }
  }


  /* Carrusel */
   // Inicializar el carrusel
   $('#demo').carousel();

   // Intervalo de tiempo para cambiar de slide automáticamente
   $('.carousel').carousel({
     interval: 2000 // Cambiar a cada 2 segundos
   });

});



/* API Divisa */
$(document).ready(function() {
	var app_id = '931b07bd9c76460da8266882763edaf6'; // Reemplaza con tu propia App ID

	$.ajax({
	    url: 'https://openexchangerates.org/api/latest.json?app_id=' + app_id,
	    dataType: 'jsonp',
	    success: function(json) {
	        var clp_rate = json.rates.CLP.toFixed(2);
	        var usd_rate = (json.rates.CLP / json.rates.USD).toFixed(2);
	        var jpy_rate = (json.rates.CLP / json.rates.JPY).toFixed(2);
	        var tipo_cambio = '1 USD = ' + usd_rate + ' CLP / 1 JPY = ' + jpy_rate + ' CLP';
	        $('#tipo-cambio').text(tipo_cambio);
	    }
	});
});
