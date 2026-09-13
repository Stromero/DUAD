const axios = require("axios");


async function listarObjetosAxios() {
  try {
    const response = await axios.get("https://api.restful-api.dev/objects");
    const objetos = response.data;

    const filtrados = objetos.filter(obj => obj.data);

    console.log("Objetos con data:");
    filtrados.forEach(obj => {
      console.log(`ID: ${obj.id}`);
      console.log(`Nombre: ${obj.name}`);
      console.log(`Data: ${JSON.stringify(obj.data)}`);
      console.log("-------------------------");
    });
  } catch (error) {
    console.error("Error al obtener objetos:", error.message);
  }
}


async function crearObjetoAxios(info) {
  try {
    const response = await axios.post("https://api.restful-api.dev/objects", info);
    console.log("Objeto creado:", response.data);
    console.log("⚠️ ID generado:", response.data.id);
    return response.data.id;
  } catch (error) {
    console.error("Error al crear objeto:", error.message);
  }
}


async function obtenerObjetoAxios(id) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);
    console.log("Objeto encontrado:", response.data);
  } catch (error) {
    console.error("Error al obtener objeto:", error.message);
  }
}


async function actualizarObjetoAxios(id, nuevosDatos) {
  try {
    const response = await axios.put(`https://api.restful-api.dev/objects/${id}`, nuevosDatos);
    console.log("Objeto actualizado:", response.data);
  } catch (error) {
    console.error("Error al actualizar objeto:", error.message);
  }
}


(async () => {
  await listarObjetosAxios();

  const nuevoId = await crearObjetoAxios({
    name: "Balón de Fútbol",
    data: { marca: "Adidas", modelo: "Al Rihla" }
  });

  if (nuevoId) {
    await obtenerObjetoAxios(nuevoId);

    await actualizarObjetoAxios(nuevoId, {
      name: "Balón de Fútbol Actualizado",
      data: { marca: "Adidas", modelo: "Al Rihla Pro", año: 2026 }
    });

    await obtenerObjetoAxios(nuevoId);
  }
})();
