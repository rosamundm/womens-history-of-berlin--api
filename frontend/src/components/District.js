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
            // this fetch is where 404 comes up... but it works when replaced 
            // with districts/1, districts/2, etc.
            const response = await fetch(`${LOCAL_API_URL}districts/${districtID}`, {
                method: "GET",
                headers: {
                    // I know... I committed the token ;)
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzNzQ3NDc3LCJpYXQiOjE2NDM3NDAyNzcsImp0aSI6ImZmMDBjZDZmNmM4NjQyZTRhMTEzNmYwNGMwMjRhNDcxIiwidXNlcl9pZCI6MX0.d1DbxodnNZMQvQM1wVAlhG4omP4R9Tbzmd8gy0vECrs",
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
