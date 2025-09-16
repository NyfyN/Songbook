import React, { useEffect, useState } from "react";
import { Form, Button, Container, Alert } from 'react-bootstrap';
import axios from 'axios';
import './LoginForm.css';
import { useNavigate } from "react-router-dom";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

const LoginForm = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const [isVisible, setIsVisible] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        setTimeout(() => {
            setIsVisible(true);
        }, 10);
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const csrfToken = getCookie('csrftoken');
            const response = await axios.post('http://localhost:8000/logreg/sign_in/', {
                username,
                password,
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                withCredentials: true  // Ensure cookies are sent with the request
            });

            console.log("Response data:", response.data);
            setSuccess('Login successful');
            setError('');
            setTimeout(() => {
                navigate('/main');
            }, 1000);
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
                    <img src={`/logo.png`} alt="HarmonyHub" />
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