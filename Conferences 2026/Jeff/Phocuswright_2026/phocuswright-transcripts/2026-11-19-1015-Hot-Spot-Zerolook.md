# Hot Spot: Zerolook

**Event:** The Phocuswright Conference 2026
**Speakers:** Simone Lini, CEO, Zerolook
**Room:** Center Stage
**Start:** 2026-11-19 10:15 AM America/New_York
**End:** 2026-11-19 10:20 AM America/New_York
**Status:** completed
**Transcript word count:** 816
**Session ID:** `abedc536-50f1-4742-9aa9-2dd9a5f4022d`

## Summary

The session opened with a pitch built around a real-world example: an AI agent built with Claude Code that ran roughly 881,000 flight searches on Etihad's website, illustrating how AI agents search far more aggressively than humans without tiring, while still booking at normal human rates. A further example showed how a simple multi-city, multi-week flight query (Fort Lauderdale/Miami to Greek islands over a month) could generate 1,400 separate searches, since these are low-intent, high-up-the-funnel queries that convert poorly—best case 1%, implying a look-to-book ratio as high as 144,000 to 1. The core problem stated was that the cost airlines and OTAs pay per search in such cases exceeds the gross margin earned from the eventual flight sale, making the current search infrastructure unsustainable for this kind of volume.

The proposed solution, Zerolook, is described as a bold bet: building a new layer specifically to absorb low-intent queries rather than sending every search to live airline or GDS systems. The pitch clarified that this approach is meant for situations where look-to-book ratios and query volume are problematic, not a replacement for existing infrastructure when that isn't an issue. Zerolook offers a flight shopping API that cuts the cost of search by up to two orders of magnitude, reserving live queries to airlines or GDS systems only for moments of genuinely high purchase intent.

Technically, the system relies on a trained machine learning model—explicitly not an LLM—that learns the pricing patterns airline revenue managers follow, combined with daily sampling of a small set of itineraries to track price movement. This lets the system predict prices accurately without hitting live systems; on their best-performing case, a U.S. carrier, the model reaches 96% pricing accuracy. The stated goal is to push accuracy to 97% across a broad set of carriers by Q1 of next year and launch a full flight search API, with the team acknowledging substantial R&D work remains before the space is fully solved.

On credibility and backing, the pitch highlighted a founding team with deep travel and tech pedigree: a founder who previously sold a company to lastminute.com, led metasearch product and commercial work, and ran partnerships at Google for tours/activities and later flights; a co-founder with an MIT computer science PhD, prior VP experience at Kayak, and engineering leadership roles at NVIDIA and Google; and an advisory board drawing from Sabre Labs, Kayak's machine learning leadership, and other veteran travel-tech operators. The company has raised $1.9 million, is based in Zurich, runs a six-person team (all engineers except the speaker), and is assembling a cohort of test partners ahead of its planned Q1 launch, inviting companies facing look-to-book cost problems to get in touch.

The session then shifted to a broader industry research presentation building on prior talks about what travel companies can learn from AI-native startups and an 'AI advantage' equation for measuring competitive position. Drawing on a new global survey of roughly 150 travel enterprises and startups—nearly all already using AI—fielded in August and September and soon to be published as 'Rebuild or Bolt-On: Travel's Agentic-AI Divide' (sponsored by CNF Travel and Sabre), the talk set up a comparison of how established companies versus startups are faring, noting that even among AI-engaged companies ahead of the industry curve, a significant divide in AI adoption and advantage remains evident.

## Key Takeaways

### 🔢 Broad travel queries can produce thousands of searches

A seemingly simple request—such as finding a one-week June trip from either Fort Lauderdale or Miami to a Greek island—can require roughly 1,400 search combinations across airports, destinations, and dates.

Quotes:

> You have two departure airports. Thirty airports in Greece on island with commercial service. And then you have 24 one-week windows in June. That makes 1,400 searches.

### 📊 Daily sampling helps track changing airline prices

Although the model does not query live systems for every request, Zerolook samples a small number of flights and itineraries each day to observe price movements and update its predictions.

Quotes:

> Every day we also take a sample of a small number of flights, of itineraries, to know how the price is moving.

### ⚖️ AI adoption is opening a divide among travel companies

Early research from a survey of roughly 150 already AI-engaged travel enterprises and startups suggests that established companies and startups are diverging in how effectively they use AI.

Quotes:

> Nearly all of them already use AI. These are companies that are AI engaged, may run ahead of the industry, yet we still see a big divide opening up among them.

### 🎯 Live inventory remains available for high-intent shoppers

Zerolook is not presented as a replacement for live airline or GDS searches. Once a traveler demonstrates sufficient intent, the system can issue a live query to obtain current booking options.

Quotes:

> Whenever someone has high enough intent, they can go and place a live query to the airline, to the GDS.

### ✈️ AI agents create an unsustainable flight-search cost problem

Agents can generate enormous numbers of flight searches because they systematically explore many combinations, but those searches often have low purchase intent. The resulting search costs can exceed the margin earned from selling the flight.

Quotes:

> They don't get tired of searching. The issue is they also book like everyone else. So, the cost becomes an issue for everyone.

### 🧪 The product is still in active research and development

The speaker stresses that Zerolook has not solved the entire flight-pricing problem yet; the reported results are encouraging, but further development is required before the planned API launch.

Quotes:

> We still have a lot of research and development in front of us, and we have by no means solved the entire space.

### 🤖 Zerolook uses traditional machine learning rather than an LLM

The pricing system is based on conventional machine learning trained to learn patterns in airline revenue-management decisions, rather than on a large language model.

Quotes:

> We have trained a machine learning model. It's not an LLM, it's good old style machine learning.

### 📉 Low-intent searches have extremely weak conversion economics

The presentation estimates that broad, exploratory flight searches may convert at best around 1%, creating a look-to-book ratio of approximately 144,000 to one and making conventional live-search economics unworkable.

Quotes:

> Those searches are very high up in the funnel. They don't convert well. Best case, one percent conversion rate. That's a look-to-book ratio of 144,000 to one.

### ✅ Zerolook reports 96% pricing accuracy for one U.S. carrier

Zerolook says its model predicted prices with 96% accuracy for one U.S. carrier without querying a live system, with a goal of reaching 97% across a broader range of carriers by Q1 next year.

Quotes:

> We can be 96% accurate on our prediction on pricing without needing to hit any live system. And our goal is to reach 97% across a wide number of carriers by Q1 next year.

### 💰 The proposed API aims to cut flight-search costs by up to 100×

The company says its flight-shopping API can reduce the cost of searching by up to two orders of magnitude, potentially making high-volume exploratory queries viable.

Quotes:

> We offer a flight shopping API that reduces the cost of search by up to two orders of magnitude.

### 🧩 Zerolook proposes a new layer for low-intent queries

Zerolook’s product is intended to handle broad, low-intent shopping requests separately from existing live airline or GDS systems, while preserving the current setup for searches whose volume is economically manageable.

Quotes:

> We're going to build one new layer that addresses all of the low-intent queries.

## Idea Cloud

- AI Agents Break Flight Search Economics (score: 361)
- Pricing Accuracy Tests Viability (score: 349)
- Flight Query Combinations Explode Search Volume (score: 349)
- Zerolook Adds A Predictive Shopping Layer (score: 348)
- Machine Learning Predicts Airline Prices (score: 337)
- Travel Companies Show An Agentic AI Divide (score: 301)
- Sampling Keeps Predictions Current (score: 235)
- Zerolook’s Specialized Team And Funding (score: 210)

## Transcript
that is—
881,000 and change flight searches.
That is what a gentleman named Kiruba posted on LinkedIn.
He built an agent with Claude Code, and the agent searched for combinations on API websites.
The issue is that's a lot of searches.
Agent search like no one else.
They don't get tired of searching.
The issue.
Is they also book like everyone else.
So, the cost becomes an issue for everyone.
For example, if I ask any AI agent, "Find me flights to get from Fort Lauderdale or Miami to a Great Island in June for one week," well, that's too many searches.
You have two departure airports.
Thirty airports in Greece on island with commercial service.
And then you have 24 one-week windows in June.
That makes 1,400 searches.
And those searches are very high up in the funnel.
They don't convert well.
Best case, one percent conversion rate.
That's a look-to-book ratio of 144,000 to one.
And the issue is that at the cost for the PSS or.
The cost of the OTA pays for the search.
This exceeds the gross margin made by selling the flight.
So that doesn't work.
Depends on your take.
Do you look is one that you might call it bold or crazy.
That is—
We're going to build one new layer that.
Addresses all of the low-intent queries.
If look-to-book, if the number of searches is not a problem by all means, the current setup is the perfect one.
But whenever there is an issue, with look-to-book, whenever the number of queries is too high, that's where we come in.
We offer a flight shopping API that reduces the cost of search by up to two orders of magnitude.
And then whenever someone has high enough intent, they can go and place a larger query to the airline, to the GDS.
So—
The name of the game here is—
Accuracy on price.
So how do we do that, by the way?
The idea, as mentioned, is we don't hit any live system.
We have trained a machine learning model.
It's not an LM.
It learns the pricing patterns followed by revenue managers at airlines.
It's a good old-style machine learning.
And every day we also take a sample that a small number of flights of itineraries to know how the price is moving.
In terms.
Out, you can actually predict the price quite well.
So far, our best result is on a US carrier the name would be ironic, given recent news, we can be 96.6 percent accurate on our prediction on pricing without needing to hit any live system.
And our goal is to reach 97 percent across a wide number of carriers by Q1 next year and launch our flight search API.
But the progress is very encouraging.
We still have a lot of research and development in front of us, and we have by no means solved the entire space.
Why ASA?
So myself, I sold my first company to Lasmin.com.
I led Meta Search on product and commercial.
I joined Google and led partnerships first on tourism activities, then on flights.
My co-founder, George, has a PhD at MIT in computer science, was a VP at Kayak, and led engineering team at NVIDIA and Google.
We also joined by an amazing advisory board, including Sundar, former CTO at IT Software, and president at Sabre Labs, Andreas, senior machine learning director at Kayak, Tai, who worked for Google as well, IT Software, and pretty much the whole industry, just like Anne, who I couldn't name all the companies she worked with without exceeding the time I have available today.
We raised 1.9 million dollars.
We are based in Zurich.
We have a small team, six people.
Everyone is an engineer.
Except for myself.
And as mentioned, we are launching in Q1 next year.
We've been assembling a cohort of test partners.
So, thank you very much.
So if look-to-book is an issue, then please find me.
A year ago on this stage, I made the case for what travel can learn from AI-native startups.
Then I focused right at Europe in June.
I proposed a simple math equation for all travel companies to be able to build and calculate their AI advantage.
Both of those talks are on YouTube on our Focusrite channel for reference.
Today I'll be elaborating on the AI advantage equation and comparing how established companies and startups are faring using our latest research.
So most of the data you'll see comes from our new global survey of travel enterprises and startups, fielded in August and September.
Soon to be published as Rebuild or Bolt On: Travel's Agentic AI Divide.
And a big thank you to CNF Travel and Sabre for sponsoring the project.
So one note upfront about 150 companies responded to the survey, and nearly all of them already use AI.
