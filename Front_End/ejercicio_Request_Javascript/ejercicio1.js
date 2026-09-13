
async function listarObjetos() {
  try {
    const response = await fetch("https://api.restful-api.dev/objects");

    if (!response.ok) {
      throw new Error("Error al obtener objetos");
    }

    const objetos = await response.json();
    const filtrados = objetos.filter(obj => obj.data);

    console.log("Objetos con data:");
    filtrados.forEach(obj => {
      console.log(`ID: ${obj.id}`);
      console.log(`Nombre: ${obj.name}`);
      console.log(`Data: ${JSON.stringify(obj.data)}`);
      console.log("-------------------------");
    });
  } catch (error) {
    console.error("Error:", error.message);
  }
}


async function crearObjeto(info) {
  try {
    const response = await fetch("https://api.restful-api.dev/objects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(info)
    });

    if (!response.ok) {
      throw new Error("Error al crear objeto");
    }

    const nuevo = await response.json();
    console.log("Objeto creado:", nuevo);
    console.log("⚠️ ID generado:", nuevo.id);
    return nuevo.id;
  } catch (error) {
    console.error("Error:", error.message);
  }
}


async function obtenerObjeto(id) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects/${id}`);

    if (!response.ok) {
      throw new Error("Objeto no encontrado");
    }

    const objeto = await response.json();
    console.log("Objeto encontrado:", objeto);
  } catch (error) {
    console.error("Error:", error.message);
  }
}


async function actualizarObjeto(id, nuevosDatos) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(nuevosDatos)
    });

    if (!response.ok) {
      throw new Error("Error al actualizar objeto");
    }

    const actualizado = await response.json();
    console.log("Objeto actualizado:", actualizado);
  } catch (error) {
    console.error("Error:", error.message);
  }
}


(async () => {
  await listarObjetos();

  const nuevoId = await crearObjeto({
    name: "Mi Laptop",
    data: { marca: "Dell", modelo: "XPS 13" }
  });

  if (nuevoId) {
    await obtenerObjeto(nuevoId);

    
    await actualizarObjeto(nuevoId, {
      name: "Mi Laptop Actualizada",
      data: { marca: "Dell", modelo: "XPS 15", año: 2026 }
    });

    
    await obtenerObjeto(nuevoId);
  }
})();



