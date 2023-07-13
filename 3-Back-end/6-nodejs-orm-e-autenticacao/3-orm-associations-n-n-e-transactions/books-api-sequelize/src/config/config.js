const config = {
  username: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DATABASE,
  host: process.env.MYSQL_HOST,
  dialect: 'mysql',
};

module.exports = {
  development: {...config, database: 'books_database_development'},
  test: { ...config, database: 'books_database_test'},
  production: { ...config, database: 'books_database_production'},
};
