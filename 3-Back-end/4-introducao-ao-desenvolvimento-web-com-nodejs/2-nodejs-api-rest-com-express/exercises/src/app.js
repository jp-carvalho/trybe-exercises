const express = require('express');
const { read } = require('fs');
const fs = require('fs').promises;
const path = require('path');

const app = express();
app.use(express.json());

const moviesPath = path.resolve(__dirname, './movies.json');

const readFile = async () => {
  try {
    const data = await fs.readFile(moviesPath);
    return JSON.parse(data);
  } catch (error) {
    console.log(`Arquivo não pôde ser lido: ${error}`);
  }
};
//exercicio 05
app.get('/movies/:id', async (req, res) => {
  try {
    const movies = await readFile();
    const movie = movies.find(({ id }) => id === Number(req.params.id));
    res.status(200).json(movie)
  } catch (err) {
    res.status(500).send({ message: err.message });
  }
});

//exercicio 06
app.get('/movies', async (req, res) => {
  try {
    const movies = await readFile();
    res.status(200).json(movies);
  } catch (err) {
    res.status(500).send({ message: err.message });
  }
});

// exercicio 10 - Bônus
app.get('/movies/search', (req, res) => {
  try {
    const { q } = req.query;
    const movies = await readFile();

    if (q) {
      const filteredMovies = movies.filter((element) => element.movie.includes(q));
      return res.status(200).json(filteredMovies);
    }
    res.status(200).end()
  } catch (err) {
    res.status(500).send({ message: err.message })
  }
})

//exercicio 07
app.post('/movies', async (req, res) => {
  try {
    const { movie, price } = req.body;
    const movies = await readFile();
    const newMovie = {
      id: movies[movies.length - 1].id + 1,
      movie,
      price,
    };
    const allMovies = JSON.stringify([...movies, newMovie]);
    res.status(200).json(newMovie);
  } catch (err) {
    res.status(500).send({ message: err.message });
  }
})

//exercicio 08
app.put('/movies', async (req, res) => {
  try {
    //id desconstruido da requisição (parametros)
    const { id } = req.params;
    //movie e price desconstruidos do corpo da req
    const { movie, price } = req.body;
    const movies = await readFile();
    const index = movies.findIndex((element) => element.id === Number(id));
    movies[index] = { id: Number(id), movie, price };
    const updatedMovies = JSON.stringify(movies, null, 2);
    await fd.writeFile(moviesPath, updatedMovies);
    res.status(200).json(movies[index]);
  } catch (err) {
    res.status(500).send({ message: err.message });
  }
});

app.delete('/movies/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const movies = await readFile();
    const filteredMovies = movies.filter((movie) => movie.id !== Number(id));
    const updatedMovies = JSON.stringify(filteredMovies, null, 2);
    await fs.writeFile(moviesPath, updatedMovies);
    res.status(204).end();
  } catch (err) {
    res.status(500).send({ message: err.message });
  }
})

module.exports = app;