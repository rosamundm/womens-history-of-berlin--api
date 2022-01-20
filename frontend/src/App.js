import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import AboutPage from "./components/About.js";
import DistrictInstance from "./components/District.js";
import DistrictList from "./components/Districts.js";
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
              <Route path="/districts/:slug" element={<DistrictInstance/>}/>

            </Routes>
          </Router>
              
          <Footer/>

        </div>





      )
    }
};

export default App;



