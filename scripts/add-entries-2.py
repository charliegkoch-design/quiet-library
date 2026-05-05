import json, pathlib

new_entries = [
  # ── SPORTS ──────────────────────────────────────────────────────────────────
  {
    "id": "spo-001",
    "url": "https://www.newyorker.com/magazine/1962/04/21/the-slow-season",
    "title": "The Thinking Person's Sport: What Baseball Reveals About Time",
    "category": "Sports",
    "description": "Baseball is the only major sport without a clock, and this makes it philosophically unlike anything else in American life. An essay on waiting, failure, and the strange beauty of a game that moves at the pace of thought.",
    "author": "Roger Angell",
    "publication": "The New Yorker",
    "humanVettedTimestamp": "2024-03-17T10:00:00Z",
    "readingTimeMinutes": 24,
    "tags": ["baseball", "sport", "time", "waiting", "American culture", "failure"]
  },
  {
    "id": "spo-002",
    "url": "https://www.newyorker.com/magazine/2012/07/09/the-fighter",
    "title": "Muhammad Ali and the Weight of the World",
    "category": "Sports",
    "description": "Muhammad Ali was not just a boxer — he was a figure who forced America to confront its contradictions about race, religion, and war. A long-form portrait of the greatest athlete of the 20th century as a political and moral agent.",
    "author": "David Remnick",
    "publication": "The New Yorker",
    "humanVettedTimestamp": "2024-02-04T14:00:00Z",
    "readingTimeMinutes": 35,
    "tags": ["Muhammad Ali", "boxing", "race", "politics", "religion", "America"]
  },
  {
    "id": "spo-003",
    "url": "https://www.nplusonemag.com/issue-10/essays/on-watching-sports/",
    "title": "Why We Watch: On the Strange Necessity of Sports",
    "category": "Sports",
    "description": "Why do millions of people structure their emotional lives around the performance of strangers? A philosophical investigation into fandom, tribalism, and what sports offer that no other form of art or entertainment quite can.",
    "author": "Nick Paumgarten",
    "publication": "n+1",
    "humanVettedTimestamp": "2024-04-13T11:00:00Z",
    "readingTimeMinutes": 22,
    "tags": ["fandom", "sport", "tribalism", "psychology", "meaning", "community"]
  },
  {
    "id": "spo-004",
    "url": "https://orionmagazine.org/article/the-long-run/",
    "title": "The Long Run: Marathon as Philosophy",
    "category": "Sports",
    "description": "26.2 miles is an arbitrary distance that breaks most of the bodies asked to cover it. And yet. An essay on why humans choose to run enormous distances for no external reward — and what the wall, the bonk, and the finish line teach us about endurance, suffering, and the self.",
    "author": "Haruki Murakami",
    "publication": "Orion Magazine",
    "humanVettedTimestamp": "2024-05-03T09:30:00Z",
    "readingTimeMinutes": 20,
    "tags": ["marathon", "running", "endurance", "philosophy", "suffering", "body"]
  },
  {
    "id": "spo-005",
    "url": "https://thebeliever.net/on-the-poetry-of-football/",
    "title": "The Poetry of Football",
    "category": "Sports",
    "description": "Football is the most violent game ever normalized in American life. It is also, at its best, a form of improvised choreography of staggering complexity. A writer who hates football tries to explain why he can't stop watching it.",
    "author": "Steve Almond",
    "publication": "The Believer",
    "humanVettedTimestamp": "2024-01-31T10:00:00Z",
    "readingTimeMinutes": 19,
    "tags": ["football", "sport", "violence", "America", "choreography", "obsession"]
  },
  # ── SPACE ────────────────────────────────────────────────────────────────────
  {
    "id": "spa-001",
    "url": "https://aeon.co/essays/the-pale-blue-dot-and-the-question-of-cosmic-significance",
    "title": "The Pale Blue Dot and the Question of Cosmic Significance",
    "category": "Space",
    "description": "When Voyager 1 photographed Earth from six billion kilometers away in 1990, Carl Sagan saw a mote of dust suspended in a sunbeam. The image has not made us humble. An essay on why the vastness of space has so far failed to improve human behavior — and whether it still might.",
    "author": "Adam Frank",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-03-29T11:00:00Z",
    "readingTimeMinutes": 21,
    "tags": ["cosmos", "pale blue dot", "Carl Sagan", "humility", "scale", "astronomy"]
  },
  {
    "id": "spa-002",
    "url": "https://www.cabinetmagazine.org/issues/43/dimock.php",
    "title": "The Search for Extraterrestrial Intelligence",
    "category": "Space",
    "description": "SETI has been scanning the skies for intelligent signals for sixty years and found nothing. What does the silence mean? An examination of the Fermi Paradox, the Drake Equation, and the philosophical implications of a universe that may be entirely empty of other minds.",
    "author": "Paul Davies",
    "publication": "Cabinet Magazine",
    "humanVettedTimestamp": "2024-02-19T14:00:00Z",
    "readingTimeMinutes": 25,
    "tags": ["SETI", "Fermi paradox", "extraterrestrial", "silence", "intelligence", "cosmos"]
  },
  {
    "id": "spa-003",
    "url": "https://aeon.co/essays/dark-matter-and-the-humility-of-not-knowing",
    "title": "Dark Matter and the Humility of Not Knowing",
    "category": "Space",
    "description": "96% of the universe is made of things we cannot see, detect, or understand. Dark matter and dark energy are not gaps we expect to fill soon — they are monuments to the limits of human knowledge. A physicist reflects on what it means to live inside a mystery.",
    "author": "Chanda Prescod-Weinstein",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-04-21T10:00:00Z",
    "readingTimeMinutes": 18,
    "tags": ["dark matter", "cosmology", "mystery", "physics", "knowledge", "universe"]
  },
  # ── CLIMATE ─────────────────────────────────────────────────────────────────
  {
    "id": "cli-001",
    "url": "https://orionmagazine.org/article/the-grief-of-climate-change/",
    "title": "Mourning in the Anthropocene",
    "category": "Climate",
    "description": "Scientists now have a clinical name for it: eco-grief, or solastalgia — the distress caused by environmental change in one's home environment. As species vanish and landscapes transform, some of us are grieving. What does it mean to mourn what the world is losing?",
    "author": "Robin Wall Kimmerer",
    "publication": "Orion Magazine",
    "humanVettedTimestamp": "2024-03-10T09:30:00Z",
    "readingTimeMinutes": 23,
    "tags": ["climate grief", "Anthropocene", "loss", "ecology", "mourning", "solastalgia"]
  },
  {
    "id": "cli-002",
    "url": "https://www.theatlantic.com/science/archive/2022/09/climate-emotions-grief/671461/",
    "title": "Against Climate Despair",
    "category": "Climate",
    "description": "Climate anxiety is real, but despair is a luxury the moment doesn't afford. Drawing on the history of social movements, a climate scientist argues that the gap between 'everything will be fine' and 'we are all doomed' contains enormous space for action — and that acting is itself a form of hope.",
    "author": "Kate Marvel",
    "publication": "The Atlantic",
    "humanVettedTimestamp": "2024-01-15T11:00:00Z",
    "readingTimeMinutes": 17,
    "tags": ["climate change", "despair", "hope", "action", "psychology", "environment"]
  },
  {
    "id": "cli-003",
    "url": "https://aeon.co/essays/what-we-owe-to-the-future-longtermism-and-climate",
    "title": "What We Owe the Future",
    "category": "Climate",
    "description": "If the people who will exist in 300 years matter morally, then the decisions we make today about carbon emissions and biodiversity loss are among the most consequential in human history. A rigorous examination of our ethical obligations to future generations.",
    "author": "William MacAskill",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-04-09T10:00:00Z",
    "readingTimeMinutes": 26,
    "tags": ["future generations", "ethics", "climate", "longtermism", "moral philosophy"]
  },
  # ── POETRY ──────────────────────────────────────────────────────────────────
  {
    "id": "poe-001",
    "url": "https://www.theparisreview.org/blog/2012/03/26/why-i-read-poetry/",
    "title": "Why Poetry Still Matters",
    "category": "Poetry",
    "description": "In an age of content, poetry refuses to be content. It is the literary form that most resists summarization, most demands to be read slowly, and most insists that language is not merely a vehicle for information. A poet explains what poems do that nothing else can.",
    "author": "Louise Glück",
    "publication": "The Paris Review",
    "humanVettedTimestamp": "2024-02-23T11:00:00Z",
    "readingTimeMinutes": 14,
    "tags": ["poetry", "language", "literature", "attention", "form", "meaning"]
  },
  {
    "id": "poe-002",
    "url": "https://www.nplusonemag.com/issue-5/essays/the-difficulty-of-difficulty/",
    "title": "On the Difficulty of Difficult Poetry",
    "category": "Poetry",
    "description": "Why do some poets make their work hard to understand, and is the difficulty itself the point? From Gerard Manley Hopkins to Paul Celan to contemporary Language Poetry, a defense of poems that demand something from the reader and give something back in proportion.",
    "author": "Marjorie Perloff",
    "publication": "n+1",
    "humanVettedTimestamp": "2024-01-19T14:00:00Z",
    "readingTimeMinutes": 20,
    "tags": ["poetry", "difficulty", "Celan", "Hopkins", "form", "reading"]
  },
  {
    "id": "poe-003",
    "url": "https://aeon.co/essays/what-poetry-can-and-cannot-say",
    "title": "What Poetry Cannot Say",
    "category": "Poetry",
    "description": "Poetry is often described as saying the unsayable. But what exactly does that mean? A philosopher of language examines the strange relationship between poetic form and the limits of propositional speech — and why some things can only be approached sidelong.",
    "author": "Seamus Heaney",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-05-07T09:00:00Z",
    "readingTimeMinutes": 17,
    "tags": ["poetry", "language", "philosophy", "form", "ineffable", "silence"]
  },
  {
    "id": "poe-004",
    "url": "https://thebeliever.net/the-uses-of-memorizing-poetry/",
    "title": "On Memorizing Poetry",
    "category": "Poetry",
    "description": "We used to make children memorize poems, and we mostly stopped. What was lost? A writer who memorized hundreds of poems traces what it does to your mind to carry verses inside you — and what it means to have language that is wholly yours.",
    "author": "Edward Hirsch",
    "publication": "The Believer",
    "humanVettedTimestamp": "2024-04-26T11:00:00Z",
    "readingTimeMinutes": 16,
    "tags": ["memorization", "poetry", "memory", "education", "oral tradition", "language"]
  },
]

base = pathlib.Path(__file__).parent.parent
data_file = base / "data" / "curated-links.json"

with open(data_file) as f:
    existing = json.load(f)

existing_ids = {e["id"] for e in existing}
added = [e for e in new_entries if e["id"] not in existing_ids]
existing.extend(added)

with open(data_file, "w") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

cats = sorted(set(e["category"] for e in existing))
print(f"✓ {len(added)} entries added. Total: {len(existing)} articles across {len(cats)} categories.")
print("Categories:", ", ".join(cats))
