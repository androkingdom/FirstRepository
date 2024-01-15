const express = require('express');
const blog = require('./router/blog')
const home = require('./router/home')

const app = express()
const port = 3000;

app.use((req , res , next)=>{
  console.log("User Entered")   //custom middleware
  next()
})

app.use(express.static("public"))
app.use('/', home)
app.use('/blog', blog)
app.use(express.static("templates"))

app.get("/contact" , (req , res) => {
    res.sendFile("templates/contact.html" , {root: __dirname})
})

// app.get("/home",(req,res)=>{
//   res.sendFile("templates/home.html",{root: __dirname})
// })

// app.get("/:slug",(req,res)=>{
//   res.send(`<h1>${req.params.slug} page</h1>`)
//   req.query = {"name":"andro","age":20}
// })

// app.get("/:slug/:slug",(req,res)=>{
//   res.send(`<h1>${req.params.slug} page</h1>`)
// })

app.listen(port, () => {
  console.log(`Server running at ${port}`);
});


