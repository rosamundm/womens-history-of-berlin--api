import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { JWT_TOKEN, LOCAL_API_URL } from "../constants";

function CategoryList() {
    
    const [categoryList, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(null);

    useEffect(() => {
        
        (async () => {
            const response = await fetch(`${LOCAL_API_URL}categories/`, {
                method: "GET",
                headers: {
                    "Authorization": `JWT ${JWT_TOKEN}`,
                    "Accept" : "application/json", 
                    "Content-Type": "application/json"
                }
            });
            const data = await response.json();
            setCategories(data);
        })();
    }, []);

    return (
        <div>
            <h2>Categories:</h2>

            {categoryList.map((category) => (

              <div key={category.name} onClick={() => setSelectedCategory(category)}>
                <Link to={`/categories/${category.category_slug}`}>
                {category.name}
                </Link>

              </div>

            ))}

        </div>
    )
}

export default CategoryList;
