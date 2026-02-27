const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function getDashboard(userId: number) {
  const res = await fetch(`${API_BASE}/dashboard/${userId}`, { cache: "no-store" });
  return res.json();
}

export async function getCapital(userId: number) {
  const res = await fetch(`${API_BASE}/capital/structure/${userId}`, { cache: "no-store" });
  return res.json();
}
