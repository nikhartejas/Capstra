import Link from "next/link";

const modules = [
  "Market Risk Foundations",
  "Behavioral Discipline & Bias Control",
  "Capital Protection Principles",
  "Position Sizing & Loss Containment",
  "Readiness Checklist Before Exposure",
];

export default function LandingPage() {
  return (
    <main className="mx-auto max-w-5xl px-6 py-16">
      <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Capstra</p>
      <h1 className="mt-2 text-4xl font-bold text-slate-100 md:text-5xl">Education Before Exposure</h1>
      <p className="mt-6 max-w-3xl text-lg leading-relaxed text-slate-300">
        Capstra is a structured pre-market readiness platform for Indian retail participants. We
        focus on risk discipline, financial preparedness, and behavioral stability before any
        capital deployment.
      </p>

      <section className="mt-10 grid gap-6 rounded-xl border border-slate-800 bg-slate-900/40 p-6">
        <h2 className="text-xl font-semibold text-slate-100">Foundation Modules (MVP)</h2>
        <ul className="grid gap-3 text-slate-300">
          {modules.map((item) => (
            <li key={item} className="rounded-md border border-slate-800 px-4 py-3">
              {item}
            </li>
          ))}
        </ul>
      </section>

      <div className="mt-8 flex flex-wrap gap-3">
        <Link href="/dashboard" className="rounded bg-slate-100 px-5 py-3 font-medium text-slate-900">
          Open Readiness Dashboard
        </Link>
      </div>
    </main>
  );
}
