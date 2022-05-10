import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import AboutPage from "./components/About.js";
import DistrictInstance from "./components/District.js";
import DistrictList from "./components/Districts.js";
import StreetInstance from "./components/Street.js";
import Footer from "./components/layout/Footer.js";
import Header from "./components/layout/Header.js";
import HomePage from "./components/Home.js";

class App extends Component {

    render() {

      return (

          <main className="text-indigo-800 bg-teal-100 body-font min-h-screen">

            <Header/>  

            <Router>
              <Routes>

                <Route path="/" element={<HomePage/>}/>
                <Route path="/about" element={<AboutPage/>}/>

                <Route path="/districts" element={<DistrictList/>}/>
                <Route path="/districts/:district_slug" element={<DistrictInstance/>}/>
                <Route path="/districts/:district_slug/:street_slug" element={<StreetInstance/>}/>

              </Routes>
            </Router>
              
            <Footer/>

          </main>

      )
    }
};

export default App;



