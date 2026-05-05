import { redirect } from "next/navigation";
import { search } from "@/lib/search";
import { SearchResultsView } from "@/components/SearchResultsView";

export default async function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q } = await searchParams;
  if (!q?.trim()) redirect("/");

  const results = await search(q.trim());

  return <SearchResultsView query={q.trim()} results={results} />;
}
