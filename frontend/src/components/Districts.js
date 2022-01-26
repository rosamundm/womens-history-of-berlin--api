import React, { Component, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { LOCAL_API_URL } from "../constants";
import DistrictInstance from "./District";

function DistrictList() {
    
    const [districtList, setDistricts] = useState([]);
    const [selectedDistrict, setSelectedDistrict] = useState(null);

    useEffect(() => {
        
        (async () => {
            const response = await fetch(`${LOCAL_API_URL}districts/`, {
                method: "GET",
                headers: {
                    // I know... I committed the token ;)
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzMTQ1MTM0LCJpYXQiOjE2NDMxMzc5MzQsImp0aSI6IjJjZDFmN2ZlMjBiMzQ3MjFiN2JmNzE1ZDZhZDVhZDVmIiwidXNlcl9pZCI6MX0.MLFj6ilCIihT8dcgSP13_4Fys-HQW5gg3O8sKYIX2-M",
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
            <h2>Districts:</h2>

            {districtList.map((district) => (

              <div key={district.name} onClick={() => setSelectedDistrict(district)}>
                <Link to={`/districts/${district.slug}`}>
                {district.name}
                </Link>

              </div>

            ))}

            <DistrictInstance district={selectedDistrict} />

            {
            /* returns null: */
            console.log(selectedDistrict)
            } 

        </div>
    )
}

export default DistrictList;
