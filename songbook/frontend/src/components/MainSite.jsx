import React, { useState, useEffect } from "react";
import { Button, Container, Modal } from 'react-bootstrap';
import axios from 'axios';  // Dodanie axios do obsługi requestów HTTP
import './MainSite.css';

const MainSite = () => {

    const fetchFolders = async () => {
        try {
            const response = await axios.get('http://localhost:8000/main/get_tabs',
                { withCredentials: true }
            );
            setFolders(response.data);
        } catch (error) {
            console.error('Błąd podczas pobierania folderów:', error);
        }
    };

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
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
            const csrfToken = getCookie('csrftoken');
            const response = await axios.get('http://localhost:8000/main/is_authenticated/', {
                withCredentials: true,  // Ensure cookies are sent with the request
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            return response.data.authenticated;
            // return true;
        } catch (error) {
            console.error('Błąd podczas sprawdzania autoryzacji:', error);
            return false;
        }
    };


    // Funkcja obsługi dodania nowego folderu
    const handleSubmit = async (event) => {
        event.preventDefault();
        const isAuthenticated = await checkAuth();
        const csrfToken = getCookie('csrftoken');

        if (!isAuthenticated) {
            alert("User not logged in. Redirecting to login page.");
            window.location.href = 'http://localhost:3000';  // Redirect to login page
            return;
        }

        if (folderName.trim() === '') {
            alert("Folder name cannot be empty!");
        };  // Jeśli nazwa jest pusta, nie wysyłaj requestu

        try {
            const response = await axios.post('http://localhost:8000/main/add_tab/', {
                folderName,
            }, {
                withCredentials: true,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            console.log("RESPONSE:", response.status);
            if (response.status === 201) {
                console.log('Folder added successfully:', response.data);
                setFolderName('');  // Wyczyść pole tekstowe po zamknięciu
                fetchFolders();  // Odśwież listę folderów
            }

        } catch (error) {


            console.error('Błąd podczas dodawania folderu:', error);
        }
    };

    // Pobierz istniejące foldery z backendu po załadowaniu komponentu
    useEffect(() => {
        fetchFolders();
        // fetchFolders();
    }, []);

    return (
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
                        onClick={handleSubmit}  // Wyślij dane na backend
                        type="submit">
                        Add folder
                    </Button>
                </Modal.Footer>
            </Modal>
        </Container>
    );
};

export default MainSite;
