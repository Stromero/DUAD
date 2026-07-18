const example = "This is a string!";
let result = [];
let palabra = "";

for (let i = 0; i < example.length; i++) {
    const char = example[i];

    if (char === " ") {
        
        if (palabra.length > 0) {
            result.push(palabra);
            palabra = "";
        }
    } else {
        
        palabra += char;
    }
}


if (palabra.length > 0) {
    result.push(palabra);
}

console.log("Entrada:", example);
console.log("Salida:", result);
