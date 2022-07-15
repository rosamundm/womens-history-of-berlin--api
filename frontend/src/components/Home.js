import DistrictGrid from "./DistrictGrid";
import StreetSearch from "./StreetSearch";
import HomepageHeader from "./layout/HomepageHeader";

export default function HomePage() {
  return (

    <div className="landing" class="px-20 justify-center justify-self-center	max-w-4xl m-auto">

      <HomepageHeader />

        <div className="search">

          <div className="district-grid">
            <DistrictGrid />
          </div>


           <div className="street-search" class="py-10 font-sans text-center">
             <StreetSearch />
           </div>

        </div>

    </div>

  )
};