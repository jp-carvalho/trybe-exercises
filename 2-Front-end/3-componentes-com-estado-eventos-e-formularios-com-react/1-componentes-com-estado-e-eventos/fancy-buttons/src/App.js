import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(){
    super();
    // só precisa se não for arrow function
    this.handleClickOne = this.handleClickOne.bind(this)

    this.state = {
      clickOne: 0,
      clickTwo: 0,
      clickThree: 0,
    };
  }

  handleClickOne() {
    const { clickOne } = this.state;
    this.setState((prevState) => ({
      clickOne: prevState.clickOne + 1,
    }), () => {
      console.log(`Botão 1 ${this.getButtonColor(clickOne)}`);
    })
  }
  
  handleClickTwo = () => {
    const { clickTwo } = this.state; 
    this.setState((prevState) => ({
      clickTwo: prevState.clickTwo + 1,
    }), () => {
      console.log(`Botão 2 ${this.getButtonColor(clickTwo)}`);
    })
  }
  
  handleClickThree = () => {
    const { clickThree } = this.state;
    this.setState((prevState) => ({
      clickThree: prevState.clickThree +1,
    }), () => {
      console.log(`Botão 3 ${this.getButtonColor(clickThree)}`);
    })
  }

  getButtonColor = (num) => {
    return num % 2 === 0 ? 'green' : 'white';
  }

  render(){
    const { clickOne, clickTwo, clickThree } = this.state;
    return (
      <div>
        <button onClick={ this.handleClickOne } style={{backgroundColor: this.getButtonColor(clickOne)}}>{`Cliques no primeiro: ${clickOne}`}</button>
        <button onClick={ this.handleClickTwo } style={{backgroundColor: this.getButtonColor(clickTwo)}}>{`Cliques no segundo: ${clickTwo}`}</button>
        <button onClick={ this.handleClickThree } style={{backgroundColor: this.getButtonColor(clickThree)}}>{`Cliques no terceiro: ${clickThree}`}</button>
      </div>
    );
  }
}

export default App;
