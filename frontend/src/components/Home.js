// import DistrictList from "./Districts";
import Dropdown from "react-dropdown";
import DistrictList from "./Districts";
import StreetSearch from "./StreetSearch";

function HomePage() {
  return (

    <div className="landing" class="px-20 justify-center justify-self-center	max-w-4xl m-auto">

        <div className="search">

          <div className="district-list">
            <DistrictList />
          </div>


           <div className="street-search" class="py-10 font-sans text-center">
             <StreetSearch />
           </div>

        </div>



    </div>

  )
}

export default HomePage;
