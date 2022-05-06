import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import AboutPage from "./components/About.js";
import PersonInstance from "./components/Person.js";
import DistrictInstance from "./components/District.js";
import DistrictList from "./components/Districts.js";
import StreetInstance from "./components/Street.js";
import Footer from "./components/layout/Footer.js";
import Header from "./components/layout/Header.js";
import HomePage from "./components/Home.js";

class App extends Component {

    render() {

      return (

        <div>
          <Header/>  

          <Router>
            <Routes>

              <Route path="/" element={<HomePage/>}/>
              <Route path="/about" element={<AboutPage/>}/>

              <Route path="/districts" element={<DistrictList/>}/>
              <Route path="/districts/:district_slug" element={<DistrictInstance/>}/>
              <Route path="/districts/:district_slug/:street_slug" element={<StreetInstance/>}/>

              <Route path="/person/:person_slug" element={<PersonInstance/>}/>

            </Routes>
          </Router>
              
          <Footer/>

        </div>

      )
    }
};

export default App;



