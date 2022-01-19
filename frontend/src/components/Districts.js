import axios from "axios";
import React, { Component } from "react";
import { Link } from "react-router-dom";
import { LOCAL_API_URL } from "../constants";

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
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyNTk5NTU3LCJpYXQiOjE2NDI1OTU5NTcsImp0aSI6IjQ4ODM4NjQ2ZWMzYzRhNDBhOGZkNmZkNDdlMDk2NWFkIiwidXNlcl9pZCI6MX0.9mIRv36-Pa5cBaf4omGp4KEOq1931j_B8H9WH1wkUR8",
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
                      to={`/districts/${district.name}`}
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
