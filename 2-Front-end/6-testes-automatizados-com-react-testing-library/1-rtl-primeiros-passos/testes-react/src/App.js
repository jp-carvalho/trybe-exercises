// // App.js
// ABA RTL NA PRÁTICA
// import React from 'react';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <label htmlFor="id-email">
//         Email
//         <input id="id-email" type="email" />
//       </label>
//       <input id="btn-send" type="button" data-testid="id-send" value="Enviar" />
//       <input id="btn-back" type="button" value="Voltar" />
//     </div>
//   );
// }

// export default App;

// App.js
// ABA TESTANDO EVENTOS
import React, { Component } from 'react';
import ValidEmail from './ValidEmail';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      saveEmail: '',
    };
  }

  changeEmail(value) {
    this.setState({ email: value });
  }

  changeSaveEmail(value) {
    this.setState({ saveEmail: value, email: '' });
  }

  render() {
    const { email, saveEmail } = this.state;
    return (
      <div className="App">
        <label htmlFor="id-email">
          Email
          <input
            id="id-email"
            value={ email }
            type="email"
            onChange={ (event) => this.changeEmail(event.target.value) }
          />
        </label>
        <input
          id="btn-enviar"
          type="button"
          data-testid="id-send"
          value="Enviar"
          onClick={ () => this.changeSaveEmail(email) }
        />
        <input id="btn-id" type="button" value="Voltar" />
        <ValidEmail email={ saveEmail } />
      </div>
    );
  }
}

export default App;
