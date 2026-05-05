import { TopicSearch } from "@/components/TopicSearch";

export default function Home() {
  return (
    <div className="min-h-screen bg-parchment flex flex-col">
      <main className="flex-1 flex flex-col items-center justify-center px-6 py-20">
        {/* Eyebrow */}
        <div
          className="mb-3 text-xs tracking-[0.35em] uppercase text-ink-faint"
          style={{ animation: "fade-up 0.6s ease-out forwards", opacity: 0 }}
        >
          A reading room
        </div>

        {/* Heading */}
        <h1
          className="text-6xl md:text-7xl text-ink text-center leading-none mb-6"
          style={{
            fontFamily: "var(--font-display)",
            animation:
              "fade-up 0.7s 0.1s cubic-bezier(0.16, 1, 0.3, 1) forwards",
            opacity: 0,
          }}
        >
          The Quiet Library
        </h1>

        {/* Tagline */}
        <p
          className="text-ink-muted text-center text-base max-w-sm leading-relaxed mb-16"
          style={{
            animation:
              "fade-up 0.7s 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards",
            opacity: 0,
          }}
        >
          Human-curated long-form reading.
          <br />
          No algorithms. No ads. No noise.
        </p>

        {/* Search block */}
        <div
          className="w-full max-w-xl"
          style={{
            animation:
              "fade-up 0.7s 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards",
            opacity: 0,
          }}
        >
          <TopicSearch />
        </div>
      </main>

      {/* Footer */}
      <footer className="px-8 py-6 border-t border-border">
        <p className="text-center text-xs text-ink-faint tracking-widest uppercase">
          Every link hand-picked. Every article worth your time.
        </p>
      </footer>
    </div>
  );
}
