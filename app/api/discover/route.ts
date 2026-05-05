import { type NextRequest } from "next/server";
import rawLinks from "@/data/curated-links.json";
import type { CuratedEntry } from "@/lib/curated";

const links = rawLinks as CuratedEntry[];

export function GET(request: NextRequest) {
  const params = request.nextUrl.searchParams;
  const topic = params.get("topic")?.toLowerCase().trim();
  const excludeId = params.get("exclude")?.trim();

  let pool = links;

  if (topic) {
    const filtered = links.filter(
      (entry) =>
        entry.category.toLowerCase() === topic ||
        entry.category.toLowerCase().includes(topic) ||
        entry.tags.some((t) => t.toLowerCase().includes(topic))
    );
    if (filtered.length > 0) pool = filtered;
  }

  if (excludeId && pool.length > 1) {
    pool = pool.filter((entry) => entry.id !== excludeId);
  }

  const entry = pool[Math.floor(Math.random() * pool.length)];

  return Response.json(entry);
}
