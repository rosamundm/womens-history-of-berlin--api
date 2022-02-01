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
                    // I know... I committed the token ;)
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQ3NDc3LCJpYXQiOjE2NDM3NDAyNzcsImp0aSI6ImZmMDBjZDZmNmM4NjQyZTRhMTEzNmYwNGMwMjRhNDcxIiwidXNlcl9pZCI6MX0.d1DbxodnNZMQvQM1wVAlhG4omP4R9Tbzmd8gy0vECrs",
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

            <DistrictInstance district={selectedDistrict} />

            {
            /* returns null: */
            console.log(selectedDistrict)
            } 

        </div>
    )
}

export default DistrictList;
