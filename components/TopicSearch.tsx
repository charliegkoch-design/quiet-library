"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { CATEGORIES, type Category } from "@/lib/curated";

export function TopicSearch() {
  const [input, setInput] = useState("");
  const [selected, setSelected] = useState<Category | null>(null);
  const router = useRouter();

  function handleCategoryClick(cat: Category) {
    setSelected(cat === selected ? null : cat);
    setInput("");
  }

  function handleInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    setInput(e.target.value);
    setSelected(null);
  }

  function handleSurpriseMe() {
    const topic = selected ?? input.trim();
    if (topic) {
      router.push(`/discover?topic=${encodeURIComponent(topic.toLowerCase())}`);
    } else {
      router.push("/discover");
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === "Enter") handleSurpriseMe();
  }

  const activeLabel = selected ?? (input.trim() || null);

  return (
    <div className="flex flex-col items-center gap-8 w-full max-w-xl">
      {/* Category pills */}
      <div className="flex flex-wrap justify-center gap-2">
        {CATEGORIES.map((cat) => (
          <button
            key={cat}
            onClick={() => handleCategoryClick(cat)}
            className={`px-4 py-1.5 rounded-full text-sm tracking-wide border transition-all duration-200 cursor-pointer ${
              selected === cat
                ? "bg-ink text-parchment border-ink"
                : "bg-transparent text-ink-muted border-border hover:border-ink-muted hover:text-ink"
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Divider */}
      <div className="flex items-center gap-4 w-full">
        <div className="flex-1 h-px bg-border" />
        <span className="text-xs text-ink-faint tracking-widest uppercase">
          or name a subject
        </span>
        <div className="flex-1 h-px bg-border" />
      </div>

      {/* Text input */}
      <input
        type="text"
        value={input}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        placeholder="fungi, Byzantine art, Stoicism…"
        className="w-full bg-transparent border-b-2 border-border focus:border-ink-muted outline-none text-center text-ink placeholder:text-ink-faint text-lg pb-2 transition-colors duration-200"
        spellCheck={false}
        autoComplete="off"
      />

      {/* Surprise Me button */}
      <button
        onClick={handleSurpriseMe}
        className="group relative px-10 py-4 bg-ink text-parchment text-base tracking-widest uppercase cursor-pointer hover:bg-accent-hover transition-colors duration-300 overflow-hidden"
        style={{ fontFamily: "var(--font-display)" }}
      >
        <span className="relative z-10">
          {activeLabel ? `Open a ${activeLabel} piece` : "Surprise Me"}
          <span className="ml-3 inline-block transition-transform duration-300 group-hover:translate-x-1">
            →
          </span>
        </span>
      </button>
    </div>
  );
}
