
async function listObjects() {
  try {
    const response = await fetch("https://api.restful-api.dev/objects");

    if (!response.ok) {
      throw new Error("Error al obtener objetos");
    }

    const objects = await response.json();
    const filters = objects.filter(obj => obj.data);

    console.log("Objetos con data:");
    filters.forEach(obj => {
      console.log(`ID: ${obj.id}`);
      console.log(`Nombre: ${obj.name}`);
      console.log(`Data: ${JSON.stringify(obj.data)}`);
      console.log("-------------------------");
    });
  } catch (error) {
    console.error("Error:", error.message);
  }
}


async function createObject(info) {
  try {
    const response = await fetch("https://api.restful-api.dev/objects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(info)
    });

    if (!response.ok) {
      throw new Error("Error al crear objeto");
    }

    const newObject = await response.json();
    console.log("Objeto creado:", newObject);
    console.log("⚠️ ID generado:", newObject.id);
    return newObject.id;
  } catch (error) {
    console.error("Error:", error.message);
  }
}


async function getObject(id) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects/${id}`);

    if (!response.ok) {
      throw new Error("Objeto no encontrado");
    }

    const object = await response.json();
    console.log("Objeto encontrado:", object);
  } catch (error) {
    console.error("Error:", error.message);
  }
}


async function updateObject(id, nuevosDatos) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(nuevosDatos)
    });

    if (!response.ok) {
      throw new Error("Error al actualizar objeto");
    }

    const updated = await response.json();
    console.log("Objeto actualizado:", updated);
  } catch (error) {
    console.error("Error:", error.message);
  }
}


(async () => {
  await listObjects();

  const newId = await crearObjeto({
    name: "Mi Laptop",
    data: { 
      marca: "Dell", 
      modelo: "XPS 13",
      procesador: "Intel Core i7",
      memoriaRAM: "16GB",
      almacenamiento: "512gb SDD" 
    }
  });

  if (newId) {
    await getObject(newId);

    
    await updateObject(newId, {
      name: "Mi Laptop Actualizada",
      data: { marca: "Dell", modelo: "XPS 15", año: 2026 }
    });

    
    await getObject(newId);
  }
})();



