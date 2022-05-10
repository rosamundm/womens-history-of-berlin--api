import React from "react";
import Header from "./layout/Header";

function HomePage() {
  return (

    <div className="landing" class="px-20 justify-center justify-self-center	max-w-4xl m-auto">

        <div className="description">
          <p class="py-10 font-sans text-center">
            Search by district: {/* DistrictDropdown */}
              <br></br>
            Search by street: {/* StreetSearch */}
          </p>
        </div>

      </div>

  )
}

export default HomePage;
