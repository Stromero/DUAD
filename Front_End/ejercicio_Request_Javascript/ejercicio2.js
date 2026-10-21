const axios = require("axios");


async function listObjectsAxios() {
  try {
    const response = await axios.get("https://api.restful-api.dev/objects");
    const objects = response.data;

    const filters = objects.filter(obj => obj.data);

    console.log("Objetos con data:");
    filters.forEach(obj => {
      console.log(`ID: ${obj.id}`);
      console.log(`Nombre: ${obj.name}`);
      console.log(`Data: ${JSON.stringify(obj.data)}`);
      console.log("-------------------------");
    });
  } catch (error) {
    console.error("Error al obtener objetos:", error.message);
  }
}


async function createObjectsAxios(info) {
  try {
    const response = await axios.post("https://api.restful-api.dev/objects", info);
    console.log("Objeto creado:", response.data);
    console.log("⚠️ ID generado:", response.data.id);
    return response.data.id;
  } catch (error) {
    console.error("Error al crear objeto:", error.message);
  }
}


async function getObjectAxios(id) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);
    console.log("Objeto encontrado:", response.data);
  } catch (error) {
    console.error("Error al obtener objeto:", error.message);
  }
}


async function updateObjectAxios(id, nuevosDatos) {
  try {
    const response = await axios.put(`https://api.restful-api.dev/objects/${id}`, nuevosDatos);
    console.log("Objeto actualizado:", response.data);
  } catch (error) {
    console.error("Error al actualizar objeto:", error.message);
  }
}


(async () => {
  await listObjectsAxios();

  const newId = await createObjectAxios({
    name: "Balón de Fútbol",
    data: { 
      marca: "Adidas", 
      modelo: "Al Rihla",
      color: "Blanco/Azul",
      tamaño: "5",
      material: "Poliuretano" 
    }
  });

  if (newId) {
    await getObjectAxios(newId);

    await updateObjectAxios(newId, {
      name: "Balón de Fútbol Actualizado",
      data: { marca: "Adidas", modelo: "Al Rihla Pro", año: 2026 }
    });

    await getObjectAxios(newId);
  }
})();
