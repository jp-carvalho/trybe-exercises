const express = require('express');

const app = express();

app.use(express.json());
// app.get('/people', (req, res) => {
//   res.status(200).json('oi')
// })

module.exports = app