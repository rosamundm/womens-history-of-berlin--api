import axios from "axios";
import React, { Component } from "react";
import { Link } from "react-router-dom";

const LOCAL_API_URL = "http://localhost:8000/api/v1/"

class DistrictList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            districtList: []
        };
    }

    componentDidMount() {
        axios
            .get(`${LOCAL_API_URL}districts/`, {
                method: "GET",
                headers: {
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMjgxMTg0LCJpYXQiOjE2NDIyNzc1ODQsImp0aSI6ImEzNjQyZjhjYTg1YjQ5ZTJhMTI5Y2FiMTY5ZDNjYjk0IiwidXNlcl9pZCI6MX0.D7uMSdxjQ4iIfss_nGIqTH909h4FLV9YUn04Z8uxhtk",
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

                {districtList.map((district, i) => (
                  <div>
                    <Link
                      key={i}
                      to={`/districts/${district.name}`.toLowerCase()}
                    >
                      {district.name}
                    </Link>
                  </div>
                ))}
                
            </div>
        )
    }
};

export default DistrictList;
