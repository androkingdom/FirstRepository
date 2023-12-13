var buss_name = ``

// Adjectives List
let Adjectives1 = "Crazy"
let Adjectives2 = "Amazing"
let Adjectives3 = "Fire"

// Shop List
let Shop1 = "Engine"
let Shop2 = "Foods"
let Shop3 = "Garments"

// Another List
let Another1 = "Bros"
let Another2 = "Limite"
let Another3 = "Hub"


var choice_maker_Adjectives = Math.floor(Math.random() * 3);
var choice_maker_Shop = Math.floor(Math.random() * 3);
var choice_maker_Another = Math.floor(Math.random() * 3);

let i = 0
var Adjectives = ""
var Shop = ""
var Another = ""

while (i < 3) {
        if (i == 0) {
                if (choice_maker_Adjectives == 0) { Adjectives = Adjectives1}
                else if (choice_maker_Adjectives == 1) {Adjectives = Adjectives2 }
                else if (choice_maker_Adjectives == 2) { Adjectives = Adjectives3}
        }
        else if (i == 1) {
                if (choice_maker_Shop== 0) { Shop = Shop1}
                else if (choice_maker_Shop == 1) {Shop = Shop2 }
                else if (choice_maker_Shop == 2) { Shop = Shop3}
        }
        else if (i == 2) {
                if (choice_maker_Shop == 0) { Another = Another1}
                else if (choice_maker_Shop == 1) {Another = Another2 }
                else if (choice_maker_Shop == 2) { Another = Another3}
        }
        i++
}

buss_name += `The ${Adjectives} ${Shop} ${Another} is coming soon!`
console.log(buss_name)