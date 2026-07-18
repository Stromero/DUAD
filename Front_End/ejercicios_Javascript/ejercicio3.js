let celsius = [0, 20, 30, 40, 100];

// Fórmula: F = (C * 9/5) + 32
let fahrenheit = celsius.map(temp => (temp * 9/5) + 32);

console.log("Temperaturas en Celsius:", celsius);
console.log("Temperaturas en Fahrenheit:", fahrenheit);
