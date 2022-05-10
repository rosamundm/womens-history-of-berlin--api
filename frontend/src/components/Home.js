import DistrictList from "./Districts";
import Dropdown from "react-dropdown";

function HomePage() {
  return (

    <div className="landing" class="px-20 justify-center justify-self-center	max-w-4xl m-auto">

        <div className="search">

          <div className="district-search" class="py-10 font-sans text-center">
            Select a district:
            <DistrictList />
          </div>

          <div className="street-search" class="py-10 font-sans text-center"></div>
            Search by street: 
            {/* StreetSearch */}
          </div>

    </div>

  )
}

export default HomePage;
