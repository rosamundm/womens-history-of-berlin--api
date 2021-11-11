import React from "react";

const Districts = ({districts}) => {
    return (
        <div>
            <center><h1>Districts</h1></center>
            {districts.map((district) => (
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{district.name}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{district.id}</h6>
                    </div>
                </div>
            ))}
        </div>
    )
};

export default Districts;