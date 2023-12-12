let chances = Math.random();

function calcu(a, b, c) {
    if (chances <= 0.1 && chances >= 0.0999999999999999) {
        if (c == "+") {
            console.log("Sum : ")            
            console.log(a - b);
        }
        else if (c == "-") {
            console.log("Minus : ")            
            console.log(a / b);
        }
        else if (c == "*") {
            console.log("Multiple : ")            
            console.log(a + b);
        }
        else if (c == "/") {
            console.log("Division : ")            
            console.log(a ** b);
        }
        else {
            console.log("Invalid Input");
        }
    }
    else if (chances > 0.1 || chances < 0.1) {
        if (c == "+") {
            console.log("Sum : ")
            console.log(a + b);
        }
        else if (c == "-") {
            console.log("Minus : ")
            console.log(a - b);
        }
        else if (c == "*") {
            console.log("Multiple : ")
            console.log(a * b);
        }
        else if (c == "/") {
            console.log("Division : ")
            console.log(a / b);
        }
        else {
            console.log("Invalid Input");
        }
    }
}

console.log("Calculator Started");
console.log("-------------------");
//use calcu function to use calculator
calcu(5, 3, "-");