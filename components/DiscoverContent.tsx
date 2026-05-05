"use client";

import { useState, useEffect, useCallback } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import type { CuratedEntry } from "@/lib/curated";
import { formatVettedDate } from "@/lib/curated";

export function DiscoverContent() {
  const searchParams = useSearchParams();
  const topic = searchParams.get("topic") ?? undefined;

  const [entry, setEntry] = useState<CuratedEntry | null>(null);
  const [loading, setLoading] = useState(true);
  const [animKey, setAnimKey] = useState(0);

  const fetchEntry = useCallback(
    async (excludeId?: string) => {
      setLoading(true);
      const url = new URL("/api/discover", window.location.origin);
      if (topic) url.searchParams.set("topic", topic);
      if (excludeId) url.searchParams.set("exclude", excludeId);

      const res = await fetch(url.toString());
      const data: CuratedEntry = await res.json();
      setEntry(data);
      setAnimKey((k) => k + 1);
      setLoading(false);
    },
    [topic]
  );

  useEffect(() => {
    fetchEntry();
  }, [fetchEntry]);

  function handleDiscoverAnother() {
    fetchEntry(entry?.id);
  }

  return (
    <div className="min-h-screen bg-parchment flex flex-col">
      {/* Top bar */}
      <header className="px-8 py-6 border-b border-border">
        <Link
          href="/"
          className="text-sm text-ink-muted hover:text-ink tracking-widest uppercase transition-colors duration-200 inline-flex items-center gap-2"
        >
          <span>←</span>
          <span>The Quiet Library</span>
        </Link>
      </header>

      {/* Main content */}
      <main className="flex-1 flex items-center justify-center px-6 py-16">
        {loading && !entry ? (
          <div className="text-ink-faint tracking-widest uppercase text-sm animate-pulse">
            Finding something worth reading…
          </div>
        ) : entry ? (
          <article
            key={animKey}
            className="max-w-2xl w-full"
            style={{ animation: "fade-up 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards", opacity: 0 }}
          >
            {/* Category badge */}
            <div className="mb-8">
              <span className="text-xs tracking-widest uppercase text-accent border border-accent/40 px-3 py-1.5 rounded-full">
                {entry.category}
              </span>
            </div>

            {/* Title */}
            <h1
              className="text-4xl leading-tight text-ink mb-6"
              style={{ fontFamily: "var(--font-display)" }}
            >
              {entry.title}
            </h1>

            {/* Byline */}
            <div className="flex flex-wrap items-center gap-2 text-ink-muted text-sm mb-8">
              <span>{entry.author}</span>
              <span className="text-border">·</span>
              <span className="italic">{entry.publication}</span>
              <span className="text-border">·</span>
              <span>~{entry.readingTimeMinutes} min read</span>
            </div>

            {/* Divider */}
            <div className="h-px w-16 bg-border mb-8" />

            {/* Description */}
            <p className="text-ink leading-relaxed text-lg mb-12">
              {entry.description}
            </p>

            {/* Tags */}
            <div className="flex flex-wrap gap-2 mb-12">
              {entry.tags.map((tag) => (
                <span
                  key={tag}
                  className="text-xs text-ink-faint tracking-wide"
                >
                  #{tag}
                </span>
              ))}
            </div>

            {/* Vetted note */}
            <p className="text-xs text-ink-faint mb-10 tracking-wide">
              Human-vetted {formatVettedDate(entry.humanVettedTimestamp)}
            </p>

            {/* Actions */}
            <div className="flex flex-col sm:flex-row gap-4">
              <a
                href={entry.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex-1 flex items-center justify-center gap-3 px-8 py-4 bg-ink text-parchment tracking-widest uppercase text-sm hover:bg-accent-hover transition-colors duration-300"
                style={{ fontFamily: "var(--font-display)" }}
              >
                Open Article
                <span className="text-base">↗</span>
              </a>

              <button
                onClick={handleDiscoverAnother}
                disabled={loading}
                className="flex-1 flex items-center justify-center gap-3 px-8 py-4 border border-border text-ink-muted tracking-widest uppercase text-sm hover:border-ink-muted hover:text-ink transition-all duration-300 disabled:opacity-40 cursor-pointer"
                style={{ fontFamily: "var(--font-display)" }}
              >
                {loading ? "Finding…" : "Discover Another →"}
              </button>
            </div>
          </article>
        ) : null}
      </main>

      {/* Footer */}
      <footer className="px-8 py-6 border-t border-border">
        <p className="text-center text-xs text-ink-faint tracking-widest uppercase">
          No algorithms. No ads. Human curation only.
        </p>
      </footer>
    </div>
  );
}
