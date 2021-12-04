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
                    "Authorization": "JWT <access_token>",
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                this.setState({ districtList: response.data});
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    render () {
        const districtList = this.state.districtList;

        return (
            <div>
                {districtList.map((district, i) => (
                    <ul key={i}>{district.name}</ul>
                ))}
            </div>
        )
    }
};

export default DistrictList;
