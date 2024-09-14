import React, { useState } from "react";
import { Form, Button, Container, Alert } from 'react-bootstrap';
import axios from 'axios';

const RegisterForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirm_password, setConfirmPassword] = useState("");
    const [e_mail, setEmail] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");

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
        }catch (err){
            console.log('error:', err);
            setSuccess('');
            setError('Register error!')
        }
    };
    return (
        <Container className="mt-5">
            <h2>Register</h2>
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
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="email"
                        placeholder="Enter email"
                        value={e_mail}
                        onChange={(e) => setEmail(e.target.value)}
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
                <Form.Group controlId="formBasicConfirmPassword">
                    <Form.Label>Confirm Password</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Confirm password"
                        value={confirm_password}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                    />
                </Form.Group>
                <Button variant="primary" className="button" type="submit">
                    Register
                </Button>
            </Form>
        </Container>
    );
};

export default RegisterForm;