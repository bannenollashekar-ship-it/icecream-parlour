import { useEffect, useState } from "react";
import { getDashboardData } from "../services/api";

function Dashboard() {
  const [data, setData] = useState("");

  useEffect(() => {
    getDashboardData()
      .then((res) => setData(res.data.message))
      .catch(() => alert("Error fetching data"));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Dashboard</h2>
      <p>{data}</p>
    </div>
  );
}

export default Dashboard;