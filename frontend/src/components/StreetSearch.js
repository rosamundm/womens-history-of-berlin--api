import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";

function StreetSearch() {

  const [data, setData] = useState([]);  // fetched data
  const [searchQuery, setSearchQuery] = useState(""); // value of search field

  const fetchData = () => {
    fetch(`${LOCAL_API_URL}streets/`, {
      method: "GET",
      headers: {
        "Authorization": `JWT ${JWT_TOKEN}`,
        "Accept" : "application/json", 
        "Content-Type": "application/json"
      }
    })
      .then((response) => response.json())
      .then((result) => setData(result))
      .catch((error) => console.log("Error fetching data"))
  };

  useEffect(() => {
    fetchData();
  }, []);

  function handleChange(event) {
    setSearchQuery(event.target.value);
  }

  return (
      <div className="flex items-center justify-center">
        <div className="flex border-2 rounded">
          <input 
            type="text" 
            className="px-4 py-2 w-80" 
            placeholder="Search by street"
            value={searchQuery}
            onChange={handleChange}
          >
          </input>

          <div>
            {data &&
              data.map((item) =>(
                item.name.toLowerCase().slice(0,3) === searchQuery.slice(0,3)
                ? <Link 
                    to={`/districts/${item.district.district_slug}/${item.street_slug}`}>{item.name}
                </Link>
                : null
              ))
            }


          </div>
        </div>
      </div>
  )
};

export default StreetSearch;