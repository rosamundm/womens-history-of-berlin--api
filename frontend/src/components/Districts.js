import axios from "axios";
import React, { Component, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { LOCAL_API_URL } from "../constants";
import DistrictInstance from "./District";


// ***APPROACH 2:***

const DistrictList = () => {
    const [districtList, setDistricts] = useState([]);
    const [selectedDistrict, setSelectedDistrict] = useState(null);

    useEffect(() => {
        
        (async () => {
            const response = await fetch(`${LOCAL_API_URL}districts/`, {
                method: "GET",
                headers: {
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyNzEyNjk2LCJpYXQiOjE2NDI3MDU0OTYsImp0aSI6IjM2YmRmZTU0NDQzNTQ4YzZiNjFlNjY0MDUxNDE1MDMyIiwidXNlcl9pZCI6MX0.gC5fkyyfWEC9ngglcTcBQ0RQ7p6o3IvlyUnpiJ3mnVA",
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const data = await response.json();
            setDistricts(data);
        })();
    }, []);

    return (
        <div>
                <h1>Districts</h1>
                
                {districtList.map(district => (

                <ul>
                    <li key={district.name}>

                      <Link to={`/districts/${district.slug}`}
                      onClick={() => setSelectedDistrict(district)}>
                          {district.name}
                      </Link>

                    </li>
                </ul>
                ))}

        </div>
    )
}

/*
*** APPROACH 1:***

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
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyNjI3Mzg1LCJpYXQiOjE2NDI2MjAxODUsImp0aSI6IjFiMTU3NmZkNWQ2MjRmMDg5NjAzYWI4M2YzMWUxYjhhIiwidXNlcl9pZCI6MX0.DFSIA0l-Dl5-b2g-TC_jVorBd6F06JJiTX8B54DuP6E",
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

                {districtList.map((district) => (

                  <div key={district.name}>
                    <Link to={`/districts/${district.slug}`}>
                      {district.name}
                    </Link>
                  </div>

                ))}

            </div>
        )
    }
};
*/

export default DistrictList;
