"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { CATEGORIES, CATEGORIES_PREVIEW_COUNT, type Category } from "@/lib/curated";

export function TopicSearch() {
  const [input, setInput] = useState("");
  const [selected, setSelected] = useState<Category | null>(null);
  const [showAll, setShowAll] = useState(false);
  const router = useRouter();

  const visibleCategories = showAll
    ? CATEGORIES
    : (CATEGORIES.slice(0, CATEGORIES_PREVIEW_COUNT) as readonly Category[]);

  const hiddenCount = CATEGORIES.length - CATEGORIES_PREVIEW_COUNT;

  function handleCategoryClick(cat: Category) {
    setSelected(cat === selected ? null : cat);
    setInput("");
  }

  function handleInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    setInput(e.target.value);
    setSelected(null);
  }

  function handleSearch() {
    const q = selected ?? input.trim();
    if (q) {
      router.push(`/search?q=${encodeURIComponent(q)}`);
    }
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
    if (e.key === "Enter") handleSearch();
  }

  const activeLabel = selected ?? (input.trim() || null);

  return (
    <div className="flex flex-col items-center gap-8 w-full max-w-xl">
      {/* Category pills */}
      <div className="flex flex-col items-center gap-3 w-full">
        <div className="flex flex-wrap justify-center gap-2">
          {visibleCategories.map((cat) => (
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

        {/* See all / Show fewer toggle */}
        <button
          onClick={() => setShowAll((s) => !s)}
          className="text-xs text-ink-faint hover:text-ink-muted tracking-widest uppercase transition-colors duration-200 cursor-pointer flex items-center gap-1.5 mt-1"
        >
          {showAll ? (
            <>Show fewer <span className="text-base leading-none">↑</span></>
          ) : (
            <>See all {CATEGORIES.length} topics <span className="text-base leading-none">↓</span> <span className="text-ink-faint/50 normal-case tracking-normal">({hiddenCount} more)</span></>
          )}
        </button>
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

      {/* Action buttons */}
      <div className="flex flex-col sm:flex-row items-center gap-3 w-full justify-center">
        {/* Search button */}
        <button
          onClick={handleSearch}
          disabled={!activeLabel}
          className="group relative px-10 py-4 bg-ink text-parchment text-base tracking-widest uppercase cursor-pointer hover:bg-accent transition-colors duration-300 disabled:opacity-40 disabled:cursor-not-allowed"
          style={{ fontFamily: "var(--font-display)" }}
        >
          <span className="relative z-10">
            Search
            <span className="ml-3 inline-block transition-transform duration-300 group-hover:translate-x-1">
              ↗
            </span>
          </span>
        </button>

        {/* Surprise Me button */}
        <button
          onClick={handleSurpriseMe}
          className="group relative px-10 py-4 bg-transparent text-ink border border-border text-base tracking-widest uppercase cursor-pointer hover:border-ink-muted hover:text-accent transition-colors duration-300"
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
    </div>
  );
}
