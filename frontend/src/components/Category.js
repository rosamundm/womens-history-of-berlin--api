import React, { useEffect, useState } from "react";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";
import { Link, useParams } from "react-router-dom";

function CategoryInstance() {

    let { category_slug } = useParams();
    const categorySlug = category_slug;
    const [categoryInstance, setCategoryInstance] = useState(null);
    const [selectedCategory, setSelectedCategory] = useState(null);

    const categoryInstanceURL = `${LOCAL_API_URL}categories/${categorySlug}`

    const personInstanceURL = `${LOCAL_API_URL}people/${categorySlug}`

    useEffect(() => {

        if (!categorySlug) {
            return;
        }

        (async () => {
            const response = await fetch(categoryInstanceURL, {
                method: "GET",
                headers: {
                    "Authorization": `JWT ${JWT_TOKEN}`,
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const categoryInstance = await response.json();            
            setCategoryInstance(categoryInstance);
    })();
}, [categorySlug]);

if (!categoryInstance) {
    return <div>Loading...</div>;
}

return (
    <div>
            <h2>{categoryInstance.name}</h2>
             
              <div>

                <h3>People in {categoryInstance.name}</h3>
                
                  {categoryInstance.people.map((person) => ( 
                    <div key={person.name} onClick={() => setSelectedCategory(person)}>
                        <Link to={`/districts/${districtInstance.district_slug}/${person.person_slug}`}>
                            {person.name}
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
