import React, { useEffect, useState } from "react";
import { LOCAL_API_URL } from "../constants";
import { Link } from "react-router-dom";

function DistrictInstance(district) {

    const [districtInstance, setDistrictInstance] = useState(null);

    useEffect(() => {
        (async () => {
            // this fetch is where 404 comes up... but it works when replaced 
            // with districts/1, districts/2, etc.
            const response = await fetch(`${LOCAL_API_URL}districts/${district.id}`, {
                method: "GET",
                headers: {
                    // I know... I committed the token ;)
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzMTQ1MTM0LCJpYXQiOjE2NDMxMzc5MzQsImp0aSI6IjJjZDFmN2ZlMjBiMzQ3MjFiN2JmNzE1ZDZhZDVhZDVmIiwidXNlcl9pZCI6MX0.MLFj6ilCIihT8dcgSP13_4Fys-HQW5gg3O8sKYIX2-M",
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const districtInstance = await response.json();
            setDistrictInstance(districtInstance);
    })();
}, [district]);

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
