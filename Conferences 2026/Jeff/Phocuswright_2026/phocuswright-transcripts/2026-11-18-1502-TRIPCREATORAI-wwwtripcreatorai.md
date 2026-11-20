# TRIPCREATORAI (www.tripcreator.ai)

**Event:** The Phocuswright Conference 2026
**Speakers:** Chelsea Salamone, Principal, Thayer Investment Partners; Ellen Keszler, CEO, Clear Sky Associates; Erik Blachford, Founder, Pine5 Ventures LLC; Kristina Carter, VP, Global Partnerships, Perk; Kurien Jacob, Partner, Highgate Technology Ventures; Michael Berk, Director of Strategic Innovation and Partnerships, American Express Global Business Travel; Pete Comeau, Managing Director, Phocuswright; Roger Sharp, Chairman, WebBeds Group and North Ridge Partners; Steve Singh, Executive Chairman and CEO, Spotnana; Traci Mercer, Chief Commercial Officer, Priceline; Marc Harrison, Founder & CEO, TRIPCREATORAI
**Room:** Center Stage
**Start:** 2026-11-18 3:02 PM America/New_York
**End:** 2026-11-18 3:11 PM America/New_York
**Status:** completed
**Transcript word count:** 1382
**Session ID:** `359ac7db-ae3d-44f0-8389-cbae9338b293`

## Summary

The session opened with an extended Marco Polo narrative used as a framing device: unlike Columbus, who planned a journey based on secondhand, unverified stories, Marco Polo actually traveled to the places he described. This was mapped onto today's AI landscape, where LLM-generated itineraries are compared to travel writing based on information read online rather than firsthand experience — itineraries that read beautifully but fall apart when a travel specialist tries to execute them, creating a 'nightmare' when a client brings in an unworkable 15-day plan.

The company's product, also named Marco Polo, was presented as a large travel model (LTM) rather than a general-purpose LLM — a B2B tool for tour operators and travel planners built so that operators retain ownership of their data and travel expertise. Instead of predicting the next word, the model determines the best sequence of travel events from a tour operator's own catalog, matched to traveler demographics, producing a cohesive, bookable itinerary. A live demo generated a five-day Tuscany itinerary in 14 seconds, with every point of interest tied to a catalog ID, precise coordinates, and verification against both Marco Polo's own database of over half a million places and the tour operator's catalog, with zero invented locations and lower cost than general AI generation.

The business case rested on a $271 billion tours-and-experiences market, two-thirds of which is still booked offline, with custom trips representing a $25 billion high-ticket segment of which $16.8 billion remains offline and dependent on archaic email-based workflows involving four to five rounds of back-and-forth between client and specialist. The pitch positioned the product as a top-of-funnel collaboration tool where traveler, agent, and operator shape experiences, flights, hotels, and transport together on one screen, offered through three paths: a developer API, an interactive bookable itinerary tool (Vista), and a customization layer matching a brand's voice (Atlas). The long-term vision is an interactive map as the medium for collaborative trip planning, eventually allowing travelers to get feedback from friends and family and to talk to and modify itineraries conversationally, with six brands already live in 2026.

In the Q&A, panelists pushed on whether the company was really building two separate products — a developer-facing model and a crowded application layer. It was clarified that the tool does not itself book trips; booking stays with whatever system an operator already uses, while itineraries can be uploaded and shown interactively, with client communication embedded directly in the itinerary rather than in email. On future focus, the plan is to work with tour operator brands and DMCs and their travel agent networks, concentrating API development on the large travel model as the basis for trip planning and the mapping layer.

Asked what stops general LLMs from catching up and building an equivalent large travel model, the response acknowledged that serving small, medium, and large travel-specific models using operators' own data is something anyone could do, citing a recent comment that 'there is no moat,' and argued that the real defensibility comes from being first to market and from the distribution advantage of the interactive itinerary, with the model itself being a matter of execution and speed. A further question about whether the model was distilled from existing large language models was answered firmly in the negative: the system is described as a transformer model built from scratch using the company's own point-of-interest database and tour operators' data, not a distillation of general-purpose LLMs.

## Key Takeaways

### 🔌 The platform offers three ways to adopt it

Travel companies can build on the API, use interactive bookable itineraries, or create and customize trips using their own itineraries and brand voice. The company says the interactive itinerary and its distribution may provide the stronger moat than the model alone.

Quotes:

> There are three ways then to work with us: developers just build on top of our API; Vista your trips in an interactive itinerary, bookable atlas; trip creation and customization based on your itineraries and your brand's voice... We believe that the distribution, so the side of actually the interactive itinerary, is where our moat comes from.

### 🏢 Operators retain their data and expertise

Marco Polo is positioned as a B2B tool in which tour operators and travel planners retain ownership of their data and travel expertise instead of relying solely on general AI knowledge.

Quotes:

> It's a B2B tool for the itinerary creation and proprietary model for tour operators where you own your data and the travel expertise, not the general AI.

### 🔗 It sequences bookable travel events

Rather than predicting the next best words, the system determines the best sequence of travel events from a tour operator's catalog and then turns that sequence into a cohesive itinerary.

Quotes:

> Marco Polo doesn't predict the next best words; it determines the best sequence of travel events based on a tour operator's catalog.

### 🛡️ Guardrails preserve traveler choice while keeping trips sellable

The system gives clients the impression of choice within constraints defined by the operator, so the resulting trip can still be shaped, quoted, and sold.

Quotes:

> To the client it's the illusion of choice with guardrails of things that the tour operator can only book.

### 🎯 The top of the funnel connects intent to sellable inventory

Marco Polo brings the traveler, agent, and operator together while shaping flights, hotels, transport, and experiences around the operator's real catalog, turning a request into a trip the operator can quote and sell.

Quotes:

> At the top of the funnel on one screen: the traveler, the agent and the operator's product shaping it together—the experience, the flights, the hotels and the transport in between.

### 🧭 Travel AI must be grounded in verified experience

The presentation contrasts general-purpose LLMs, which may rely on assumptions and unverified web data, with a system grounded in verified places and operator inventory so itineraries work in practice.

Quotes:

> AI and LLM wrappers plan like Columbus, based on assumptions and unverified data.

### 🧠 Marco Polo is a travel-specific model built from scratch

Marco Polo is presented as a large travel model built from scratch using the company's POI database and tour operators' data, rather than distilled from general-purpose language models.

Quotes:

> It's a transformer model built from scratch using POIs that we have on our own database and using basically tour operators' data. It's not a distilled model from the large language models.

### 🏷️ Each itinerary point carries structured provenance

The demonstrated itinerary includes a catalog ID, meter-level coordinates, and verification from both Marco Polo and the tour operator catalog.

Quotes:

> First of all it has a catalog ID, second it has coordinates down to the meter and third is verified by both Marco Polo and the tour operator catalog.

### ⚡ Itinerary creation can happen in seconds

The demonstration generated a customized Tuscany itinerary in 14 seconds, showing a major speed advantage over manually assembling comparable trips.

Quotes:

> Five days in Tuscany—two in Florence, Siena and San Gimignano... 14 seconds.

### 📧 Custom-trip planning is still highly manual

The company targets a workflow in which a client request typically arrives by email or form and requires four to five rounds of revisions and 15 to 20 emails between the traveler and specialist.

Quotes:

> A request comes in via an email or a form, then there's four to five iterations back and forth—15 to 20 emails between the client and the travel specialist, if not more.

## Transcript

all right I'd first like to introduce our CTO Eduardo Penichi Edo if you weren't here we wouldn't be doing this so thank you let's go thank you Mark in.
1298 a Venetian came back home after 24 years exploring Asia and he wrote a book describing places no one in Europe had ever seen he named.
It The Description of the World.
For centuries map makers drew from histories and tried to draw Asia and.
But no one had ever been there his name was Marco Polo and.
Fast forward two centuries after Columbus using the same stories tried to guess to reach Asia from the other side and you know very well where it went here in America and.
Marco Polo was an explorer who wrote about places he had actually been today AI and LLM rappers plan like Columbus based on assumptions and unverified data nowadays you might say he read it somewhere on the internet like.
Travel writer writing an itinerary of a tour operator's trip that it's never actually been on and.
Now everyone's seeing something like this before it writes beautifully and.
But when a travel specialist receives one from a client it's a nightmare they read a 15-day itinerary only to explain to the client that it can't it simply doesn't work and.
It writes it writes a nice itinerary it's just never been there and.
Every LLM you have used speaks a language that uses words we've built a language that speaks travel an LTM that's a large travel model it's name is Marco Polo and.
Marco Polo is a B2B tool for the itinerary creation and.
Proprietary model for tour operators and travel planners where you own your data and the travel expertise not the general AI and.
Marco Polo doesn't predict the next best words it determines the best sequence of travel events based on a tour operator's catalog with the traveler's demographic in mind then structures and writes a cohesive bookable itinerary it turns intent into reality words into a map a map into an experience and an experience into exploration now 20 years ago I couldn't find a travel software that could build and customize trips so I built one my record was five minutes for a fully customizable privately labeled web itinerary before it was even a category Eduardo show us one of Marco Polo's qualifying laps and.
Five days in Tuscany or two in Florence Siena and San Gimignano art in the morning and.
Reshape every brand's itineraries based on real inventory and experiences from the tour operator's catalog and.
To the client it's the illusion of choice with guardrails of things that the tour operator can only book to the operator it's a trip that the client's created that they can actually shape quote and sell and.
14 seconds and.
That used to be unimaginable Eduardo take us into day one of the itinerary let's check it out first of all it has a catalog ID second it has coordinates down to the meter and third is verified by both Marco Polo and the tour operator catalog now some.
Hard numbers first and.
Foremost our tour generation or trip generation held zero invented places and all the POIs come from our database of more than half a million places all verified by tour operators the generation is a super fast and cost a fraction of what general AI generally run now.
Tours and experience are a 271 billion dollar market and.
Two thirds of it still book offline with travel specialists about.
About 25 billion of that are custom trips the highest ticket item in travel and 16.8 billion of it still book offline that's our horizon now.
Custom travel planning is still archaic a request comes in via an email or a form then there's four to five iterations back and forth 15 to 20 emails between the the the client and the travel specialist if not more that.
Where we start at the top of the funnel on one screen one screen the traveler the agent and the operator's product shaping it together the experience the flights the hotels and the transport in between and.
Now there are three ways then to work with us developers just build on top of our API vista your trips in an interactive itinerary bookable atlas trip creation and customization based on your itineraries and your brand's voice we're building a future where an interactive map is the medium of collaborative travel planning experience today you saw a large travel model that creates an intelligent bookable itinerary next travelers plan with their tribe they get feedback from their friends and family they talk to the itinerary and it changes and.
On his deathbed Marco Polo's friend asked him to take it back none of these places are real Marco but he just said he replied to them I didn't say the half of the places that I saw and.
Show you the half of where we're headed six brands.
Live in 2026 if you plan tailor-made trips or you're looking to grow revenue in that direction or you want travelers to explore your itineraries visually instead of researching them let's talk and.
Thank you Mark well.
Done thank you Mariette.
Lots of greens maybe a red down here and.
Focus group and.
Chelsea's halfway Roger's a red and.
Let's start with Chelsea I.
Struggle here because I think you're building two separate products I'm I'm really curious more about the developer and the model aspect of this and I understand both of them are intertwined but I think the more application layer is just a really crowded space so that's where my flipping comes back and okay so just for the application with the booking layer like we don't actually we're not they're not actually using our system to book the trips it's the top of the funnel they can use whatever system they want to and then they can actually upload that itinerary if they want to to show it in the interactive itinerary with the customer and actually have the communications that instead of the emails being via email actually inside the itinerary as well so it all comes inside the itinerary and so when you developed this a little bit further how will you weight your focus and.
How will we weight our focus in the future is basically we're working with tour operator brands right now and DMCs to basically work with their travel agent networks as well and basically it would be I would say the the API focus would be where we would focus on the large travel model to actually use that as a as a basis for planning trips and a mapping layer and.
The LLMs aren't there yet right they're they're not an LPM as you positioned yourself but what's preventing them from going there and doing what you did and.
Why not like serving small medium and large models on demand for tour operators using their data it's something that everybody can do like we are moving first in the space and.
I mean like there is always a.
Twitter from I think a couple of weeks ago from Peter Doherty from X that said there is no moat that's the reality and we start first and we believe that the distribution so the side of actually the interactive itinerary is where our moat comes from the model side is a matter of execution and speed okay is it distillation that you're doing or you're creating content and are you distilling the larger language models and getting it to a more travel model and.
I can.
Hear you like I didn't it's two echoes distillation is obviously taking stuff from the larger large language models and actually improving upon them and creating your own model you mean distilling and no absolutely no is that is that transformer model built upon scratch using a POIs that we have on our own database and using basically tour operators data to it it's.
A distilled model from the large language model and thanks a lot Mark well done and.
Our last presenter please join me in welcoming Sarah Figueroa from Swivel and.
