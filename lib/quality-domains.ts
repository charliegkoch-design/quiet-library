/**
 * Trusted long-form publication domains.
 * Only web results from these sources are surfaced — no ad farms,
 * no SEO mills, no AI-generated content.
 */
export const QUALITY_DOMAINS = new Set([
  // Already in our curated collection
  "aeon.co",
  "orionmagazine.org",
  "theparisreview.org",
  "nplusonemag.com",
  "cabinetmagazine.org",
  "placesjournal.org",
  "daily.jstor.org",
  "publicbooks.org",
  "thebeliever.net",
  "laphamsquarterly.org",
  "theatlantic.com",
  "theappendix.net",
  "thebaffler.com",
  "newyorker.com",

  // Longform & literary
  "longreads.com",
  "longform.org",
  "harpers.org",
  "nyrb.com",
  "lrb.co.uk",
  "granta.com",
  "themarginalian.org",
  "lithub.com",
  "electricliterature.com",
  "believermag.com",
  "berfrois.com",
  "3quarksdaily.com",

  // Science & ideas
  "nautil.us",
  "nautilus.pub",
  "scientificamerican.com",
  "smithsonianmag.com",
  "nationalgeographic.com",
  "americanscientist.org",

  // Politics & society
  "bostonreview.net",
  "dissentmagazine.org",
  "jacobinmag.com",
  "foreignaffairs.com",
  "foreignpolicy.com",
  "thenation.com",
  "prospectmagazine.co.uk",

  // Arts & culture
  "poetryfoundation.org",
  "artforum.com",
  "frieze.com",
  "4columns.org",

  // Nature & environment
  "outsideonline.com",
  "sierraclub.org",
  "audubon.org",
  "highcountrycalvert.org",
  "highcountrynews.org",

  // Tech & ideas
  "ribbonfarm.com",
  "stratechery.com",
  "increment.com",

  // Misc quality outlets
  "texasmonthly.com",
  "theguardian.com",
  "tls.co.uk",
  "philosophybites.com",
  "philosophynow.org",
  "theconversation.com",
]);

export function isQualityDomain(url: string): boolean {
  try {
    const hostname = new URL(url).hostname.replace(/^www\./, "");
    return QUALITY_DOMAINS.has(hostname);
  } catch {
    return false;
  }
}
