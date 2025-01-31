// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes,  } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import MainSite from './components/MainSite';
import './App.css';

function App(){
  return(
    <div className='App'>
      <Router>
        <div>
        {/* nav links */}
          <Routes>
            <Route path="/" element={<LoginForm />} />
            <Route path="/register" element={<RegisterForm />} />
            <Route path="/main" element={<MainSite />} />
          </Routes>
          {/* <Footer /> */}
        </div>
      </Router>
    </div>
  );
}
export default App;

