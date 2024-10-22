import "./App.css";
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CompetitionsCards from "./components/competitions/CompetitionsCards";
import SingleCompetitionPage from "./pages/SingleCompetitionPage";
import { Navbar } from "./components/Navbar";
import { TeamPage } from "./pages/TeamPage";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="App">
        <Routes>
          <Route
            exact
            path="/competetion/:code"
            element={
              <React.Fragment>
                <SingleCompetitionPage />
              </React.Fragment>
            }
          />
          <Route
            path="/"
            element={
              <React.Fragment>
                <CompetitionsCards />
              </React.Fragment>
            }
          />
          <Route
            path="/team/:teamId"
            element={
              <React.Fragment>
                <TeamPage />
              </React.Fragment>
            }
          />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
