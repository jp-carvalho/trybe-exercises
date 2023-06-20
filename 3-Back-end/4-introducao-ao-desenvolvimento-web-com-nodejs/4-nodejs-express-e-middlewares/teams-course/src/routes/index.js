const express = require('express');

const router = express.Router();

const teamsRouter = require('./teamsRouter');

router.use('/teams', teamsRouter);

module.exports = router;