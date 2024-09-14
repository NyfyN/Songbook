import React, { useState } from "react";
import { Form, Button, Container, Alert } from 'react-bootstrap';
import axios from 'axios';
import './LoginForm.css';

const LoginForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            // Wysyłamy dane na backend
            const response = await axios.post('http://localhost:8000/logreg/sign_in/', {
                username,
                password,
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            // Sprawdzamy, czy odpowiedź jest prawidłowa
            console.log("Response data:", response.data);

            // Ustawiamy komunikat sukcesu
            setSuccess('Login successful');
            setError('');

        } catch (err) {
            console.error("Error during login:", err); // Zaloguj błąd
            setSuccess('');
            setError('Invalid username or password');
        }
    };

    return (
        <Container className="mt-5">
            <h2>Login</h2>
            {success && <Alert variant="success">{success}</Alert>}
            {error && <Alert variant="danger">{error}</Alert>}
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formBasicUsername">
                    <Form.Label>Username</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </Form.Group>
                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Enter password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </Form.Group>
                <Button variant="primary" className="button" type="submit" >
                    Sign In
                </Button>
            </Form>
        </Container>
    );
};

export default LoginForm;
