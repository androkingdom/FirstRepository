const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
  res.send('blog page')
})

router.get('/first-blog', (req, res) => {
  res.send('My First Blog')
})

module.exports = router