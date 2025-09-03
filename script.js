  window.onload = function() {
  
  const formulario = document.querySelector(".formulario");

  formulario.addEventListener("submit", (evento) => {
    const nombre = document.getElementById("nombre").value.trim();
    const correo = document.getElementById("correo").value.trim();

    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (nombre === "" || correo === "") {
      evento.preventDefault(); // Evita que se envíe el formulario
      alert("⚠️ Antes de enviar tu mensaje a Biblioteca de las Sombras!, asegúrate de completar todos los campos obligatorios.");
    } else {
      alert("📨 Tu mensaje ha sido enviado con éxito. ¡Gracias por contactar con Biblioteca de las Sombras!");
    }

    if (!regexCorreo.test(correo)){
      evento.preventDefault();
      alert("ingresa un correo valido.");
      return;
    }


    fetch("/guardar", {
      method: "POST", 
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ nombre, correo })
    })
    .then(response => response.json())
    .then(data => {
      console.log("Datos guardados:", data);
    });
  });
  };