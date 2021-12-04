import axios from "axios";
import React, { Component } from "react";

class DistrictList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            districtList: []
        };
    }

    componentDidMount() {
        axios
            .get("http://127.0.0.1:8000/api/v1/districts/", {
                method: "GET",
                headers: {
                    "Authorization": "Bearer: some_token",
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                const districtList = response.data;
                this.setState({districtList});
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    render () {
        return (
                Object.keys(this.state.districtList).map(district => (
                    <ul>{district}</ul>
                ))
        )
    }

};

export default DistrictList;
