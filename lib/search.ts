import rawLinks from "@/data/curated-links.json";
import type { CuratedEntry } from "@/lib/curated";
import { isQualityDomain } from "@/lib/quality-domains";

const links = rawLinks as CuratedEntry[];

export interface WebResult {
  title: string;
  url: string;
  description: string;
  publication: string;
  source: "web";
}

export interface SearchResults {
  curated: CuratedEntry[];
  web: WebResult[];
  webEnabled: boolean;
}

/** Score a curated entry against a freetext query (0–1). */
function curatedScore(entry: CuratedEntry, query: string): number {
  const q = query.toLowerCase();
  const terms = q.split(/\s+/).filter(Boolean);
  let score = 0;

  for (const term of terms) {
    if (entry.category.toLowerCase().includes(term)) score += 3;
    if (entry.title.toLowerCase().includes(term)) score += 2;
    if (entry.tags.some((t) => t.toLowerCase().includes(term))) score += 2;
    if (entry.description.toLowerCase().includes(term)) score += 1;
    if (entry.author.toLowerCase().includes(term)) score += 1;
    if (entry.publication.toLowerCase().includes(term)) score += 1;
  }

  return score;
}

/** Search the curated library by freetext query. */
export function searchCurated(query: string, limit = 6): CuratedEntry[] {
  if (!query.trim()) return [];

  return links
    .map((entry) => ({ entry, score: curatedScore(entry, query) }))
    .filter(({ score }) => score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit)
    .map(({ entry }) => entry);
}

/** Derive a publication name from a URL hostname. */
function pubFromUrl(url: string): string {
  try {
    const host = new URL(url).hostname.replace(/^www\./, "");
    const map: Record<string, string> = {
      "aeon.co": "Aeon",
      "newyorker.com": "The New Yorker",
      "theatlantic.com": "The Atlantic",
      "harpers.org": "Harper's Magazine",
      "nyrb.com": "NYRB",
      "lrb.co.uk": "London Review of Books",
      "longreads.com": "Longreads",
      "nautil.us": "Nautilus",
      "nautilus.pub": "Nautilus",
      "scientificamerican.com": "Scientific American",
      "smithsonianmag.com": "Smithsonian Magazine",
      "nationalgeographic.com": "National Geographic",
      "theguardian.com": "The Guardian",
      "bostonreview.net": "Boston Review",
      "lithub.com": "Literary Hub",
      "granta.com": "Granta",
      "themarginalian.org": "The Marginalian",
      "poetryfoundation.org": "Poetry Foundation",
      "jacobinmag.com": "Jacobin",
      "thenation.com": "The Nation",
      "foreignaffairs.com": "Foreign Affairs",
    };
    return map[host] ?? host.replace(/\.(com|org|net|co\.uk|pub)$/, "");
  } catch {
    return "Web";
  }
}

/** Call Brave Search and return quality-filtered results. */
async function braveSearch(query: string, count = 10): Promise<WebResult[]> {
  const key = process.env.BRAVE_API_KEY;
  if (!key) return [];

  const url = new URL("https://api.search.brave.com/res/v1/web/search");
  url.searchParams.set("q", query);
  url.searchParams.set("count", String(count));
  url.searchParams.set("result_filter", "web");
  url.searchParams.set("freshness", "py"); // past year preferred

  const res = await fetch(url.toString(), {
    headers: {
      Accept: "application/json",
      "Accept-Encoding": "gzip",
      "X-Subscription-Token": key,
    },
    next: { revalidate: 3600 }, // cache 1 hour
  });

  if (!res.ok) return [];

  const data = await res.json();
  const raw: Array<{ title: string; url: string; description?: string }> =
    data?.web?.results ?? [];

  return raw
    .filter((r) => isQualityDomain(r.url))
    .map((r) => ({
      title: r.title,
      url: r.url,
      description: r.description ?? "",
      publication: pubFromUrl(r.url),
      source: "web" as const,
    }));
}

/** Full search: curated first, then quality web results. */
export async function search(query: string): Promise<SearchResults> {
  const [curated, web] = await Promise.all([
    Promise.resolve(searchCurated(query)),
    braveSearch(query),
  ]);

  // Remove web results whose URLs are already in the curated set
  const curatedUrls = new Set(curated.map((e) => e.url));
  const deduped = web.filter((r) => !curatedUrls.has(r.url));

  return {
    curated,
    web: deduped,
    webEnabled: Boolean(process.env.BRAVE_API_KEY),
  };
}
