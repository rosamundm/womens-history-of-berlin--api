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

    const districts = districtList

    return (

        <div class="p-8 bg-violet-300">
          <div class="heading">
            <p class="text-2xl text-center">Browse by district:</p>
          </div>  
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-8">
              {districtList.map((district) => (
                <div 
                  class="p-4 bg-red-200 rounded-md flex items-center justify-center" 
                  role="none" 
                  key={district.name} 
                  onClick={() => setSelectedDistrict(district)}>   

                  <Link 
                  to={`/districts/${district.district_slug}`}>{district.name}
                  </Link>
                </div>
            ))}

            </div>
            
        </div>
            
    )
}

export default DistrictList;
