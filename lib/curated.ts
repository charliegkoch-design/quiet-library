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
  "Anthropology",
  "Architecture",
  "Art",
  "Baking",
  "Cities",
  "Climate",
  "Craft",
  "Design",
  "Economics",
  "Essays",
  "Film",
  "Food",
  "History",
  "Language",
  "Literature",
  "Mathematics",
  "Medicine",
  "Music",
  "Nature",
  "Philosophy",
  "Poetry",
  "Politics",
  "Psychology",
  "Religion",
  "Science",
  "Space",
  "Sports",
  "Technology",
  "Travel",
] as const;

/** How many pills to show before the "See all" toggle */
export const CATEGORIES_PREVIEW_COUNT = 10;

export type Category = (typeof CATEGORIES)[number];

export function formatVettedDate(isoString: string): string {
  return new Date(isoString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}
