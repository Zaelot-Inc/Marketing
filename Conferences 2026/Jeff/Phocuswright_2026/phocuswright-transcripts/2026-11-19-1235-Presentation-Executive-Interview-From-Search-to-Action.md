# Presentation + Executive Interview: From Search to Action

**Event:** The Phocuswright Conference 2026
**Speakers:** James Byers, Group Product Manager, Google; Mitra Sorrells, SVP, Content, Phocuswright
**Room:** Center Stage
**Start:** 2026-11-19 12:35 PM America/New_York
**End:** 2026-11-19 12:55 PM America/New_York
**Status:** completed
**Transcript word count:** 3861
**Session ID:** `78a1a9f5-4f5f-4fd8-8d8a-01334a1bea46`

## Summary

The session opened with a retrospective on how travel AI has evolved year by year: in 2023 it was novel but shaky and unreliable, by 2024 it was everywhere but still creaky and prone to hallucinations, in 2025 it became fluent with richer conversations and more accurate data, achieving habitual use at scale, and in 2026 it moved surprisingly quickly into being agentic. Rather than predicting the next label, the key question posed was when travel AI will be trusted the way travel search once was, with users confident about pricing, sourcing, and accuracy.

Google's current travel footprint was outlined as resting on massive-scale products—2.5 billion monthly active users on AI Overviews, billion-user products in AI Mode and the Gemini app, and Ask Maps now live in over 200 countries with new features like road trips. These sit atop the rapidly evolving Gemini model family and a data foundation combining web content, partner feeds for prices and availability, Google's Maps and Local corpora, and personalization signals from Gmail, Wallet, and Calendar. New AI Mode capabilities were highlighted, including end-to-end flight search with date and destination flexibility, bookable itineraries, price graphs and booking-timing guidance, points-and-miles integration across air and hotel, natural-language deal tracking, and a full hotel agentic booking flow from research through room selection to booking.

User behavior is shifting markedly in this AI-driven environment: queries in AI are three times longer on average than in Search, one in five queries is multimodal (voice or image), and users increasingly start in Search before moving into AI to dig deeper. Users now expect personalization as they share more context, but they also need to be convinced the AI got it right, which means trust still has to be earned.

Building that trust was framed around four principles: transparency about whether offers are commercial and how user data is used; privacy as a bedrock commitment even as expectations shift toward users willingly sharing more for better AI experiences; choice, meaning continuing to show every option, price, and booking path rather than steering to convenient answers; and simplicity, so partners only need one integration that works across all of Google's surfaces.

On the data and integration side, web and feed content remains foundational for upper- and mid-funnel discovery and comparison because it efficiently delivers accurate prices and availability. A newly announced Connected Apps platform offers a complementary path for deeper one-to-one relationships, loyalty, personalization, and brand voice, while the Universal Commerce Protocol extends into actions, checkout, and the post-booking relationship. Together with browser agents and account linking, these layers are meant to let Google and partners build trust collaboratively, with the ambition that today's uncertainty will look, in a few years, as distant as 2023 does now, as agentic travel AI capabilities are still only in their early stages.

## Key Takeaways

### 🧩 Use feeds, connected apps and protocols for different jobs

Google’s emerging model assigns different integration methods to different parts of the journey: feeds for discovery, comparison, price and availability; connected apps for loyalty, personalization and post-booking relationships; and connected apps or the Universal Commerce Protocol for checkout and other actions.

Quotes:

> Discovery and comparison is feeds... Loyalty and personalization, also powered by feeds, but also by connected apps... And actions and checkout, both connected apps and the Universal Commerce Protocol to go the last mile.

### 🧠 Travel AI needs structured, connected and attributable data

Incomplete or poorly connected airline data leads to inaccurate AI answers. Fare rules, ticket combinations and other travel datasets are not written in natural language, so they must be structured and linked in ways that let AI interpret them and reliably attribute its answers.

Quotes:

> A lot of the fare rules and all the intricacies of tickets... are not in machine-readable context today. And therefore, whatever conversational AI it is, is going to get stuck because it can't attribute them back together.

### 🔌 Access layers can hide airline-content complexity

Sabre’s strategy is to handle the complexity of NDC, EDIFACT, low-cost-carrier content, fare rules and combinations behind APIs or MCP, allowing travel companies and new entrants to focus on building user experiences rather than integrating every underlying format.

Quotes:

> What we've elected to do at Sabre is build an MCP platform on top of that where we take that complexity away and build the APIs.

### 🗣️ Travel queries are becoming longer, multimodal and personalized

As travelers move from traditional search into AI experiences, they provide more context through longer queries, voice and images, and expect answers tailored to their preferences and situation. Travel products should be prepared for richer inputs rather than relying only on short destination-and-date searches.

Quotes:

> Users are issuing much, much longer queries than they did on Search, 3 times the average query length in AI, and they're issuing them in new ways. 1 in 5 queries is multimodal, issued in voice or with an image.

### 📊 Extreme look-to-book ratios challenge travel economics

Conversational agents can generate dramatically more searches than traditional travel channels—potentially hundreds of thousands of looks for a booking versus roughly 1,000 for a classical travel agent. Every question still has to be answered by airline, hotel or car-rental systems, increasing infrastructure costs and supplier burden.

Quotes:

> We look at look-to-books at classical travel agents, it may be 1,000 looks before they do a booking. You look at some of the conversational AIs, they're in the hundreds of thousands.

### 🔔 Events are preferable to constant polling for changing travel data

Rather than having AI agents repeatedly ask whether prices or disruptions have changed, travel infrastructure can notify them when an update occurs, reducing unnecessary requests and system cost.

Quotes:

> Rather than asking us asking the airline every 15 minutes if the price has changed, how about if we tell you? How about if we tell you your Travelers are disrupted?

### 🤝 Trust requires transparency, privacy and meaningful choice

Travel AI must make commercial relationships, data use and recommendations transparent, protect user privacy and preserve meaningful choice. Users want confidence that the system considered relevant options, used appropriate data and can explain how it reached an answer.

Quotes:

> Users expect AI to do it for them, but they want to be convinced that AI did it right.

### ✈️ MCP and NDC are complementary distribution layers

The speakers do not expect airlines to abandon NDC, whose adoption is continuing. MCP can instead provide an access layer that brings multiple content sources together and may reduce the need for airline-specific direct NDC connectors, particularly for airlines that have not yet adopted NDC.

Quotes:

> I think they're complementary. But what I do think it replaces is this kind of fever that we had from some airlines at the time... bidding customer specific NDC connectors.

### 🛫 AI needs context about the travel product, not just the fare

Travel AI must answer experience questions that fare and schedule data do not capture, such as whether a flight has Starlink, how much legroom or seat width it offers, and whether it will be comfortable for a particular traveler. ATPCO is working to make airlines’ existing product and attribute data usable by AI through an airline context protocol.

Quotes:

> There is no fare that answers the question, is this going to be comfortable for me if I'm tall, right? Or I need extra legroom or I need extra seat width.

### ⚡ Predictive caching can shield suppliers from AI query volume

Conversational systems may generate far more searches than traditional travel channels, especially as agents repeatedly explore options. Travel platforms are therefore using predictive caches to answer language-model queries while reducing repeated calls to airlines and other suppliers; Sabre says its infrastructure handles about 20,000 transactions per second.

Quotes:

> A key part that's been super important at Sabre is getting a predictive cache in place... We do 20,000 transactions a second to be able to shield the suppliers, but providing all of the large language models with the answers they need.

## Transcript

so if it's not trained on it, it doesn't actually understand this data set as well as it should.
So the answers that come back are.
Incomplete at best.
And that's actually what leads to the inaccuracies.
And so what we're focused on, HEPCO has over 90% of the world's airfares in our database.
And what we're working on is turning that those data sets connecting them in ways that an AI can read it and understand it.
It's more than it's not as simple as natural language because these data sets are not built in natural language.
I think you point out a point which is a lot of the fare rules and all the intricacies of tickets of can I book this ticket with that airline and can I combine them, etc. A lot of that is done in machine-readable context today.
Yep.
And therefore whatever conversational AI it is, it's going to get stuck.
Because it can't attribute them back together.
So again, I think that's the key part of we can.
Either expose that complexity.
What we've elected to do at Sabre is build an MCP platform on top of that where we take that complexity away and build the APIs so that people where whether they are Travel agent today or a new player in the industry, have the ability to build the experience.
But where the complexity goes away and we'll handle that complexity.
Because the Traveler doesn't care if it's an NDC booking, an EDIFACT booking, or a low-cost carrier booking or how do you combine these things.
What they care about is their trip and the experience that they get at the end of the day.
And so for us, that's been an important part.
And we're all experimenting now.
Different AI solutions built on that MCP server.
And that's why I think opening up and having access to the APIs we have over 80 customers that either have live or in production in a way on their way into production.
So for me, that's the challenge is how do we take away the complexity and.
Do that in an effective way so that people can interact with conversational AI the way they want to.
So Steve, it seems sorry, do you want to add something?
Oh, I was going to say I give the AI a better fighting chance of understanding airline fare rules than human do.
Yeah.
Because it seems to me that.
If Sabre is building MCPs and you're building a.
Various layers to talk to your structured data and I'm sure your I mean, isn't that kind of increase the complexity of the industry?
Do we are we going to have to go back to more standards do you think?
I don't think so.
I think the standards we have now are just fine.
The MCP server is akin to REST or SOAP.
It's the way to access the data and the structure of workflows.
So maybe we a lot.
Of the partners that we have work with our API, they're not even using MCP server.
So it works.
It works well the infrastructure that we have today.
Why do you think that's needed?
You've got this handshake protocol that you've been developing.
Well, what.
We consider is a.
Kind of what Nicholas was describing, but even more than just fares and rules and combinability, Travelers want to know like does my flight have Starlink?
What's the like is it going to be comfortable?
Yeah.
There is no fare that answers the question is this going to be comfortable for me if I'm tall, right?
Or I need extra legroom or I need extra seat width.
And so the question is how do you answer those types of questions in conversational AI or even when agents are interacting with each other?
To answer a Traveler's question.
And that data exists.
It just isn't in a format that AI can read it and understand it.
And that's what we're focused on at HEPCO is taking these data sets that airlines already provide that airlines want Travelers to understand.
What is in the bundle?
What's the product look like?
What's it going to feel like?
And.
Doing your typical flight search with an O&D and dates doesn't answer that question.
So that's really what we're focused on.
And what we are calling that internally is more of an airline context protocol.
And then I think the other part that's super important I go back to look to book all these questions we're now asking all of these somehow have to be answered by the airline systems.
Whether it's a request for a flight or whether it's a comfortable seat.
And we look and look to books at classical Travel agents and maybe a thousand looks before they do a booking.
You look at some of the conversational AIs, they're in the hundreds of thousands.
And so a key part is okay, how do you handle that in.
Given for every airline or every hotel or every rental car to be able to answer all those questions and respond back?
So for me, the other part that's been super important at Sabre is getting a predictive cache in place and no one does it at the scale.
I mean, we do 20,000 transactions a second.
To be able to shield the suppliers but providing all of the large language models with answers they need.
The other one which is agents are fantastic but we're starting to see things now like continuous polling.
Is there a better price?
Is there a disruption happening?
Because you see players building AI solutions to handle those pieces.
Again.
All of that drives data in the system system cost tokens and yes volume.
So the other part I think is the industry changing as well.
We just brought out kind of where we can.
Tell people when things change.
So you can subscribe on that.
So rather than asking us asking the airline every 15 minutes if the price has changed, how about if we tell you?
How about if we tell you your Travelers are disrupted?
So that the conversational AI can do the fantastic piece of work that they do around those pieces.
Steve, you and I talked a little bit about caching yesterday and really if.
It's not live, is it good enough?
I think it depends on where the Traveler is in their journey.
What we've seen is that for.
The very early stage when the AI is trying to figure out where should I go on holiday in December, it creates a lot of search volume.
But that's the truth of a lot of solutions out there, not just AI.
When it comes to more transactional requests, the volumes have been within the norm of the industry.
Like the volumes we're seeing today are not anything crazy.
Okay.
So I do think that it will change over time as maybe more of that early funnel.
Gets captured by the agent.
But today on the transactional stuff, it's no different than a regular OTA.
I want to touch on NGC for a minute because Sabre's message to the market has been that MCP can replace NGC, but MCP is just a connector.
So Brett.
Are airlines you have airline owners.
Are airlines going to abandon NGC?
No.
I think airlines that have NGC are a.
Seeing good success with how it's been adopted.
More airlines are deploying it this year.
Delta has announced that they're going to be deploying NGC by the end of the year.
So I don't see airlines walking that back.
What it may cause is airlines who haven't yet adopted NGC to consider other options for getting their offers to market.
But I think the end goal remains the same, which is we want to get our offers in front of Travelers in a way that is well adapted to what the Traveler is looking for.
And that's what dynamic offers, dynamic bundling is all about.
And I don't think AI changes that I actually think AI accelerates that.
Yeah.
And I also think that.
Like MCP and NGC or two sides.
Of the same coins.
Like even with MCP, you're going to have to define like what data you pass in, what data you get out.
And so it's going to be the I mean, it might be NGC offered via MCP, but we need some kind of standard.
Yeah.
And I don't think that and.
Seen the same article that we put out, but NGC a lot almost every airline has it one way or another.
What we see MCP being able to fill the roles.
I think a lot of airlines are struggling with the NGC direct only.
And what an MCP can help replace that is by bringing all the content sources together.
NGC is a great channel, especially for airlines going down modern retailing because it's really attuned to what offers and orders are.
So I think your comment is right.
They're complementary.
But what I do think it replaces is this kind of fever that we had from some airlines at the time.
And many are backing back now bidding customer specific NGC connectors.
I want to ask you all about I mean, you spoke about look to book ratios and you say right now they're in within industry norms.
But that's probably going to change.
How do you see economic models evolving as a result?
Well, I think the big question on a lot.
Of providers' mind now actor.
In the industry is does.
Search needs to be monetized?
Today you go on any online travel agency or any provider that offer these services and you don't have to pay anything.
When agents are going to be browsing the internet of agents and making searches like maybe we need to start having some tool in place whether it takes the form of a transactional fee or tokens in the same way that a lot of the providers in the AI industry are monetizing today.
That's still up for discussion.
But that's definitely something that's going to change.
Brett, do you think that we go back more to the realms of surcharging like we saw with NGC to encourage the adoption of those standards?
I don't know about airline appetite for broad.
Surcharging.
We've certainly seen that with a handful.
What I think is different though about this model is the internet is free.
And so what powers the internet is marketing.
And.
When you're using agents I don't think that's a free business model.
It's too expensive to actually do the compute and the inference required to actually power it.
And so I think I.
See it moving to more of a subscription model.
And we'll see how that impacts travel.
But I don't think it's unreasonable to expect if you want to set if you want to have your own personal travel agent and you want to subscribe to that for 20 bucks or 50 bucks or whatever the price is per year, I.
That's a subscription model that could work.
Okay.
And I think we're going to see all types of those models.
And that's a fun part of the innovation that's happening now because both the pricing models as well as the servicing models are developing in what's a whole new channel.
So I go back to the point there's going to be people that want to book indirect the classical way.
There's people that's going to rely on their agents.
There's people that's going to want to book directly with their preferred airlines.
And you're going to find financial models that solve for all three of those.
Whether it's your personal agents booking at your personal airline such as Chat.
GPT plugin for one specific airline yeah.
That will have a model that will be different from if you've gone to a conversational AI and started your search.
Do you want to add something?
No. That's fine.
Yep.
Okay.
So when the traveler blames the airline when the trip goes wrong why would.
They keep letting agents sell their product?
And we have seen that with United and yes it's early days but what let's talk about the factors that are really behind Scott Kirby's decision.
Is it we don't say it's volume of searches.
Thanks everyone.
Wonderful to be here I am going to ask you to go on a.
Journey with me.
Briefly.
A journey where I want you to remember back a.
Long time ago.
Way back in time.
A time some of you probably have forgotten.
So close your eyes take a deep breath relax does.
Anyone here remember what the world was like in 2023?
No?
Seems like a distant memory?
Well I want you to think about how you would describe travel AI.
When you go back to 2023.
What word would you use in that year?
The word I would use is it was novel.
Lots of promise.
A little bit shaky.
But you could see there was a seed.
A germ of something quite spectacular for our industry back at that time.
One year later I would say that that word is everywhere.
Every launch.
Every surface.
Every company.
Everyone was racing towards this future.
And the experience was better but it was still a little bit creaky.
It wasn't always backed by data.
There were hallucinations.
It was a little bit of a mess.
2025 I'd say got fluent.
We started to see richer deeper conversations.
More accuracy.
Better data.
A very useful set of services.
And travel AI became a habit in 2025 for lots and lots of users.
Which is quite remarkable given the short time scales here.
At scale.
Now in 2026 I think we very quickly went to agentic.
Surprisingly quickly.
I think if we look at the timeline here.
Now you might think I'm going to predict that word for 2027 or 2028 but if I do that I'll get it wrong and next year MITRA will play it back on the big screen and I'll be embarrassed and you'll all laugh.
So I'll ask a different question.
When will travel AI be trusted?
In what year can we look and say that.
Millions of people rely on these services and deeply trust them?
I believe users did deeply trust travel search a few years ago.
Our data shows this.
Our research shows this.
They understood what they were getting.
Who they were getting it from.
What prices were accurate.
What weren't.
This system worked.
But when will that be true for travel AI?
So before we look to the future let's talk a bit about where we are today.
And what travel looks like at Google.
We're privileged to have some very large services that travelers use nonstop for their travel needs.
2.5 billion monthly active users use AI overviews.
Both AI mode and Gemini app.
Our billion user products.
And Ask Maps is growing incredibly quickly.
It's now live in over 200 countries.
It has wonderful new features including some announced this week.
Around road trips and building this really connected journey inside the Maps app for travel use cases.
These sit atop a wonderful model.
And you've seen really rapid evolution of the family of Gemini models with new launches now every few weeks.
And of course underneath this sits an incredible wealth of data.
The content across the web from human voices.
From authoritative sources.
Feeds that we collect and gather from all of you for prices and availability.
And attributes.
The data Google knows about the real world from our Maps corpus.
Our local corpus.
And.
Gmail wallet.
Calendar.
Personalization signals.
All of this together lets us build these wonderful and.
Capable AI travel experiences.
And most of our newest experiences go live in AI mode first.
A couple of these that we've launched recently are end-to-end flight search.
Both understanding date and destination flexibility.
Looking across millions of combinations of flights in seconds.
And going all the way to itineraries you can click through and book with the airline or OTA of your choosing.
And of course we're.
Not just showing you itineraries.
We're telling you when you might book.
We're showing you price graphs.
And we're letting AI adapt that experience to where you are in your journey.
We're also doing it for points.
And miles.
Incredibly important for our users and our travelers.
To see AI reflect their brand preference.
To reflect those of you they trust with their travel.
So we're doing this both for air and hotel and across many other verticals as we expand over time.
Helping with that really difficult calculus.
That puzzle of when to earn.
When to burn.
How it all fits together.
We're also letting users track all of these things.
In natural language.
So over time we want the user to be able to say I want.
To go to Spain.
For a week.
In the summer.
Just track everything and tell me when there's a great deal.
And you see us working through that experience in flights and hotels and building up that capability.
And of course we've launched hotel agentic booking.
So being able to go all the way from some early research down to choosing a destination.
Choosing a hotel.
Understanding how it fits in a neighborhood.
Learning about its amenities.
About the view.
About nearby restaurants.
Choosing a room.
Based on rich data about the rooms themselves.
With accurate prices.
And going through to book right in AI mode.
And this is the tip of the iceberg.
There's many other features in the AI mode.
You should try out around transportation search and trip planning and a whole range of other features.
User habits are changing quite quickly in this world.
We see that users are issuing much much longer queries than they did on search.
Three times the average query length in AI.
And they're issuing them in new ways.
One in five queries is multimodal.
Issued in voice.
Or with an image.
At.
Google's scale the absolute numbers behind that are astounding.
That is an astounding volume of queries that use that are multimodal.
To build up their plan.
And users often start in search and then jump into AI to dive deeper.
To ask tricky questions.
Across travel queries now users expect personalization.
As they give us more context they expect better answers.
Users did not always expect this from Google search.
And this is a relatively new phenomenon.
They want AI to do it for them.
But they want to be convinced that AI did it right.
And to do that convincing.
And today we still have a ways to go together to build up that trust.
So there are a couple of principles that fit here in our world about.
One is transparency.
How we might build up that trust.
Isn't offer commercial.
Is there is it an ad.
Or is it the AI doing its best job to serve a user need.
What is Google using your data for that we might crawl or have in feeds or connect through MCP.
How are we using that data.
How are we presenting it to our users.
Privacy for us is bedrock.
Here are two expectations are changing.
We believe that this users entrust the most a.
Private and sensitive details of their life to Google.
And we want to be very very careful to honor their privacy needs.
And give them control.
But expectations are changing.
And when partners can benefit from a bit more context.
Users expect that the AI experience will be better when they share a bit more information.
Choice.
We are built on this foundation of showing our users every option.
Every price.
Every way to book.
And we believe that remains incredibly important.
That we're demonstrating that value.
In the AI world.
That we looked at everything.
We didn't just pick the convenient answer.
We helped pick the best answer.
The best partner.
And using the right data for the job is central to those principles.
We'll talk more about that in a moment.
And finally you all should only have to do one.
Integration that works across all of Google.
And so increasingly we're converging these experiences.
So how are we evolving.
And the way we gather data to work in a more coherent way for you.
First the.
Web and feed content that we've built up together over years and decades is still at the foundation.
Especially in the upper and mid funnel journeys.
When it's incredibly efficient to use our feeds.
To show super accurate prices.
To show availability.
Versus going out and hammering your websites for hours.
We've also just announced the connected apps platform which gives you a different way.
And bring your brand's voice directly to users on our platform.
A new way to integrate with Google.
And connected apps are a way to think about the deeper one to one relationships.
The loyal users.
The actions users need to take.
That are not well served by the world of the web.
Or the world of feeds.
And so when you put all this together user.
The right data for the right job ends up.
Being a trust building exercise.
Discovery and comparison is feeds.
Users are learning that we are showing them an accurate price.
An accurate availability.
Loyalty and personalization also powered by feeds.
But also by connected apps that bring your brand directly to users.
And help them have that one to one connection.
And actions and checkout both connected apps and the universal commerce protocol to go the last mile and that's not just book.
Prebooking.
It's also the post booking relationship that you can build in the connected apps world.
And of course all of this is sat on the foundations of the.
Content across the web and human voices.
Browser agents filling in the gaps.
And account linking helping build that connection of which users use trust which services.
So we believe we can only do this together.
That we have to work in a principled way to build up trust in the AI world.
There's still a ways to go.
We're not there.
But you can imagine coming back in a couple of years at a focus right and thinking back way way way back to 2023 and it being a distant memory.
That users didn't really know when to trust.
Who to trust.
What was going on.
Where the transparency was in this ecosystem.
We're thrilled to partner with you on this journey.
And we believe that the capabilities and the growth we'll see in the agentic world in the future we've only just seen the very beginnings.
So thank you.
And on a personal note thank you again for a wonderful focus right here in Miami.
It was a great one.
And now please welcome focus right Mitra Sorrels.
