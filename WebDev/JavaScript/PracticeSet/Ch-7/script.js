// Question - 1 
let first_nav_item = document.querySelector(".NavBarItems")
first_nav_item.style.backgroundColor = "red"

// Question - 2
// Answer == No

// Question - 3
document.querySelector(".container").firstElementChild.style.backgroundColor = "green"
document.querySelector(".container").lastElementChild.style.backgroundColor = "green"

// Question - 4
let list = document.querySelector(".list")
let LIs = list.getElementsByTagName('li')
lis_list = Array.from(LIs)
lis_list.forEach(e => {
    e.style.backgroundColor = "cyan"
});

