import React from 'react';
import { render, screen } from '@testing-library/react';
import ValidEmail from './ValidEmail';

it('Testando um componente, caso o emailo seja válido', () => {
  const EMAIL_USER = 'email@email.com';
  render(<ValidEmail email={ EMAIL_USER } />);
  const isValid = screen.getByText(/email válido/i);
  expect(isValid).toBeInTheDocument();
})

it('Testando um componente, caso o email seja inválido', () => {
  const EMAIL_USER = 'emailerrado';
  render(<ValidEmail email={ EMAIL_USER } />);
  const isValid = screen.getByText(/email inválido/i);
  expect(isValid).toBeInTheDocument();
})

it('Testando se o componente não aparece caso o campo email esteja vazio', () => {
  render(<ValidEmail email="" />);
  const isValidText = screen.queryByTestId('id-is-email-valid');
  expect(isValidText).not.toBeInTheDocument();
})

it('Testando se o componente possui texto verde ao ser digitado um email válido', () => {
  const EMAIL_USER = 'email@email.com';

  render(<ValidEmail email={ EMAIL_USER } />);
  const isValidText = screen.getByTestId('id-is-email-valid');
  expect(isValidText).toHaveAttribute('class', 'green-text');
})

it('Testando se o componente possui texto vermelho ao ser digitado email inválido', () => {
  const EMAIL_USER = 'emailerrado';

  render(<ValidEmail email={ EMAIL_USER } />);
  const isValidText = screen.getByTestId('id-is-email-valid');
  expect(isValidText).toHaveAttribute('class', 'red-text');
})