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
  
    const csrftoken = getCookie('csrftoken'); // Obter o token CSRF dinamicamente

    try {
      // Faça uma requisição POST para a sua view do Django
      const response = await axios.post('/api/login/', { username, password }, {
        headers: {
          'X-CSRFToken': csrftoken
        }
      });
  
      // Verifique a resposta, faça algo com ela se necessário
      console.log(username, password);

    if (response.data.success) {
       // Se o login for bem-sucedido, redirecione para a página '/entrou/'
       window.location.href = '/entrou/';
     }

    } catch (error) {
      // Lide com erros de requisição, exibindo mais detalhes sobre o erro
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
