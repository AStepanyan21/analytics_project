import React, { useEffect, useState } from "react";
import axios from "axios";
import Slider from "rc-slider";
import "rc-slider/assets/index.css";
import { Table } from "./Table";
import { PriceHistogram } from "./charts/PriceHistogram";
import { DiscountVsRating } from "./charts/DiscountVsRating";

export default function App() {
  const [products, setProducts] = useState([]);
  const [minRating, setMinRating] = useState(0);
  const [minReviews, setMinReviews] = useState(0);
  const [priceRange, setPriceRange] = useState([0, 100000]);
  const [loading, setLoading] = useState(false);

  const fetchProducts = async () => {
    setLoading(true);
    try {
      const params = {
        rating__gte: minRating,
        reviews_count__gte: minReviews,
        price__gte: priceRange[0],
        price__lte: priceRange[1],
        limit: 100,
      };
      const response = await axios.get("/api/products/", { params });
      setProducts(response.data.results || []);
    } catch (err) {
      console.error("Error fetching products", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Product Analytics</h1>

      {/* FILTERS */}
      <div className="row g-3 mb-4">
        {/* Price Range */}
        <div className="col-md-4">
          <label className="form-label">Price Range</label>
          <div className="d-flex align-items-center mb-2">
            <input
              type="number"
              className="form-control me-2"
              placeholder="Min"
              value={priceRange[0]}
              onChange={(e) => {
                const newMin = parseInt(e.target.value) || 0;
                setPriceRange([newMin, priceRange[1]]);
              }}
            />
            <input
              type="number"
              className="form-control"
              placeholder="Max"
              value={priceRange[1]}
              onChange={(e) => {
                const newMax = parseInt(e.target.value) || 0;
                setPriceRange([priceRange[0], newMax]);
              }}
            />
          </div>
          <Slider
            range
            min={0}
            max={100000}
            step={500}
            value={priceRange}
            onChange={setPriceRange}
          />
        </div>

        {/* Min Rating */}
        <div className="col-md-4">
          <label className="form-label">Min Rating</label>
          <input
            type="number"
            className="form-control"
            value={minRating}
            step="0.1"
            min="0"
            max="5"
            onChange={(e) => setMinRating(parseFloat(e.target.value))}
          />
        </div>

        {/* Min Reviews */}
        <div className="col-md-4">
          <label className="form-label">Min Reviews</label>
          <input
            type="number"
            className="form-control"
            value={minReviews}
            onChange={(e) => setMinReviews(parseInt(e.target.value))}
          />
        </div>
      </div>

      {/* Apply Filters */}
      <button
        onClick={fetchProducts}
        className="btn btn-primary mb-4"
      >
        Apply Filters
      </button>

      {/* Loading state */}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          {/* Table */}
          <Table products={products} />

          {/* Charts */}
          <div className="row mt-4">
            <div className="col-md-6">
              <PriceHistogram products={products} />
            </div>
            <div className="col-md-6">
              <DiscountVsRating products={products} />
            </div>
          </div>
        </>
      )}
    </div>
  );
}
