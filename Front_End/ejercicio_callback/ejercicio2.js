const fs = require("fs");


const file1 = fs.readFileSync("Archivo1.txt", "utf8").split("\n").map(w => w.trim());
const file2 = fs.readFileSync("Archivo2.txt", "utf8").split("\n").map(w => w.trim());


const repeated = file1.filter(word => file2.includes(word));


console.log("Palabras repetidas en ambos archivos:");
console.log(repeated);


console.log("\nMensaje escondido:");
console.log(repeated.join(" "));
