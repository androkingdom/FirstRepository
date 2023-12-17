// Question - 1
let btn_list = Array.from(document.querySelectorAll(".btns"))
btn_list[0].addEventListener("click", () => alert("Opps!!"))
btn_list[1].addEventListener("click", () => alert("Yay!!"))
btn_list[2].addEventListener("click", () => alert("Ahhh!!"))
btn_list[3].addEventListener("click", () => alert("Don't Do!!"))

// Question - 4
async function parseinjson(url){
    let a = await fetch(url)
    let b = await a.json()
    return b
}

setInterval(async function getdata(){
    let c = parseinjson("https://jsonplaceholder.typicode.com/todos/1")
    console.log(await c)
}
,1000)


// Question - 5
let Color = ["red", "green", "blue", "yellow"]
let bulb = document.getElementsByClassName("bulb")
setInterval(() => {
    let randomNum = Math.floor(Math.random() * 4)
    console.log(Color[randomNum])
    Array.from(bulb)[0].style.backgroundColor = Color[randomNum]
}, 1000)