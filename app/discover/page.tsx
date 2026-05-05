import { Suspense } from "react";
import { DiscoverContent } from "@/components/DiscoverContent";

function LoadingShell() {
  return (
    <div className="min-h-screen bg-parchment flex items-center justify-center">
      <p className="text-ink-faint text-sm tracking-widest uppercase animate-pulse">
        Finding something worth reading…
      </p>
    </div>
  );
}

export default function DiscoverPage() {
  return (
    <Suspense fallback={<LoadingShell />}>
      <DiscoverContent />
    </Suspense>
  );
}
