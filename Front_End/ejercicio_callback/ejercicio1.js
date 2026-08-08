
function checkNumber(num, callbackEven, callbackOdd) {
if (num % 2 === 0) {
    callbackEven();
} else {
    callbackOdd();
}
}

function showEven() {
console.log("The number is even!");
}

function showOdd() {
console.log("The number is odd!");
}

checkNumber(4, showEven, showOdd);
checkNumber(7, showEven, showOdd); 
