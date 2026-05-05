export interface CuratedEntry {
  id: string;
  url: string;
  title: string;
  category: string;
  description: string;
  author: string;
  publication: string;
  humanVettedTimestamp: string;
  readingTimeMinutes: number;
  tags: string[];
}

export const CATEGORIES = [
  "Architecture",
  "Baking",
  "Philosophy",
  "Science",
  "History",
  "Literature",
  "Essays",
] as const;

export type Category = (typeof CATEGORIES)[number];

export function formatVettedDate(isoString: string): string {
  return new Date(isoString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}
