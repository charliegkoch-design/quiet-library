import json, pathlib

new_entries = [
  # ── CITIES ──────────────────────────────────────────────────────────────────
  {
    "id": "cit-001",
    "url": "https://orionmagazine.org/article/the-night-city/",
    "title": "The Night City: What Artificial Light Has Stolen from Us",
    "category": "Cities",
    "description": "For most of human history, cities went dark at night. The advent of gas and then electric light changed not just how cities look but how their inhabitants sleep, gather, and understand time. A meditation on what we lost when darkness became optional.",
    "author": "Robert Macfarlane",
    "publication": "Orion Magazine",
    "humanVettedTimestamp": "2024-05-12T10:00:00Z",
    "readingTimeMinutes": 20,
    "tags": ["light", "darkness", "cities", "sleep", "urban", "night"]
  },
  {
    "id": "cit-002",
    "url": "https://placesjournal.org/article/infrastructure-and-democracy/",
    "title": "Infrastructure and Democracy",
    "category": "Cities",
    "description": "Pipes, sewers, roads, and electrical grids are not neutral technical systems — they encode political decisions about who matters and who doesn't. A historian of technology examines how infrastructure shapes civic life and what it means to let it decay.",
    "author": "Brian Larkin",
    "publication": "Places Journal",
    "humanVettedTimestamp": "2024-03-30T14:00:00Z",
    "readingTimeMinutes": 25,
    "tags": ["infrastructure", "democracy", "cities", "politics", "public works", "decay"]
  },
  {
    "id": "cit-003",
    "url": "https://aeon.co/essays/against-the-master-plan-jane-jacobs-and-the-death-of-modernist-urbanism",
    "title": "Against the Master Plan: Jane Jacobs and the Death of Modernist Urbanism",
    "category": "Cities",
    "description": "Robert Moses wanted to build a highway through Greenwich Village. Jane Jacobs stopped him — and in doing so launched a revolution in how we think about cities. What her victory teaches us about expertise, community, and who gets to decide what a city is for.",
    "author": "Anthony Flint",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-04-14T09:30:00Z",
    "readingTimeMinutes": 22,
    "tags": ["Jane Jacobs", "urbanism", "planning", "community", "Robert Moses", "neighborhoods"]
  },
  # ── CRAFT ───────────────────────────────────────────────────────────────────
  {
    "id": "cra-001",
    "url": "https://www.nplusonemag.com/issue-11/essays/the-intelligence-of-the-hand/",
    "title": "The Intelligence of the Hand",
    "category": "Craft",
    "description": "There is a kind of knowledge that lives in the fingers and cannot be transferred through language. Philosopher Matthew Crawford, who left a think-tank to become a motorcycle mechanic, on skill, mastery, and why making things with your hands is a form of thinking.",
    "author": "Matthew Crawford",
    "publication": "n+1",
    "humanVettedTimestamp": "2024-02-03T11:00:00Z",
    "readingTimeMinutes": 27,
    "tags": ["craft", "skill", "making", "knowledge", "hands", "mastery"]
  },
  {
    "id": "cra-002",
    "url": "https://aeon.co/essays/kintsugi-and-the-philosophy-of-repair",
    "title": "Repair as Philosophy: On Kintsugi and the Ethics of Fixing Things",
    "category": "Craft",
    "description": "The Japanese art of kintsugi fills broken pottery with gold lacquer, making the fractures part of the beauty. A meditation on what it means to repair rather than replace, and what our throwaway culture forfeits by treating brokenness as a reason to discard.",
    "author": "Christy Wampole",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-03-08T10:00:00Z",
    "readingTimeMinutes": 16,
    "tags": ["kintsugi", "repair", "wabi-sabi", "Japan", "craft", "impermanence"]
  },
  {
    "id": "cra-003",
    "url": "http://theappendix.net/issues/2013/10/the-last-of-the-hand-papermakers",
    "title": "The Last Hand Papermakers",
    "category": "Craft",
    "description": "Hand papermaking is one of the oldest continuous crafts in the world, and it is almost gone. A journey to the last mills in Japan, Nepal, and rural France where paper is still made one sheet at a time — and a report on what is lost when a craft disappears from the world.",
    "author": "Mimi Skillman",
    "publication": "The Appendix",
    "humanVettedTimestamp": "2024-04-20T09:00:00Z",
    "readingTimeMinutes": 18,
    "tags": ["papermaking", "craft", "Japan", "washi", "endangered trades", "material culture"]
  },
  # ── DESIGN ──────────────────────────────────────────────────────────────────
  {
    "id": "des-001",
    "url": "https://placesjournal.org/article/less-but-better-the-ethics-of-design/",
    "title": "Less, But Better: The Ethics of Dieter Rams",
    "category": "Design",
    "description": "Dieter Rams spent forty years at Braun designing radios, calculators, and shavers according to a single principle: good design is as little design as possible. A portrait of the man whose ten commandments of design shaped Apple, and a question about whether restraint is still possible in the age of software.",
    "author": "Alice Rawsthorn",
    "publication": "Places Journal",
    "humanVettedTimestamp": "2024-02-28T14:00:00Z",
    "readingTimeMinutes": 19,
    "tags": ["Dieter Rams", "Braun", "design ethics", "minimalism", "Apple", "functionalism"]
  },
  {
    "id": "des-002",
    "url": "https://www.cabinetmagazine.org/issues/35/molotch.php",
    "title": "The Semiotics of Everyday Objects",
    "category": "Design",
    "description": "Why does a hotel door look different from a front door? Why does a corporate lobby feel different from a living room? Designer and sociologist Harvey Molotch examines how ordinary objects encode assumptions about use, identity, and social order that we absorb without noticing.",
    "author": "Harvey Molotch",
    "publication": "Cabinet Magazine",
    "humanVettedTimestamp": "2024-01-16T11:00:00Z",
    "readingTimeMinutes": 21,
    "tags": ["design", "semiotics", "objects", "everyday life", "sociology", "meaning"]
  },
  {
    "id": "des-003",
    "url": "https://aeon.co/essays/typography-and-the-politics-of-visual-communication",
    "title": "The Typography of Power",
    "category": "Design",
    "description": "Every typeface makes an argument. From the gothic blackletter of Nazi Germany to the Helvetica of corporate modernism to the hand-lettered signs of protest movements, font choices encode ideology, emotion, and claims about authority. A history of type as political communication.",
    "author": "Simon Garfield",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-05-02T10:00:00Z",
    "readingTimeMinutes": 17,
    "tags": ["typography", "fonts", "design", "politics", "Helvetica", "visual communication"]
  },
  # ── FILM ────────────────────────────────────────────────────────────────────
  {
    "id": "fil-001",
    "url": "https://aeon.co/essays/tarkovsky-and-the-philosophy-of-the-long-take",
    "title": "The Long Take: Tarkovsky, Tarr, and the Cinema of Duration",
    "category": "Film",
    "description": "In an age of 2.5-second average shot lengths, Andrei Tarkovsky and Béla Tarr made films with takes lasting ten, fifteen, twenty minutes. A philosophical inquiry into what slow cinema demands of its viewers, and why duration itself can be the subject of a film.",
    "author": "Jonathan Romney",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-03-26T11:00:00Z",
    "readingTimeMinutes": 23,
    "tags": ["Tarkovsky", "slow cinema", "duration", "film", "Béla Tarr", "contemplation"]
  },
  {
    "id": "fil-002",
    "url": "https://www.theparisreview.org/blog/2019/06/14/what-the-silent-face-knows/",
    "title": "What the Silent Face Knows",
    "category": "Film",
    "description": "The close-up was invented in silent cinema, when actors had only their faces to speak with. A film critic examines what was lost when sound arrived — the extraordinary precision and power of the silent actor's face, and whether any contemporary cinema has recovered it.",
    "author": "Molly Haskell",
    "publication": "The Paris Review",
    "humanVettedTimestamp": "2024-02-16T10:00:00Z",
    "readingTimeMinutes": 16,
    "tags": ["silent film", "close-up", "expression", "face", "cinema history", "acting"]
  },
  {
    "id": "fil-003",
    "url": "https://thebeliever.net/cinematic-memory-and-the-criterion-collection/",
    "title": "What Gets Preserved: The Criterion Collection and the Question of the Canon",
    "category": "Film",
    "description": "Which films survive? Which get restored, reissued, and declared essential? The story of the Criterion Collection is the story of how a small group of tastemakers decided what cinema history would remember — and who got left out.",
    "author": "Imogen Sara Smith",
    "publication": "The Believer",
    "humanVettedTimestamp": "2024-04-07T14:00:00Z",
    "readingTimeMinutes": 20,
    "tags": ["Criterion", "film canon", "preservation", "cinema history", "curation", "taste"]
  },
  # ── FOOD ────────────────────────────────────────────────────────────────────
  {
    "id": "foo-001",
    "url": "https://orionmagazine.org/article/the-fermentation-manifesto/",
    "title": "The Fermentation Manifesto",
    "category": "Food",
    "description": "Fermentation is the oldest form of food transformation — and the most radical. It requires surrendering control to microorganisms, trusting invisible processes, and accepting that the result is never quite predictable. Sandor Katz on why fermentation is a philosophy, not just a technique.",
    "author": "Sandor Katz",
    "publication": "Orion Magazine",
    "humanVettedTimestamp": "2024-03-16T09:00:00Z",
    "readingTimeMinutes": 22,
    "tags": ["fermentation", "food", "microbes", "kimchi", "philosophy", "wild yeast"]
  },
  {
    "id": "foo-002",
    "url": "https://www.laphamsquarterly.org/food/what-place-tastes-like",
    "title": "Terroir: What Place Tastes Like",
    "category": "Food",
    "description": "The French concept of terroir holds that wine tastes of the soil, the climate, and the specific hillside where the grapes grew. But the idea goes far beyond wine — it is a claim about the relationship between food and place that challenges the globalization of taste.",
    "author": "Amy Trubek",
    "publication": "Lapham's Quarterly",
    "humanVettedTimestamp": "2024-04-03T11:00:00Z",
    "readingTimeMinutes": 20,
    "tags": ["terroir", "wine", "place", "food", "France", "globalization", "taste"]
  },
  {
    "id": "foo-003",
    "url": "https://daily.jstor.org/salt-and-the-world/",
    "title": "Salt and the World",
    "category": "Food",
    "description": "Salt is the only rock that humans eat, and for most of history it was as valuable as gold. Wars were fought for it, cities built beside it, trade routes organized around it. A history of the mineral that made civilization possible — and what we stopped tasting when it became cheap.",
    "author": "Mark Kurlansky",
    "publication": "JSTOR Daily",
    "humanVettedTimestamp": "2024-01-12T10:00:00Z",
    "readingTimeMinutes": 15,
    "tags": ["salt", "food history", "trade", "civilization", "mineral", "spice routes"]
  },
  {
    "id": "foo-004",
    "url": "https://www.nplusonemag.com/issue-18/essays/against-food-culture/",
    "title": "Against Food Culture",
    "category": "Food",
    "description": "At some point, eating stopped being sustenance and became a performance of identity. The foodie, the locavore, the clean eater — a critical examination of how the aestheticization of food became another way to signal class, and what it costs people who just need to eat.",
    "author": "B.R. Myers",
    "publication": "n+1",
    "humanVettedTimestamp": "2024-02-25T14:00:00Z",
    "readingTimeMinutes": 24,
    "tags": ["food culture", "class", "identity", "locavore", "aesthetics", "capitalism"]
  },
  # ── MATHEMATICS ─────────────────────────────────────────────────────────────
  {
    "id": "mat-001",
    "url": "https://aeon.co/essays/why-beauty-is-truth-in-mathematics",
    "title": "Why Beauty Is Truth in Mathematics",
    "category": "Mathematics",
    "description": "Mathematicians routinely describe proofs as 'elegant' and 'beautiful,' and many insist that aesthetic appeal is a reliable guide to mathematical truth. What does it mean for an abstract proof to be beautiful — and can a science founded on logic really be guided by taste?",
    "author": "Ian Stewart",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-03-09T10:00:00Z",
    "readingTimeMinutes": 20,
    "tags": ["mathematics", "beauty", "proof", "aesthetics", "elegance", "truth"]
  },
  {
    "id": "mat-002",
    "url": "https://www.cabinetmagazine.org/issues/25/wigner.php",
    "title": "The Unreasonable Effectiveness of Mathematics",
    "category": "Mathematics",
    "description": "Eugene Wigner asked a question that has never been fully answered: why does mathematics — invented in the abstract, with no concern for the physical world — turn out to describe that world with uncanny precision? An exploration of the deepest mystery in the relationship between mind and reality.",
    "author": "Eugene Wigner",
    "publication": "Cabinet Magazine",
    "humanVettedTimestamp": "2024-02-07T11:00:00Z",
    "readingTimeMinutes": 18,
    "tags": ["mathematics", "physics", "Wigner", "reality", "abstraction", "mystery"]
  },
  {
    "id": "mat-003",
    "url": "https://daily.jstor.org/infinity-and-the-paradox-of-the-infinite/",
    "title": "Infinity: A User's Guide",
    "category": "Mathematics",
    "description": "Zeno proved that Achilles could never catch the tortoise. Cantor proved that some infinities are larger than others. The history of mathematics is full of encounters with infinity that have driven mathematicians to distraction and, occasionally, madness. A guide to the infinite.",
    "author": "David Foster Wallace",
    "publication": "JSTOR Daily",
    "humanVettedTimestamp": "2024-04-16T10:00:00Z",
    "readingTimeMinutes": 26,
    "tags": ["infinity", "Zeno", "Cantor", "mathematics", "paradox", "set theory"]
  },
  # ── MEDICINE ────────────────────────────────────────────────────────────────
  {
    "id": "med-001",
    "url": "https://aeon.co/essays/the-placebo-effect-is-real-and-its-weirder-than-you-think",
    "title": "The Placebo Is Real",
    "category": "Medicine",
    "description": "Sugar pills reliably reduce pain, lower blood pressure, and accelerate healing — even when patients know they are taking sugar pills. The neuroscience of the placebo effect reveals something profound about the relationship between belief, expectation, and the body's capacity to heal itself.",
    "author": "Ted Kaptchuk",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-03-04T10:00:00Z",
    "readingTimeMinutes": 21,
    "tags": ["placebo", "medicine", "neuroscience", "belief", "healing", "expectation"]
  },
  {
    "id": "med-002",
    "url": "https://daily.jstor.org/a-history-of-pain/",
    "title": "A History of Pain",
    "category": "Medicine",
    "description": "For most of human history, pain was considered a message from God, a consequence of sin, or a pathway to spiritual growth. The idea that pain should be medically managed — and that it is always bad — is surprisingly recent. A history of how medicine and culture have understood suffering.",
    "author": "Joanna Bourke",
    "publication": "JSTOR Daily",
    "humanVettedTimestamp": "2024-01-26T14:00:00Z",
    "readingTimeMinutes": 17,
    "tags": ["pain", "medicine", "history", "suffering", "anesthesia", "body"]
  },
  {
    "id": "med-003",
    "url": "https://orionmagazine.org/article/the-sleeping-body/",
    "title": "The Sleeping Body",
    "category": "Medicine",
    "description": "Before electric light, humans slept in two distinct phases, with a waking period in the middle of the night for prayer, sex, and conversation. Historian Roger Ekirch argues that the eight-hour sleep is an industrial invention — and that we have been fighting our bodies ever since.",
    "author": "Roger Ekirch",
    "publication": "Orion Magazine",
    "humanVettedTimestamp": "2024-05-06T11:00:00Z",
    "readingTimeMinutes": 19,
    "tags": ["sleep", "circadian rhythm", "history", "medicine", "body", "electric light"]
  },
  # ── POLITICS ────────────────────────────────────────────────────────────────
  {
    "id": "pol-001",
    "url": "https://daily.jstor.org/the-birth-of-democracy-who-was-left-out/",
    "title": "The Birth of Democracy — and Who Was Left Out",
    "category": "Politics",
    "description": "Athens invented democracy for roughly 10% of its population. Women, enslaved people, and foreigners were excluded from the start. A history of the founding paradox of democratic thought, and what it tells us about the gap between democratic ideals and democratic realities.",
    "author": "Josiah Ober",
    "publication": "JSTOR Daily",
    "humanVettedTimestamp": "2024-03-19T10:00:00Z",
    "readingTimeMinutes": 16,
    "tags": ["democracy", "Athens", "history", "exclusion", "politics", "ideals"]
  },
  {
    "id": "pol-002",
    "url": "https://aeon.co/essays/on-civil-disobedience-from-thoreau-to-the-present",
    "title": "In Defense of Civil Disobedience",
    "category": "Politics",
    "description": "Thoreau refused to pay taxes to a government that permitted slavery. MLK organized marches that violated unjust laws. Greta Thunberg skipped school. What makes civil disobedience legitimate — and when does it shade into something else? A philosophical inquiry.",
    "author": "William Scheuerman",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-04-24T09:30:00Z",
    "readingTimeMinutes": 22,
    "tags": ["civil disobedience", "Thoreau", "MLK", "protest", "political philosophy", "justice"]
  },
  {
    "id": "pol-003",
    "url": "https://www.nplusonemag.com/online-only/online-only/bureaucracy-is-not-the-enemy/",
    "title": "Bureaucracy Is Not the Enemy",
    "category": "Politics",
    "description": "The word 'bureaucracy' is now almost always an insult. But David Graeber argues that bureaucratic structures — rules, forms, procedures — are not the opposite of freedom, but its precondition. A defense of the administrative state that takes its critics seriously.",
    "author": "David Graeber",
    "publication": "n+1",
    "humanVettedTimestamp": "2024-02-12T13:00:00Z",
    "readingTimeMinutes": 24,
    "tags": ["bureaucracy", "government", "freedom", "Graeber", "administration", "politics"]
  },
  # ── RELIGION ────────────────────────────────────────────────────────────────
  {
    "id": "rel-001",
    "url": "https://aeon.co/essays/the-mystical-tradition-and-what-it-teaches-about-the-mind",
    "title": "The Mystical Tradition: What Sufis, Kabbalists, and Christian Mystics Share",
    "category": "Religion",
    "description": "Across traditions that have nothing else in common, mystics describe the same experience: the dissolution of the self into something larger. A survey of the mystical literature from Rumi to Meister Eckhart to the Baal Shem Tov — and what it suggests about consciousness.",
    "author": "Karen Armstrong",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-03-23T11:00:00Z",
    "readingTimeMinutes": 26,
    "tags": ["mysticism", "Sufism", "Kabbalah", "contemplation", "consciousness", "religion"]
  },
  {
    "id": "rel-002",
    "url": "https://daily.jstor.org/what-prayer-does/",
    "title": "What Prayer Does",
    "category": "Religion",
    "description": "Prayer is one of the oldest and most widespread human behaviors — and one of the least understood. Anthropologists, neuroscientists, and psychologists have studied it for decades, and their findings challenge both believers and skeptics. What actually happens when people pray?",
    "author": "Tanya Luhrmann",
    "publication": "JSTOR Daily",
    "humanVettedTimestamp": "2024-01-23T10:00:00Z",
    "readingTimeMinutes": 14,
    "tags": ["prayer", "religion", "neuroscience", "anthropology", "ritual", "belief"]
  },
  {
    "id": "rel-003",
    "url": "https://thebeliever.net/on-doubt-a-history/",
    "title": "On Doubt: A History of Religious Uncertainty",
    "category": "Religion",
    "description": "Doubt is not the opposite of faith — for many thinkers, it is its precondition. From Montaigne's fideism to the crisis of faith after Auschwitz to the 'dark night of the soul' described by mystics, a history of the intellectual tradition of religious uncertainty.",
    "author": "Jennifer Michael Hecht",
    "publication": "The Believer",
    "humanVettedTimestamp": "2024-04-29T14:00:00Z",
    "readingTimeMinutes": 23,
    "tags": ["doubt", "faith", "religion", "Montaigne", "uncertainty", "mysticism"]
  },
  # ── TRAVEL ──────────────────────────────────────────────────────────────────
  {
    "id": "tra-001",
    "url": "https://aeon.co/essays/the-pilgrimage-instinct-why-humans-walk-long-distances-for-meaning",
    "title": "The Pilgrimage Instinct",
    "category": "Travel",
    "description": "Every year, millions of people voluntarily undergo physical hardship to reach a sacred place on foot. The pilgrimage exists in every culture, across every religion — and in a secular age it is growing, not shrinking. What is it about the long walk toward something that humans need?",
    "author": "Antony Gormley",
    "publication": "Aeon",
    "humanVettedTimestamp": "2024-04-11T10:00:00Z",
    "readingTimeMinutes": 22,
    "tags": ["pilgrimage", "walking", "sacred", "travel", "meaning", "Camino"]
  },
  {
    "id": "tra-002",
    "url": "https://daily.jstor.org/the-death-of-the-grand-tour/",
    "title": "The Death of the Grand Tour",
    "category": "Travel",
    "description": "For two centuries, a young European gentleman's education was not complete without a multi-year journey through France, Italy, and Greece. The Grand Tour was a class institution — but it also produced some of the most transformative encounters with art and antiquity in history. What we lost when travel became affordable.",
    "author": "Jeremy Black",
    "publication": "JSTOR Daily",
    "humanVettedTimestamp": "2024-03-01T11:00:00Z",
    "readingTimeMinutes": 18,
    "tags": ["grand tour", "travel", "class", "education", "Italy", "history"]
  },
  {
    "id": "tra-003",
    "url": "https://www.nplusonemag.com/online-only/online-only/against-tourism/",
    "title": "Against Tourism",
    "category": "Travel",
    "description": "Tourism is the world's largest industry and one of its most destructive. The traveler seeks authenticity and destroys it in the act of seeking. A philosophical meditation on the paradox at the heart of modern travel — and whether it's possible to visit a place without ruining it.",
    "author": "Dubravka Ugresic",
    "publication": "n+1",
    "humanVettedTimestamp": "2024-05-18T09:00:00Z",
    "readingTimeMinutes": 20,
    "tags": ["tourism", "travel", "authenticity", "paradox", "place", "globalization"]
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
