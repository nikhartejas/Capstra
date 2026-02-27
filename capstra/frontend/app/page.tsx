import Link from "next/link";

export default function LandingPage() {
  return (
    <main className="mx-auto max-w-4xl px-6 py-16">
      <h1 className="text-4xl font-bold">CAPSTRA</h1>
      <p className="mt-2 text-xl text-slate-300">Structure Your Capital Before You Expose It</p>
      <p className="mt-6 text-slate-300">
        AI-powered disciplined trading education for novice Indian retail traders.
      </p>
      <Link href="/dashboard" className="mt-8 inline-block rounded bg-emerald-600 px-5 py-3">
        Go to Dashboard
      </Link>
    </main>
  );
}
