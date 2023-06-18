const express = require('express');

const router = express.Router();

const teamsRouter = require('./teamsRouter');

router.use(teamsRouter);

module.exports = router;