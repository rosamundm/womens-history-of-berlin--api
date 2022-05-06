import React, { useEffect, useState } from "react";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";
import { Link, useParams } from "react-router-dom";

function DistrictInstance() {

    let { district_slug, street_slug } = useParams();
    const districtSlug = district_slug;
    const streetSlug = street_slug;

    const [districtInstance, setDistrictInstance] = useState(null);
    // const [streetList, setStreets] = useState(null);

    const [selectedStreet, setSelectedStreet] = useState(null);

    const districtInstanceURL = `${LOCAL_API_URL}districts/${districtSlug}`

    useEffect(() => {

        if (!districtSlug) {
            return;
        }

        (async () => {
            const response = await fetch(districtInstanceURL, {
                method: "GET",
                headers: {
                    "Authorization": `JWT ${JWT_TOKEN}`,
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const districtInstance = await response.json();            
            setDistrictInstance(districtInstance);
    })();
}, [districtSlug]);

if (!districtInstance) {
    return <div>Loading...</div>;
}

return (
    <div>
            <h2>{districtInstance.name}</h2>
             
              <div>

                <h3>Streets in {districtInstance.name}</h3>
                
                  {districtInstance.streets.map((street) => ( 
                    <div key={street.name} onClick={() => setSelectedStreet(street)}>
                        <Link to={`/districts/${districtInstance.district_slug}/${street.street_slug}`}>
                            {street.name}
                        </Link>
                    </div>

                  ))}
                
              </div>
              
              <div className="back-to-list">
                <Link to={"/districts/"}>
                 Back to district list
                </Link>
              </div>
    
    </div>
);
}

export default DistrictInstance;
