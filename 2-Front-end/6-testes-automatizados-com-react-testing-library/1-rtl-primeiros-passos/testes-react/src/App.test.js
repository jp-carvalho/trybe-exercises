import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';

// describe('Testes da aula 01 -  aba RTL na pratica', () => {
//   it('Verificando se existe um campo de email', () => {
//     render(<App />);
//     const inputEmail = screen.getByLabelText('Email');
//     expect(inputEmail).toBeInTheDocument();
//     expect(inputEmail).toHaveProperty('type', 'email');
//   })

//   it('Verifica se existem dois botões na tela', () => {
//     render(<App />);
//     const buttons = screen.getAllByRole('button');
//     expect(buttons).toHaveLength(2);
//   })

//   it('Verifica se existe um botão', () => {
//     render(<App />);
//     const buttonSend = screen.getByTestId('id-send');
//     expect(buttonSend).toBeInTheDocument();
//     expect(buttonSend).toHaveProperty('type', 'button');
//     expect(buttonSend).toHaveValue('Enviar');
//   })
// })
describe('Testes da aula 01 -  aba TESTANDO EVENTOS',  () => {
  it('Verificando se o botão e o campo email estão funcionando', async() => {
    render(<App />);

    const TEST_EMAIL = 'email@email.com';

    const testEmail = screen.getByTestId('id-email-user');
    expect(testEmail).toBeInTheDocument();
    expect(testEmail).toHaveTextContent('Valor:');

    const btnSend = screen.getByTestId('id-send');
    const inputEmail = screen.getByLabelText('Email');
    userEvent.type(inputEmail, TEST_EMAIL);
    userEvent.click(btnSend);

    await waitFor(() => {
      expect(inputEmail).toHaveValue('');
    })
    expect(testEmail).toHaveTextContent(`Valor: ${TEST_EMAIL}`);
  })
})
