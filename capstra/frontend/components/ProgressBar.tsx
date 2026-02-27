export default function ProgressBar({ score }: { score: number }) {
  return (
    <div className="w-full">
      <div className="mb-2 text-sm">Capital Fitness Score: {score}</div>
      <div className="h-3 w-full rounded bg-slate-700">
        <div className="h-3 rounded bg-emerald-500" style={{ width: `${score}%` }} />
      </div>
    </div>
  );
}
