const express = require('express');

const router = express.Router();

const activitiesRouter = require('./activities.router');
const signupRouter = require('./signup.router');

router.use(activitiesRouter);
router.use(signupRouter);

module.exports = router;