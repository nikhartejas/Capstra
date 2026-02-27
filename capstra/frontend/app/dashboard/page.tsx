import ChatMentor from "@/components/ChatMentor";
import ProgressBar from "@/components/ProgressBar";
import { getCapital, getDashboard } from "@/lib/api";

export default async function DashboardPage() {
  const userId = 1;
  const dashboard = await getDashboard(userId).catch(() => ({ capital_fitness_score: 50, recent_violations: [], suggested_improvement: "Login to load data" }));
  const capital = await getCapital(userId).catch(() => null);

  return (
    <main className="mx-auto grid max-w-5xl gap-6 px-6 py-10">
      <h2 className="text-3xl font-bold">Discipline Dashboard</h2>
      <ProgressBar score={dashboard.capital_fitness_score} />

      <section className="rounded border border-slate-700 p-4">
        <h3 className="font-semibold">Recent Violations</h3>
        <ul className="mt-2 list-disc pl-6 text-slate-300">
          {(dashboard.recent_violations || []).map((v: string, i: number) => <li key={i}>{v}</li>)}
        </ul>
        <p className="mt-3 text-emerald-300">Suggested improvement: {dashboard.suggested_improvement}</p>
      </section>

      <section className="rounded border border-slate-700 p-4">
        <h3 className="font-semibold">Capital Allocation View</h3>
        {capital ? (
          <div className="mt-2 text-slate-300">
            <p>Capital preservation: ₹{capital.recommended_allocation.capital_preservation}</p>
            <p>Active learning trades: ₹{capital.recommended_allocation.active_learning_trades}</p>
            <p>Max risk per trade: ₹{capital.max_risk_per_trade}</p>
            <p className="mt-2 text-xs">{capital.disclaimer}</p>
          </div>
        ) : <p className="mt-2 text-slate-400">No profile loaded yet.</p>}
      </section>

      <ChatMentor userId={userId} />
    </main>
  );
}
