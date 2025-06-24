import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export function DiscountVsRating({ products }) {
  const data = products.map((p) => ({
    rating: p.rating,
    discount: p.price - p.discounted_price,
  }));

  return (
    <>
      <h3>Discount vs Rating</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="rating" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="discount" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>
    </>
  );
}
