const crearPromesaPalabra = (palabra, ms) => {
  return new Promise(resolve => {
    setTimeout(() => resolve(palabra), ms);
  });
};


const listaOriginal = ["very", "dogs", "cute", "are"];


const promesaVery = crearPromesaPalabra(listaOriginal[0], 300);
const promesaDogs = crearPromesaPalabra(listaOriginal[1], 100);
const promesaCute = crearPromesaPalabra(listaOriginal[2], 400);
const promesaAre  = crearPromesaPalabra(listaOriginal[3], 200);



Promise.all([promesaDogs, promesaAre, promesaVery, promesaCute])
  .then(palabras => {
    
    const frase = palabras.join(" ");
    const fraseFinal = frase.charAt(0).toUpperCase() + frase.slice(1);
    
    console.log(fraseFinal); 
  })
  .catch(error => console.error("Error:", error));

  //comment