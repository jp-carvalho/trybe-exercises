// REPOSITORIO TRYBE
// https://github.com/tryber/sd-029-b-exercise-frontend-content

import React from 'react';
import './App.css';
import Header from './Header';
import Content from './Content';
import Footer from './Footer';

class App extends React.Component {
  render() {
    return (
      <>
        <Header />
        <Content />
        <Footer />
      </>
    );
  }
}

export default App;
