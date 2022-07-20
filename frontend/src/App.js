import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AboutPage from "./components/About.js";
import DistrictBrowser from "./components/DistrictBrowser.js";
import DistrictInstance from "./components/District.js";
import StreetInstance from "./components/Street.js";
import HomePage from "./components/Home.js";

export default function App() {

      return (

          <main className="text-indigo-800 bg-teal-100 body-font min-h-screen flex items-center justify-center">

            <Router>
              <Routes>

                <Route path="/" element={<HomePage/>}/>
                <Route path="/about" element={<AboutPage/>}/>

                <Route path="/districts" element={<DistrictBrowser/>}/>
                <Route path="/districts/:district_slug" element={<DistrictInstance/>}/>
                <Route path="/districts/:district_slug/:street_slug" element={<StreetInstance/>}/>

              </Routes>
            </Router>
              
            { /* <Footer/> */ }

          </main>

      )
};
