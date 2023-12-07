console.log("Hello World !!")

let colour_list = [
    "red","green","blue","violet","yellow"
]

random_number = Math.floor(Math.random() * 5)

RandomColour = colour_list[Math.floor(random_number)]
console.log(`Your Random Colour is ${RandomColour}`)

get_container = document.querySelectorAll(".box")

get_container.forEach(e => {
    e.style.backgroundColor = RandomColour
});
