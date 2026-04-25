import { useState } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();


    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const res = await api.post('/token/', { username, password });
            localStorage.setItem('access_token', res.data.access);
            localStorage.setItem('refresh_token', res.data.refresh);
            navigate('/dashboard');
        }catch (err) {
         alert('Login failed');   


    }
      
    };

    return(
        <form onSubmit={handleSubmit} className="p-8 max-w-sm mx-auto">
            <h1 className="text-2xl mb-4">SmartSeason Login</h1>
            <input
              className="border p-2 w-full mb-2" 
              placeholder="Username" 
              value={username}
              onChange={(e) => setUsername(e.target.value)} 
            />
            <input
              className="border p-2 w-full mb-2"
              type="password"
              placeholder="Password"
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
            />
            <button className="bg-green-600 text-white p-2 w-full">Login</button>

        </form>

    );
};

export default Login

    
