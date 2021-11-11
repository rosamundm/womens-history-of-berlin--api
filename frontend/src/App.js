import React, { Component } from "react";
import Districts from "./components/Districts.js";

class App extends Component {
    render() {
      return (
          <Districts districts={this.state.districts} />
      )
    }

    state = {
      districts: []
    };
  
    componentDidMount(res) {
      const token = "xyz";
      fetch("http://127.0.0.1:8000/api/v1/districts/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Authorization": `JWT ${token}`
        }
      }    
      )
        .then((data) => {
          this.setState({ districts: data })
        })
        .catch(console.log)
    }
}

export default App;



