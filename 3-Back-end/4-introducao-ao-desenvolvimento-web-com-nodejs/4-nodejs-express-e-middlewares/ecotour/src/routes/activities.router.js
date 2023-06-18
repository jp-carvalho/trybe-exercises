const express = require('express');
const validateName = require('../middlewares/validateName');
const validatePrice = require('../middlewares/validatePrice')
const validateDescription = require('../middlewares/validateDescription');
const validateCreatedAt = require('../middlewares/validateCreatedAt');
const validateRating = require('../middlewares/validateRating');
const validateDifficulty = require('../middlewares/validateDifficulty');
const auth = require('../middlewares/auth');
const router = express.Router();

router.post('/activities',
  auth,
  validatePrice, 
  validateName, 
  validateDescription, 
  validateCreatedAt,
  validateRating,
  validateDifficulty,
  (req, res) => {
  res.status(201).json({ message: 'Atividade cadastrada com sucesso' });
})

module.exports = router;