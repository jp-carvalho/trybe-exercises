const teams = require('../utils/teams');

const existingId = (req, res, next) => {
  const id = Number(req.params.id);
  const checkedId = teams.some((t) => t.id === id);
  if ( !checkedId ) return res.status(404).json({ message: 'Time não encontrado'});
  next();
}

module.exports = existingId;