async function adder(p, s, text) {
    let promise = new Promise((resolve, reject) => {
        p.append(s)
        s.textContent = text

        let timer = setInterval(() => {
            s.append(".")
        }, 1500)

        setTimeout(() => {
            clearInterval(timer)
            resolve(1)
        }, 5000)

    })
    return await promise
    
}

let place = document.querySelector(".place")
let start = document.getElementsByTagName("button")
let sideBoxes = document.getElementsByClassName("code")

let span1 = document.createElement("span")
let span2 = document.createElement("span")
let span3 = document.createElement("span")
let span4 = document.createElement("span")
let span5 = document.createElement("span")

async function init() {
    await adder(place, span1, "Initializing Hacking")
    await adder(place, span2, "Reading your Files")
    await adder(place, span3, "Password files Detected")
    await adder(place, span4, "Sending all passwords and personal files to server")
    await adder(place, span5, "Cleaning up")
}


start[0].addEventListener("click",()=>{
    start[0].remove()
    init()
    
})


