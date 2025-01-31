import React, { useEffect, useState } from "react";
import { Form, Button, Container, Alert } from 'react-bootstrap';
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import './RegisterForm.css';

const RegisterForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirm_password, setConfirmPassword] = useState("");
    const [e_mail, setEmail] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const [isVisible, setIsVisible]= useState(false);

    const navigate = useNavigate();

    useEffect(()=> {
        setTimeout(()=>{
            setIsVisible(true);
        }, 10);
    });

    const handleSubmit = async (event) =>{
        event.preventDefault();

        // Form fields validation
        if (!username || !password || !confirm_password || !e_mail){
            setError('All fields are required!');
            return;
        }
        // Matching password and confirmPassword
        if (password !== confirm_password){
            setError('Passwords are not the same!');    
            return;
        }

        console.log('Dane przesyłane do backendu:', {
            username: username,
            e_mail: e_mail,
            password: password,
            confirm_password: confirm_password
        });
        // Sending data to backend
        try {
            const response = await axios.post('http://localhost:8000/logreg/sign_up/', {
                username: username,
                e_mail: e_mail,
                password: password,
                confirm_password: confirm_password
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            console.log('response data:', response.data);
            setSuccess('Register successful');
            setError('');

            setTimeout(() => {
                navigate('/');
            }, 5000)
        }catch (err){
            console.log('error:', err);
            setSuccess('');
            setError('Register error!')
        }
    };
    return (
        <Container className={`register-form mt-5 container ${isVisible ? 'show' : ''}`}>
            <div class="content">
                <div className="register-logo">
                    <img src={`${process.env.PUBLIC_URL}/logo.png`} alt="HarmonyHub" />
                    <span>
                        <p>Create your</p>
                        <p>own songbook!</p>
                    </span>
                </div>
                {success && <Alert variant="success">{success}</Alert>}
                {error && <Alert variant="danger">{error}</Alert>}
                <Form onSubmit={handleSubmit}>
                    <Form.Group controlId="formBasicUsername">
                        <Form.Control
                            type="text"
                            placeholder="Login"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </Form.Group>
                <Form.Group controlId="formBasicPassword">
                    <Form.Control
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </Form.Group>

                <Form.Group controlId="formBasicConfirmPassword">
                    <Form.Control
                        type="password"
                        placeholder="Confirm password"
                        value={confirm_password}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                    />

                <Form.Group controlId="formBasicEmail">
                    <Form.Control
                        type="email"
                        placeholder="E-mail"
                        value={e_mail}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </Form.Group>
                </Form.Group>
                <Button variant="primary" className="button" type="submit">
                    Sign Up!
                </Button>
            </Form>
                <div>
                    <span>Do you already have an account? &nbsp;</span>
                    <a href='/' className="sign-up">
                        Sign in here!
                    </a>
                </div>
            </div>
        </Container>
    );
};

export default RegisterForm;