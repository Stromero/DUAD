function cargarPrimerPokemon() {
  console.log("Buscando el Pokémon más rápido...");

  const promesas = [25, 150, 133].map(id => 
    fetch(`https://pokeapi.co/api/v2/pokemon/${id}`).then(r => r.json())
  );

  Promise.any(promesas)
    .then(pokemonRapido => {
      console.log(`El más rápido en responder fue: ${pokemonRapido.name}`);
    })
    .catch(err => {
      console.error("Ninguna promesa se cumplió:", err);
    })
    .finally(() => {
      console.log("Operación de Promise.any finalizada.");
    });
}

cargarPrimerPokemon();