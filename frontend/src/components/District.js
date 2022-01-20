import React, { useEffect, useState } from "react";
import { useParams} from "react-router";
import { Link } from "react-router-dom";
import { LOCAL_API_URL } from "../constants";

const DistrictInstance = ({district}) => {
    const [districtInstance, setDistrictInstance] = useState(null);

    // const districtID = useParams();

    useEffect(() => {
        (async () => {
            const response = await fetch(`${LOCAL_API_URL}districts/${district.id}`, {
                method: "GET",
                headers: {
                    "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyNzEyNjk2LCJpYXQiOjE2NDI3MDU0OTYsImp0aSI6IjM2YmRmZTU0NDQzNTQ4YzZiNjFlNjY0MDUxNDE1MDMyIiwidXNlcl9pZCI6MX0.gC5fkyyfWEC9ngglcTcBQ0RQ7p6o3IvlyUnpiJ3mnVA",
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
        {districtInstance && (
            <> {/* stands for React.Fragment */}
              <ul>
                  <li>Name: {districtInstance.name}</li>
                  <li>Slug: {districtInstance.slug}</li>
              </ul>

              <Link to={"/districts/"}>
               Back to list
            </Link>
            </>
        )}
    </div>
);

}


/*
function DistrictInstance(props) {

    let { name } = this.props.district.name;

    return (
        <div>
            <h1 key={name}>District: {name}</h1>

            <Link to={"/districts/"}>
               Back to list
            </Link>
        </div>
    );
}
*/

export default DistrictInstance;
