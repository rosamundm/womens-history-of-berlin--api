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
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMjY4NTU1LCJpYXQiOjE2NDIyNjQ5NTUsImp0aSI6Ijk1ZWZkOTM5ZDNmNTQ1MmZiZDhjYzRlNzFmYzZiMzlhIiwidXNlcl9pZCI6MX0.6ZiDlu-uiIIlZs_WacbQCLn7Vsen1z3dEHahQ0VOpT0",
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
                <h1>Districts</h1>
                <span>Render data here:</span>
                {districtList.map((district, i) => (
                    <ul key={i}>{district.name}</ul>
                ))}
            </div>
        )
    }
};

export default DistrictList;
