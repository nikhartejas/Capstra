"use client";

import { useState } from "react";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function ChatMentor({ userId }: { userId: number }) {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const send = async () => {
    const res = await fetch(`${API_BASE}/mentor/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, message }),
    });
    const data = await res.json();
    setReply(data.response || data.detail);
  };

  return (
    <div className="rounded border border-slate-700 p-4">
      <h3 className="mb-2 text-lg font-semibold">Chat Mentor</h3>
      <textarea
        className="w-full rounded bg-slate-900 p-2"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask about discipline and capital structure"
      />
      <button className="mt-2 rounded bg-indigo-600 px-4 py-2" onClick={send}>Send</button>
      {reply && <p className="mt-3 whitespace-pre-wrap text-sm text-slate-200">{reply}</p>}
    </div>
  );
}
