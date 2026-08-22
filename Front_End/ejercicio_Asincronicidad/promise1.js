
const pokemonIds = [1, 4, 7]; // Bulbasaur, Charmander, Squirtle


const promesasPokemon = pokemonIds.map(id =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => {
      if (!res.ok) throw new Error(`Error en el Pokémon ${id}`);
      return res.json();
    })
);


Promise.all(promesasPokemon)
  .then(pokemones => {
    // Extraer y mostrar los nombres al mismo tiempo
    const nombres = pokemones.map(p => p.name);
    console.log("Los 3 Pokémon cargados simultáneamente:", nombres);
  })
  .catch(error => console.error("Error en Promise.all:", error));