const fs = require("fs");

fs.readFile("Archivo1.txt", "utf8", (err, data1) => {
  if (err) {
    console.error("Error leyendo archivo1:", err);
    return;
  }

  
  fs.readFile("Archivo2.txt", "utf8", (err, data2) => {
    if (err) {
      console.error("Error leyendo archivo2:", err);
      return;
    }

    
    const words1 = data1.split("\n").map(w => w.trim());
    const words2 = data2.split("\n").map(w => w.trim());

   
    const repeated = words1.filter(word => words2.includes(word));

    
    console.log("Palabras repetidas en ambos archivos:");
    console.log(repeated);

    
    console.log("\nMensaje escondido:");
    console.log(repeated.join(" "));
  });
});
