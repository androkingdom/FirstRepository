function factorial_of(number){
    var FactorialList = []
    while (number >= 1){
        FactorialList.push(number)
        number -= 1
    }
    let factorial = FactorialList.reduce((x,y) => {
        return x * y;
    })
    return factorial;
}

console.log(factorial_of(10))