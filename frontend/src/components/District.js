import React from "react";
import { useParams} from "react-router";
import { Link } from "react-router-dom";

const DistrictInstance = () => {

    let { id } = useParams();

    return (
        <div>
            <h1>District: {id}</h1>

            <Link to={"/districts/"}>
               Back to list
            </Link>
        </div>
    );
}

export default DistrictInstance
