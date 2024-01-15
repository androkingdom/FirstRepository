const express = require('express');
// const ejs = require('ejs')
const app = express();
port = 3000

app.set("view engine" , "ejs")

app.get('/', (req, res) => {
    let Cname = "Andro" ;
    let name = "Andro" ;
    res.render("home" , {CompanyName : Cname , Name : name});
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`);
});
