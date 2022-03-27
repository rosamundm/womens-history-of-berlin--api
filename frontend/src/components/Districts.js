import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";

function DistrictList() {
    
    const [districtList, setDistricts] = useState([]);
    const [selectedDistrict, setSelectedDistrict] = useState(null);

    useEffect(() => {
        
        (async () => {
            const response = await fetch(`${LOCAL_API_URL}districts/`, {
                method: "GET",
                headers: {
                    "Authorization": `JWT ${JWT_TOKEN}`,
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
