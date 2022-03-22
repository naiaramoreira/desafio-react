import React, { useState } from 'react';
import './App.css';
import Login from './components/login';
import Food from './components/food';

function App() {

  const [token, setToken] = useState('');

  const userLogin = (tok) => {
    setToken(tok);
  }

  return (
    <div className="App">
      <Food token={'9eb4c8ac82220cb0f163d798659f2aba3a56b51d'}/>
    </div>
  );
}

export default App;
