import ChatMentor from "@/components/ChatMentor";
import ProgressBar from "@/components/ProgressBar";
import { getDashboard } from "@/lib/api";

const tracks = [
  {
    name: "Investor Track",
    condition: "Higher patience, risk containment, longer-horizon orientation",
  },
  {
    name: "Trader Track",
    condition: "Stronger execution discipline and tighter risk control consistency",
  },
];

export default async function DashboardPage() {
  const userId = 1;
  const dashboard = await getDashboard(userId).catch(() => ({
    capital_fitness_score: 52,
    recent_violations: [
      "Assessment data unavailable in demo mode",
      "Complete onboarding + baseline quiz to unlock recommendation",
    ],
    suggested_improvement: "Focus on risk-per-trade limits and impulsive decision control.",
  }));

  return (
    <main className="mx-auto grid max-w-5xl gap-6 px-6 py-10">
      <h2 className="text-3xl font-bold">Readiness Dashboard</h2>
      <ProgressBar score={dashboard.capital_fitness_score} />

      <section className="rounded border border-slate-700 p-4">
        <h3 className="font-semibold">Behavioral Risk Alerts</h3>
        <ul className="mt-2 list-disc pl-6 text-slate-300">
          {(dashboard.recent_violations || []).map((v: string, i: number) => (
            <li key={i}>{v}</li>
          ))}
        </ul>
        <p className="mt-3 text-slate-200">Next step: {dashboard.suggested_improvement}</p>
      </section>

      <section className="rounded border border-slate-700 p-4">
        <h3 className="font-semibold">Rule-Based Track Recommendation</h3>
        <div className="mt-3 grid gap-3 text-slate-300">
          {tracks.map((track) => (
            <div key={track.name} className="rounded border border-slate-800 p-3">
              <p className="font-medium text-slate-200">{track.name}</p>
              <p className="text-sm">{track.condition}</p>
            </div>
          ))}
        </div>
      </section>

      <ChatMentor userId={userId} />
    </main>
  );
}
