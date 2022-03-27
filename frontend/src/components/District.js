import React, { useEffect, useState } from "react";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";
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
                    "Authorization": `JWT ${JWT_TOKEN}`,
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
