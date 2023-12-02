StartOrNot = confirm("RockPaperScissor\n--------------------\nCommand :-\n1. Rock\n2. Paper\n3.Scissor\n--------------------\nClick 'OK' To Start The Game")

if (StartOrNot == true){
    let npc = (Math.floor(Math.random() * 3)) + 1
    let meaning = {1:"Rock" ,2:"Paper",3:"Scissor"}
    let UserCondition = {
        1:{1:"Draw",2:"Loss",3:"Win"},
        2:{2:"Draw",3:"Loss",1:"Win"},
        3:{3:"Draw",1:"Loss",2:"Win"}
    }
    
    let User = prompt("Enter Your Choice")
    if ((User.length) != 1){
        confirm("Enter Vaild Command")
    }

    let result = UserCondition[User][npc]
    confirm(`User : ${meaning[User]}\nComputer : ${meaning[npc]}\nResult : ${result}`)
}


