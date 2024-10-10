import React, { useEffect, useState } from "react";
import { Form, Button, Container, Alert } from 'react-bootstrap';
import axios from 'axios';
import './LoginForm.css';

const LoginForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const [isVisible, setIsVisible] = useState(false);

    useEffect(() => {
        setTimeout(()=>{
            setIsVisible(true);
        }, 10);
    });

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/logreg/sign_in/', {
                username,
                password,
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            console.log("Response data:", response.data);
            setSuccess('Login successful');
            setError('');
        } catch (err) {
            console.error("Error during login:", err);
            setSuccess('');
            setError('Invalid username or password');
        }
    };

    return (
        
        <Container className={`login-form mt-5 ${isVisible ? 'show' : ''}`}>
            <div className="content">
                <div className="logo">
                    <img src={`${process.env.PUBLIC_URL}/logo.png`} alt="HarmonyHub" />
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
                    <Button className="button" type="submit">
                        Sign In!
                    </Button>
                </Form>
                <div>
                    <a href="/" className="forgot-password">Forgot your password?</a>
                    <p>
                        Don't have an account yet? &nbsp;
                        <a href="/register" className="sign-up">
                            Sign up here!
                        </a>
                    </p>
                    
                </div>
        </div>
        </Container>
    );
};

export default LoginForm;
