import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export function PriceHistogram({ products }) {
  const ranges = [
    [0, 1000],
    [1000, 5000],
    [5000, 10000],
    [10000, 20000],
    [20000, 50000],
    [50000, 100000],
  ];

  const data = ranges.map(([min, max]) => {
    const count = products.filter((p) => p.price >= min && p.price < max).length;
    return {
      name: `${min}-${max}`,
      count,
    };
  });

  return (
    <>
      <h3>Price Histogram</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Bar dataKey="count" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </>
  );
}
