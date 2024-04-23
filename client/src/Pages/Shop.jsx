import React, { useEffect, useState } from "react";
import Navbar from "../Components/Navbar";
import { getProducts } from "../Services/product";

export const Shop = () => {
  const [products, setProducts] = useState({});
  const getdata = async () => {
    const data = await getProducts();
    setProducts(data.data);
  };
  useEffect(() => {
    getdata();
  }, []);
  return (
    <div>
      <Navbar />
      Shopping
      <div>
        {products.map((product) => {
          return (
            <div key={product._id}>
              <h1>{product.name}</h1>
              <p>{product.price}</p>
              <img src={product.image} alt={product.name} />
            </div>
          );
        })}
      </div>
    </div>
  );
};
