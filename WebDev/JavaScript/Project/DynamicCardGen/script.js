let number_to_view = (number) => {
    views = ``
    let strofnum = String(number)
    let lengthofnum = strofnum.length
    if (lengthofnum <= 3){
        views = strofnum
    }
    else if (lengthofnum >= 4 && lengthofnum <= 6){
        if (lengthofnum == 4){first = strofnum[0]}
        else if (lengthofnum == 5){first = strofnum.slice(0,2)}
        else if (lengthofnum == 6){first = strofnum.slice(0,3)}
        views += first
        views += "K"
        
    }
    else if (lengthofnum >= 7 && lengthofnum <= 9){
        if (lengthofnum == 7){first = strofnum[0]}
        else if (lengthofnum == 8){first = strofnum.slice(0,2)}
        else if (lengthofnum == 9){first = strofnum.slice(0,3)}
        views += first
        views += "M"
    }
    return views
}

function createCard(title, cName, views, monthsOld, duration, thumbnail_url) {
    let getContainer = document.querySelector(".container")
    console.log(getContainer)

    let box = document.createElement("div")
    box.className = "box"

    let timestamp = document.createElement("div")
    timestamp.className = "timestamp"
    timestamp.innerHTML = duration

    let thumbnail = document.createElement("div")
    thumbnail.className = "thumbnail"
    
    let image = document.createElement("img")
    image.src = thumbnail_url

    let text = document.createElement("div")
    text.className = "text"
    let text1 = document.createElement("div")
    text1.innerHTML = title
    let text2 = document.createElement("div")
    text2.innerHTML = `${cName} . ${views} views . ${monthsOld} months ago`

    getContainer.append(box)
    box.append(thumbnail)
    thumbnail.append(timestamp)
    thumbnail.append(image)
    box.append(thumbnail)
    box.append(text)
    text.append(text1)
    text.append(text2)
}
