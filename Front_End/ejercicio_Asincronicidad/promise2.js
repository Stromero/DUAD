const pokemonIds = [25, 150, 133]; // Pikachu, Mewtwo, Eevee

const promesasPokemonAny = pokemonIds.map(id =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => {
      if (!res.ok) throw new Error(`Error en ID ${id}`);
      return res.json();
    })
);


Promise.any(promesasPokemonAny)
  .then(primerPokemon => {
    console.log("El primer Pokémon recibido fue:", primerPokemon.name);
  })
  .catch(error => console.error("Todas las promesas fallaron:", error));

  //comment