import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";

function PersonInstance() {

    let { street_slug, person_slug } = useParams();
    const streetSlug = street_slug;
    const personSlug = person_slug;
    
    const [personInstance, setPerson] = useState([]);
    const [selectedPerson, setSelectedPerson] = useState(null);

    useEffect(() => {
        
        (async () => {
            const response = await fetch(`${LOCAL_API_URL}people/${personSlug}`, {
                method: "GET",
                headers: {
                    "Authorization": `JWT ${JWT_TOKEN}`,
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const personInstance = await response.json();
            setPerson(personInstance);
        })();
    }, [personSlug]);

    return (
        <div>
                <h2>{personInstance.name}</h2>
                 
                  <div>
                    <strong>Street:</strong> {personInstance.street}
                    <br></br>
                    <strong>Born:</strong> {personInstance.date_of_birth} in {personInstance.place_of_birth}
                    <br></br>
                    <strong>Died:</strong> {personInstance.date_of_death} in {personInstance.place_of_death}
                    <br></br>
                    <strong>Category:</strong> {personInstance.category}                              
                  </div>
                  
                  {/*
                  <div className="back-to-list">
                    <Link to={`/districts/${districtSlug}`}>
                     Back to street list
                    </Link>
                  </div>
                  */}
        
        </div>
    )
}

export default PersonInstance;
