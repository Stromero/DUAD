
const API_KEY = "free_user_3II7iluHc4JXm97RFvg2A7KoLX1"; 

const btnBuscar = document.getElementById("btnBuscar");
const resultado = document.getElementById("resultado");


btnBuscar.addEventListener("click", async () => {
  const id = document.getElementById("userId").value;

  if (!id) {
    resultado.innerHTML = `<p style="color:red;">Por favor, ingresa un ID válido.</p>`;
    return;
  }

  await buscarUsuarioPorId(id);
});


async function buscarUsuarioPorId(id) {
  try {
    resultado.innerHTML = `<p>Cargando usuario...</p>`;

    const response = await fetch(`https://reqres.in/api/users/${id}`, {
      headers: {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`Error ${response.status}: Usuario no encontrado`);
    }

    const data = await response.json();
    const user = data.data;

    if (user) {
      resultado.innerHTML = `
        <div style="margin-top: 15px; border: 1px solid #ccc; padding: 15px; width: max-content; border-radius: 8px;">
          <p><strong>Nombre:</strong> ${user.first_name}</p>
          <p><strong>Apellido:</strong> ${user.last_name}</p>
          <p><strong>Email:</strong> ${user.email}</p>
          <img src="${user.avatar}" alt="Avatar de ${user.first_name}" style="border-radius: 50%; margin-top: 10px;">
        </div>
      `;
    }
  } catch (error) {
    resultado.innerHTML = `<p style="color:red;">${error.message}</p>`;
    console.error("Detalle del error:", error);
  }
}

//Comment