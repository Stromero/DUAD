function cargarTresPokemones() {
  console.log("Iniciando descarga de 3 Pokémon...");

  const promesas = [1, 4, 7].map(id => 
    fetch(`https://pokeapi.co/api/v2/pokemon/${id}`).then(r => r.json())
  );

  Promise.all(promesas)
    .then(resultados => {
      console.log("Nombres obtenidos via .then():");
      resultados.forEach(p => console.log(`- ${p.name}`));
    })
    .catch(err => {
      console.error("Error al cargar los Pokémon:", err);
    })
    .finally(() => {
      console.log("Operación de Promise.all finalizada.");
    });
}

cargarTresPokemones();