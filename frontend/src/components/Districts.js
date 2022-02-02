import React, { useEffect, useState } from "react";
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
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzODM0NTgxLCJpYXQiOjE2NDM4MjczODEsImp0aSI6ImFlOGNhYzE1YzhhMjRiZTY5NGQ4ZTk1OWYyNjNiYmYyIiwidXNlcl9pZCI6MX0._EcZNg9qz2hxSujEOSlutyoPJKNGsy-QBWZALmK3qlQ",
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
                <Link to={`/districts/${district.id}`}>
                {district.name}
                </Link>

              </div>

            ))}

        </div>
    )
}

export default DistrictList;
