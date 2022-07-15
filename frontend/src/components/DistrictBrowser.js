import DistrictGrid from "./DistrictGrid.js";
import Navbar from "./layout/Navbar";

export default function DistrictBrowser() {

    return (

        <div className="landing" class="px-500 justify-center justify-self-center max-w-4xl m-auto">

            <div className="navbar">
                <Navbar />
            </div>

            <div className="header" class="p-5 font-sans text-3xl py-10 text-center">
                Browse by district
            </div>

            <div className="district-grid" class="py-10 font-sans text-center">
                <DistrictGrid />
            </div>
        </div>
    )
};