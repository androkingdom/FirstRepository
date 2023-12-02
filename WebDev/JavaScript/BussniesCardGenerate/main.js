let gen_number = () => {
    let random = Math.floor(Math.random() * 3) + 1
    return random
}

var gen = {
    Adjectives : {1 : "Crazy", 2 : "Amazing", 3 : "Fire"} , 
    Shop : {1 : "Engine", 2 : "Foods", 3 : "Garments"} , 
    Another : {1 : "Bros", 2 : "Limited", 3 : "Hub"}
}

let bussnes_name = `${gen.Adjectives[gen_number()]} ${gen.Shop[gen_number()]} ${gen.Another[gen_number()]} `
console.log(bussnes_name)
