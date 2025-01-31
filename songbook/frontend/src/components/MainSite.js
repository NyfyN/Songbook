import React, { useState, useEffect } from "react";
import { Button, Container, Modal } from 'react-bootstrap';
import axios from 'axios';  // Dodanie axios do obsługi requestów HTTP
import './MainSite.css';

const MainSite = () => {
    const [showModal, setShowModal] = useState(false);
    const [folderName, setFolderName] = useState('');  // Zmienna dla inputa
    const [folders, setFolders] = useState([]);  // Zmienna do przechowywania folderów

    // Open and close modal window
    const handleShow = () => setShowModal(true);
    const handleHide = () => {
        setShowModal(false);
        setFolderName('');  // Wyczyść pole tekstowe po zamknięciu
    };

    const checkAuth = async () => {
        try {
            const response = await axios.get('http://localhost:3000/logreg/check_session/', {
                withCredentials: true  // Ensure cookies are sent with the request
            });
            // return response.data.authenticated;
            return true;
        } catch (error) {
            console.error('Błąd podczas sprawdzania autoryzacji:', error);
            return false;
        }
    };

    const getCookie = (name) => {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) {
                return value;
            }
        }
        return null; // Zwraca null, jeśli ciasteczko nie istnieje
    };



    const testSubmit = async (event) =>{
        event.preventDefault();
        const sessionId = getCookie('sessionid');
        const csrfToken = getCookie('csrftoken');
        console.log('Session ID:', sessionId);
        console.log('CSRF Token:', csrfToken);
    }

    // Funkcja obsługi dodania nowego folderu
    const handleSubmit = async (event) => {
        event.preventDefault();
        const isAuthenticated = await checkAuth();
        if (!isAuthenticated) {
            alert("User not logged in. Redirecting to login page.");
            window.location.href = 'http://localhost:3000';  // Redirect to login page
            return;
        }

        if (folderName.trim() === '') return;  // Jeśli nazwa jest pusta, nie wysyłaj requestu

        try {
            console.log("AUTH:", isAuthenticated);
            console.log("Folder name:", folderName);
            const response = await axios.post('http://localhost:8000/main/add_tab/', {
                folderName,
            }, {
                withCredentials: true
            });
            console.log("RESPONSE:",response.status);
            if (response.status === 201) {
                console.log('Folder added successfully:', response.data);
                setFolderName('');  // Wyczyść pole tekstowe po zamknięciu
                // fetchFolders();  // Odśwież listę folderów
            }

        } catch (error) {


            console.error('Błąd podczas dodawania folderu:', error);
        }
    };

    // Pobierz istniejące foldery z backendu po załadowaniu komponentu
    useEffect(() => {
        const fetchFolders = async () => {
            try {
                const response = await axios.get('get_tabs/');
                setFolders(response.data);
            } catch (error) {
                console.error('Błąd podczas pobierania folderów:', error);
            }
        };

        fetchFolders();
    }, []);

    return(
        <Container>
            <div className="side-bar">
                <div className="main-logo">
                    LOGO HERE
                </div>
                <ul className="nav flex-column">
                    <li className="nav-item">
                        <a className="nav-link active" href="#">Home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">My Songs</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">Account settings</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">Tone Finder</a>
                    </li>
                </ul>
                <div className="logout-btn">LOGOUT</div>
            </div>

            <div className="main-grid">
                {/* Wyświetlanie listy folderów */}
                {folders.map((folder, index) => (
                    <div key={index} className="folder">
                        <div className="icon"></div>
                        <p className="folder-name">{folder.name}</p>
                    </div>
                ))}
            </div>

            <Button variant='primary'
                    className="add-folder-btn"
                    onClick={handleShow}>
                +
            </Button>

            {/* Modal window */}
            <Modal className="modal" show={showModal} onHide={handleHide}>
                <Modal.Header className="header">
                    <Modal.Title>
                        New song folder
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <input 
                        type="text" 
                        placeholder="Folder name" 
                        value={folderName}
                        onChange={(e) => setFolderName(e.target.value)}  // Aktualizacja stanu inputa
                    />
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary"
                            onClick={testSubmit}  // Wyślij dane na backend
                            type="submit">
                        Add folder
                    </Button>
                </Modal.Footer>
            </Modal>
        </Container>
    );
};

export default MainSite;
