import React, { useEffect, useState } from "react";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";
import { Link, useParams } from "react-router-dom";

function StreetInstance() {

    let { district_slug, street_slug } = useParams();
    const districtSlug = district_slug;
    const streetSlug = street_slug;

    const [streetInstance, setStreetInstance] = useState(null);

    const streetInstanceURL = `${LOCAL_API_URL}districts/${districtSlug}/streets/${streetSlug}`

    useEffect(() => {

        if (!streetSlug) {
            return;
        }

        (async () => {
            const response = await fetch(streetInstanceURL, {
                method: "GET",
                headers: {
                    "Authorization": `JWT ${JWT_TOKEN}`,
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const streetInstance = await response.json();
            setStreetInstance(streetInstance);
    })();
    }, [streetSlug]);

    if (!streetInstance) {
        return <div>Loading...</div>;
    }

    return (
        <div>
                <h2>{streetInstance.name}</h2>
                 
                  <div>
                    <strong>District:</strong> {streetInstance.district}
                    <br></br>
                    <strong>Eponym:</strong> {streetInstance.eponym}                       
                  </div>
                  
                  <div className="back-to-list">
                    <Link to={`/districts/${districtSlug}`}>
                     Back to street list
                    </Link>
                  </div>
        
        </div>
    );
}

export default StreetInstance;
