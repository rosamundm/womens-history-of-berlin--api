import React, { useEffect, useState } from "react";
import { LOCAL_API_URL } from "../constants";
import { Link, useParams } from "react-router-dom";

function DistrictInstance() {

    let params = useParams();
    const districtID = params.id;

    const [districtInstance, setDistrictInstance] = useState(null);

    useEffect(() => {

        if (!districtID) {
            return;
        }

        (async () => {
            const response = await fetch(`${LOCAL_API_URL}districts/${districtID}`, {
                method: "GET",
                headers: {
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzODM0NTgxLCJpYXQiOjE2NDM4MjczODEsImp0aSI6ImFlOGNhYzE1YzhhMjRiZTY5NGQ4ZTk1OWYyNjNiYmYyIiwidXNlcl9pZCI6MX0._EcZNg9qz2hxSujEOSlutyoPJKNGsy-QBWZALmK3qlQ",
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const districtInstance = await response.json();            
            setDistrictInstance(districtInstance);
    })();
}, [districtID]);

if (!districtInstance) {
    return <div>Loading...</div>;
}

return (
    <div>
            <h2>District: {districtInstance.name}</h2>

              <div>
                  Slug: {districtInstance.slug}
              </div>

              <div>
                <Link to={"/districts/"}>
                 Back to list
                </Link>
              </div>
    </div>
);
}

export default DistrictInstance;
