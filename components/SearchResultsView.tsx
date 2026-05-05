"use client";

import Link from "next/link";
import type { SearchResults, WebResult } from "@/lib/search";
import type { CuratedEntry } from "@/lib/curated";
import { formatVettedDate } from "@/lib/curated";

interface Props {
  query: string;
  results: SearchResults;
}

function CuratedCard({ entry }: { entry: CuratedEntry }) {
  return (
    <a
      href={entry.url}
      target="_blank"
      rel="noopener noreferrer"
      className="group flex flex-col gap-3 p-6 border border-border hover:border-ink-muted transition-all duration-200 bg-parchment hover:bg-parchment-mid"
    >
      <div className="flex items-center justify-between gap-3">
        <span className="text-xs tracking-widest uppercase text-accent border border-accent/40 px-2.5 py-1 rounded-full">
          {entry.category}
        </span>
        <span className="text-xs text-ink-faint tracking-wide flex items-center gap-1.5">
          <span className="inline-block w-1.5 h-1.5 rounded-full bg-accent/60" />
          Human Vetted
        </span>
      </div>

      <h3
        className="text-xl leading-snug text-ink group-hover:text-accent transition-colors duration-200"
        style={{ fontFamily: "var(--font-display)" }}
      >
        {entry.title}
      </h3>

      <p className="text-sm text-ink-muted leading-relaxed line-clamp-2">
        {entry.description}
      </p>

      <div className="flex items-center gap-2 text-xs text-ink-faint mt-auto pt-1">
        <span>{entry.author}</span>
        <span>·</span>
        <span className="italic">{entry.publication}</span>
        <span>·</span>
        <span>~{entry.readingTimeMinutes} min</span>
        <span className="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
          Open ↗
        </span>
      </div>
    </a>
  );
}

function WebCard({ result }: { result: WebResult }) {
  return (
    <a
      href={result.url}
      target="_blank"
      rel="noopener noreferrer"
      className="group flex flex-col gap-3 p-6 border border-border/60 hover:border-border transition-all duration-200 bg-parchment/50 hover:bg-parchment"
    >
      <div className="flex items-center justify-between gap-3">
        <span className="text-xs tracking-widest uppercase text-ink-muted border border-border px-2.5 py-1 rounded-full">
          {result.publication}
        </span>
        <span className="text-xs text-ink-faint tracking-wide flex items-center gap-1.5">
          <span className="inline-block w-1.5 h-1.5 rounded-full bg-ink-faint/60" />
          Quality Source
        </span>
      </div>

      <h3
        className="text-xl leading-snug text-ink group-hover:text-accent transition-colors duration-200"
        style={{ fontFamily: "var(--font-display)" }}
      >
        {result.title}
      </h3>

      {result.description && (
        <p className="text-sm text-ink-muted leading-relaxed line-clamp-2">
          {result.description}
        </p>
      )}

      <div className="flex items-center gap-2 text-xs text-ink-faint mt-auto pt-1">
        <span className="italic">{result.publication}</span>
        <span className="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
          Open ↗
        </span>
      </div>
    </a>
  );
}

export function SearchResultsView({ query, results }: Props) {
  const { curated, web, webEnabled } = results;
  const totalResults = curated.length + web.length;

  return (
    <div className="min-h-screen bg-parchment flex flex-col">
      {/* Header */}
      <header className="px-8 py-6 border-b border-border">
        <Link
          href="/"
          className="text-sm text-ink-muted hover:text-ink tracking-widest uppercase transition-colors duration-200 inline-flex items-center gap-2"
        >
          <span>←</span>
          <span>The Quiet Library</span>
        </Link>
      </header>

      <main className="flex-1 px-6 py-12 max-w-4xl mx-auto w-full">
        {/* Query heading */}
        <div className="mb-10">
          <p className="text-xs tracking-widest uppercase text-ink-faint mb-2">
            Search results for
          </p>
          <h1
            className="text-4xl text-ink"
            style={{ fontFamily: "var(--font-display)" }}
          >
            &ldquo;{query}&rdquo;
          </h1>
          {totalResults > 0 && (
            <p className="text-sm text-ink-muted mt-2">
              {totalResults} result{totalResults !== 1 ? "s" : ""}
              {curated.length > 0 && web.length > 0 && (
                <span>
                  {" "}— {curated.length} from the library,{" "}
                  {web.length} from the web
                </span>
              )}
            </p>
          )}
        </div>

        {/* No results at all */}
        {totalResults === 0 && (
          <div className="text-center py-20">
            <p className="text-ink-muted text-lg mb-2">Nothing found for &ldquo;{query}&rdquo;.</p>
            <p className="text-ink-faint text-sm">
              Try a broader term, or{" "}
              <Link href="/" className="underline hover:text-ink">
                explore a category
              </Link>
              .
            </p>
          </div>
        )}

        {/* Curated results */}
        {curated.length > 0 && (
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-5">
              <h2 className="text-xs tracking-widest uppercase text-ink-muted">
                From the Library
              </h2>
              <div className="flex-1 h-px bg-border" />
              <span className="text-xs text-ink-faint">
                Hand-curated · Always ad-free
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {curated.map((entry) => (
                <CuratedCard key={entry.id} entry={entry} />
              ))}
            </div>
          </section>
        )}

        {/* Web results */}
        {webEnabled && web.length > 0 && (
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-5">
              <h2 className="text-xs tracking-widest uppercase text-ink-muted">
                From the Web
              </h2>
              <div className="flex-1 h-px bg-border" />
              <span className="text-xs text-ink-faint">
                Filtered to {web.length > 1 ? `${web.length} ` : ""}quality sources only
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {web.map((result) => (
                <WebCard key={result.url} result={result} />
              ))}
            </div>
          </section>
        )}

        {/* Web disabled notice */}
        {!webEnabled && curated.length > 0 && (
          <div className="border border-border/60 p-5 text-sm text-ink-muted">
            <span className="text-ink-faint tracking-widest uppercase text-xs">
              Web search
            </span>{" "}
            — Add a{" "}
            <a
              href="https://api.search.brave.com/register"
              target="_blank"
              rel="noopener noreferrer"
              className="underline hover:text-ink"
            >
              free Brave Search API key
            </a>{" "}
            to <code className="font-mono text-xs">.env.local</code> to unlock
            results from 60+ quality publications.
          </div>
        )}
      </main>

      <footer className="px-8 py-6 border-t border-border">
        <p className="text-center text-xs text-ink-faint tracking-widest uppercase">
          No algorithms. No ads. Human curation only.
        </p>
      </footer>
    </div>
  );
}
