import React, { useState } from 'react';
import './App.css';
import senfioLogo from './Senfio-White.png'; 
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const csrftoken = getCookie('csrftoken'); 

    try {
      const response = await axios.post('http://localhost:8000/api/login/', { username, password }, {
        headers: {
          'X-CSRFToken': csrftoken
        }
      });
      
      console.log(username, password);

    if (response.data.success) {
       window.location.href = '/home/';
     }else{
      document.getElementById('erro').innerText = 'Credenciais Inválidas, Tente novamente!';
     }

    } catch (error) {
      console.error('Erro ao fazer login:', error.response.data);
    }
  };

  return (
    <div className="App" id="box">
      <h1>LOGIN</h1>
      <img src={senfioLogo} id="imagem_logo" alt="Senfio"/>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" name="username" value={username} onChange={handleUsernameChange} />
        <input type="password" placeholder="Password" name="password" value={password} onChange={handlePasswordChange} />
        <button type="submit">Login</button>
        <h3 id='erro'></h3>
      </form>
    </div>
  );
}

export default App;

// Função para obter o valor do cookie
function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}
