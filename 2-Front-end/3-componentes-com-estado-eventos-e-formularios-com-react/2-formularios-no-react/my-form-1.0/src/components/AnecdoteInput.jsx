import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AnecdoteInput extends Component {
  render() {
    const { anecdote, handleChange } = this.props;
    return (
      <label htmlFor="anecdote">
        Anedota:
        <textarea name="anecdote" id="anecdote" onChange={handleChange} value={anecdote}></textarea>
        { !anecdote ? 'A anedota precisa ser preenchida' : ''}
      </label>
    );
  }
}

AnecdoteInput.propTypes = {
  anecdote: PropTypes.string.isRequired,
  handleChange: PropTypes.func.isRequired,
};

export default AnecdoteInput;