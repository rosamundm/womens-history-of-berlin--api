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

        <div class="container p-8 bg-slate-100">
          <div className="street-title" class="p-5 text-2xl bg-sky-100">
              <a href={streetInstance.map_link}>
                {streetInstance.name}
              </a>
              <div className="eponym-basic-info" class="p-5 text-lg bg-sky-100">
                Named for {streetInstance.eponym_name}, born on {streetInstance.eponym_date_of_birth} {" "}
                in {streetInstance.eponym_place_of_birth}, {" "}
                died on {streetInstance.eponym_date_of_death} in {streetInstance.eponym_place_of_death}
              </div>
          </div>
            
          <div className="eponym-description" class="p-4">
            {streetInstance.eponym_description}
          </div>
                  
          <div className="back-to-list" class="p-2 bg-violet-300">
            <Link to={`/districts/${districtSlug}`}>
               Back to street list
            </Link>
          </div>
        
        </div>
    );
}

export default StreetInstance;
