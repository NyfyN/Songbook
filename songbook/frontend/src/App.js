// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, useLocation } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
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
          </Routes>
          <Footer />
        </div>
      </Router>
    </div>
  );
}

function Footer(){
  const location = useLocation();

  return (
    <footer>
      {location.pathname == "/" ? (
        <p>Don't have an account? <Link to="/register"> Sign Up </Link>here!</p>
      ):(
        <p>Already have an account? <Link to="/"> Sign In </Link>here!</p>      )}
    </footer>
  );
}
export default App;
// function App() {
//   return (
//     <div className="App">
//       <LoginForm />
//     </div>
//   );
// }

// export default App;
