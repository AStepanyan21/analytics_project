export function Table({ products }) {
  return (
    <table border="1" cellPadding="5" style={{ width: "100%", marginBottom: "30px" }}>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Discounted Price</th>
          <th>Rating</th>
          <th>Reviews</th>
        </tr>
      </thead>
      <tbody>
        {products.map((p) => (
          <tr key={p.nm_id}>
            <td>{p.name}</td>
            <td>{p.price}</td>
            <td>{p.discounted_price}</td>
            <td>{p.rating}</td>
            <td>{p.reviews_count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
