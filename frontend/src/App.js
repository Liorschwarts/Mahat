import "./App.css";
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CompetitionsCards from "./components/competitions/CompetitionsCards";
import SingleCompetitionPage from "./pages/SingleCompetitionPage";
import { Navbar } from "./components/Navbar";
import { TeamPage } from "./pages/TeamPage";
import LoginForm from "./components/Login/LoginForm";
import SignupForm from "./components/Login/SignUp";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="App">
        <Routes>
          {/* Define your routes here */}
          <Route path="/login" element={<LoginForm />} />
          <Route path="/signup" element={<SignupForm />} />
          {/* <Route path="/home" element={<HomePage />} /> */}

          {/* Redirect from root to login page */}
          <Route path="/" element={<SignupForm />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
