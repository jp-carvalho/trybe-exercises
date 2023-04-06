import React from 'react';
import Image from './Image';
import staringCat from './images/staringCat.jpg'

function App() {
  return (
    <Image source={ staringCat } alternativeText="Cute cat staring"/>
  );
}

export default App;
