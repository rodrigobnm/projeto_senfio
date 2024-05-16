import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
<<<<<<< Updated upstream
=======
import senfioLogo from './Senfio-White.png'; 
import axios from 'axios';

const csrftoken = getCookie('csrftoken');
console.log(csrftoken); 

// Função para obter o valor do cookie
function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}
>>>>>>> Stashed changes

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
<<<<<<< Updated upstream
    
    try {
      const response = await axios.post('/login/', {
        username: email,
        password: password
      });
      
      if (response.data.success) {
        // Login bem-sucedido
        window.location.href = '/entrou'; // Redirecionar para a página de sucesso
      } else {
        // Exibir mensagem de erro
        setError(response.data.message);
      }
    } catch (error) {
      // Exibir mensagem de erro genérico
      setError('Ocorreu um erro ao fazer login. Por favor, tente novamente mais tarde.');
=======
  
    try {
      // Faça uma requisição POST para a sua view do Django

      const response = await axios.post('/api/login/', { username, password }, {
        headers: {
          'X-CSRFToken': csrftoken
        }
      });
  
      // Verifique a resposta, faça algo com ela se necessário
      console.log(username, password);
    } catch (error) {
      // Lide com erros de requisição, exibindo mais detalhes sobre o erro
      console.error('Erro ao fazer login:', error.response.data);
>>>>>>> Stashed changes
    }
  };

  return (
    <div className="App" id="box">
      <h1>LOGIN</h1>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" value={email} onChange={handleEmailChange} />
        <input type="password" placeholder="Password" value={password} onChange={handlePasswordChange} />
        <button type="submit">Login</button>
      </form>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default App;
