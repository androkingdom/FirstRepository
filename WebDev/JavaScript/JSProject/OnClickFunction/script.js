boxinhtml = document.querySelectorAll(".container")

let ChangeColor = () => {
    boxinhtml.forEach(e => {
        e.style.backgroundColor = "red"
    });
}