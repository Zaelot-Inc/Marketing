# CTOs: your CMS migration estimate is out of date

*Manual migrations scale with page count and check only a sample. An agentic pipeline moves the cost into setup, checks every record, and makes cutover repeatable. Here's how it works.*

Oct 7, 2026 · @Ramiro Visca and @Jeff Galusha

If you lead engineering, you've probably had this request. Marketing wants off the current CMS, and they want to publish without filing tickets. You already know the target architecture: a headless CMS, a modern front end, and content as structured data. What keeps the project stuck on the roadmap is the estimate, and the risk that comes with it.

That estimate rests on an assumption. This piece explains the assumption, why it no longer holds, and what a migration looks like without it.

## Why your estimate looks the way it does

Every traditional migration estimate rests on one assumption: a person has to touch every page.

- A project owner inventories the site in a spreadsheet.
- Content editors or junior developers copy each page into the new system, fix the links, re-upload the images, and rewrite the metadata.
- Developers rebuild every template and component by hand and wire each one to the new content model.
- QA testers check a sample of the work, because checking all of it would take too many hours.

Every one of those costs grows with page count. A site twice the size takes twice the people or twice the months.

Sampling creates the risk. The records nobody checked hide the broken links, dropped fields, and missing redirects. They surface on launch day as lost traffic and support tickets. That risk is why migrations get padded, phased, and pushed to next year.

## The two migrations that make it worse

**1. Several CMSs consolidated into one.** Large organizations often run several CMSs behind one domain. A typical mix: a legacy platform for the core site, a site builder for campaign pages, and something else for docs or the blog. Each has its own content model, auth, and URL conventions. Each also holds its own copy of content that should exist once.

Consolidation multiplies every migration task by the number of source systems. It also adds work that only exists at the seams: duplicate entries, URL collisions, and taxonomies that were never designed to meet. Done by hand, each extra source is close to a separate project on the estimate.

**2. A vibe-coded or no-code site your team has outgrown.** No-code site tools (Builder, Framer, and similar) and AI code generators (Lovable, Bolt, v0, and similar) get a site live fast. Under the hood, the result often varies page to page. Content is embedded in components or layout. There's no real content model, and the structure was never written down, so there's no clean export. Some of these sites render mostly in the browser, which leaves crawlers and AI assistants little to read. Done by hand, someone has to reverse-engineer the structure page by page before any content moves.

## What changed

AI agents can now do the page-by-page work: reading, classifying, mapping, transforming, and checking. That moves the cost out of labor per page and into setup. Setup means the crawl standards, the content specification, the mappings, and the validation rules. Once those exist, page 5,000 costs about the same as page 50.

It also removes the reason for sampling. When machines check every record, nothing hides until launch. At Zaelot, every step is validated against rules agreed up front. Senior builders spend their time on the decisions that need judgment. Here's the pipeline.

## How the pipeline works

Zaelot runs these migrations into a headless CMS, usually Contentful. The stages are the same whatever the source.

### 1. Crawl and classify the whole site

*Replaces the spreadsheet inventory, and the missing export.*

One agent crawls every page. It classifies each one against standards set with your team: expected templates, composition, and structure. For no-code and vibe-coded sites, agents read the rendered pages and the code together. That's how they infer the structure nobody wrote down. A second agent reviews the outliers independently and records why each page fell outside the standard.

The inventory also captures what lives around the content: forms, embeds, tracking, and third-party scripts the new site needs to carry over.

Every page enters the migration with an assigned strategy: migrate, transform, consolidate, redirect, or prune.

### 2. Write the specification first

*Replaces conventions that drift from one person to the next.*

Before any content moves, the team writes a governing content specification. We call it the constitution. It defines the target content model, the taxonomy, the quality bar, and the reasoning behind each decision.

Every agent checks its output against the constitution through two gates. Does the field match the model? Can the agent explain why the transformation follows the rules? Output that fails either gate is rejected or routed to a person. The constitution starts from standards Zaelot built over earlier migrations. Our builders adapt it to each engagement's sources, model, and priorities.

### 3. Agents propose mappings, and people decide

*Keeps judgment with people, and production under control.*

Agents read the source structure and the target schema, then draft the field mappings. Your team and ours approve, reject, or refine each one. The content model lives in code and gets committed and reviewed like any other engineering change.

Changes to the live space follow diff-then-apply. The full plan prints before anything is sent. Applying it requires a typed confirmation. Running the same migration twice changes nothing the second time. Destructive operations, like deleting a content type or dropping a field that holds data, are held for a person. They're never applied automatically.

<!-- REVIEW (Ramiro): confirm this front-end step matches how Zaelot actually delivers before publishing. Only source so far is the Beachfinder PoC plan, not a delivered project. -->
### 4. Generate the front end from the same model

*Replaces months of hand-built templates.*

The content model that governs the migration also drives the new site. Each content type maps to a component. Agents generate templates and components against the approved schema, so the front end and the content follow the same specification. Builders review the generated code as pull requests, to the same standard as their own.

Hand-built templates used to take a team months. Generating against a reviewed model shifts that time to review. It also gives the visual parity checks later in the pipeline a precise target.

### 5. Extract and load with coordinated agents

*Turns each extra CMS into an adapter, not a project.*

The work splits along standard ETL lines. Extraction is source-specific and uses each system's API and documentation. Transformation and loading are platform-independent. Each added source means one more extraction adapter. The transform and load stages, and the whole validation suite, get reused.

Each agent handles a schema, a component, or a page. Extraction and transformation run in parallel for each source system, and progress is visible in real time. Failed records retry automatically. Anything that still fails is flagged as a recoverable record for review instead of being silently dropped.

### 6. Validate every record

*Replaces sampling.*

- **Field parity.** Source and destination are compared field by field at the component level, using the structural mappings.
- **Completeness.** Checks confirm nothing user-facing was dropped. Every deviation goes to a person. Some gaps are intentional pruning and some are defects.
- **URLs and redirects.** Validated in two steps. Each legacy URL maps to the right new URL, and each new URL resolves.
- **Assets.** Verified by hash against the source.
- **Visual parity.** DOM structure and rendered CSS are compared per component, against a design reference when there is one.
- **Accessibility.** Alt text, headings, and ARIA handling are checked against WCAG 2.2 AA.

The full suite runs for every locale. People review a prioritized set of pages plus every flagged deviation.

### 7. Rehearse until cutover is routine

*Takes the risk out of launch day.*

Because the pipeline is automated and idempotent, the team runs full rehearsals again and again. Each runs in an isolated environment with its own URL.

Cutover starts in shadow mode with a set cutoff date while the legacy site stays live. The team watches for content divergence and runs a final sync for anything created after the cutoff. A rollback path stays open throughout. Editors keep publishing on the legacy site until the switch, so there's no long content freeze. If something goes wrong, traffic goes back to the old site.

## What you end up with

Along with the content, you get a front end built for what comes next.

**Server-rendered by default.** The new front end renders on the server, with a framework like Next.js. Every page arrives as complete HTML, with its title, headings, meta description, canonical tag, and structured data in place.

**Readable by search and AI.** SEO depends on that complete HTML. So do AEO and GEO, because AI assistants can only cite what they can parse. Content lives in a structured model, so sitemaps, structured data, and files like llms.txt are generated from it instead of maintained by hand.

**Fast where it counts.** Server rendering, image optimization, and code splitting are defaults. That puts Core Web Vitals within reach on mobile and desktop.

**Composable and API-first.** The site is built from a component library mapped to the content model. Editors compose new pages without engineering. The CMS API delivers the same content to the website, apps, and other channels without duplication.

**Accessible from the start.** The WCAG 2.2 AA checks that ran during the migration keep accessibility debt from creeping back.

<!-- REVIEW (Ramiro): confirm Zaelot offers the post-launch AI harness as described (agents suggesting and applying AEO changes within editorial rules) before publishing. -->
**An AI harness after launch.** The agents, specification, and validation rules that ran the migration stay in place after launch. Agents propose changes that improve AEO, like clearer headings, better FAQs, or richer structured data. Those changes apply only within rules your editorial team sets. The same validation gates that protected the migration protect every change after it.

## What it does to your estimate

<!-- REVIEW (Christian or German): confirm the source for the 1/4 cost figure and the 50%-shorter timeline before publishing. Basis is the ALGV re-estimate. -->
**A quarter of the cost, in half the time.** On a recent project, Zaelot's estimate came in at about a quarter of what the same migration was quoted three years ago. The timeline was at least 50% shorter.

**The cost curve flattens.** Most of the effort is setup. After that, each added thousand pages means more machine time and a short list of flagged records. It doesn't mean more people or more months.

**Page 5,000 gets the same treatment as page 50.** A manual team's attention fades over thousands of pages. A pipeline applies the same rules and gates to every one. Failures surface before launch as flagged, recoverable records.

**The risk premium goes away.** Estimates get padded because nobody can see what sampling missed. With every record verified and cutover rehearsed, there's far less unknown to price in.

<!-- REVIEW (Jeff): confirm the source for the three-senior-to-one-non-senior staffing ratio before publishing. No source found in the repo. -->
**A small senior team carries the work.** Zaelot staffs these migrations with a small group of senior builders. That matches how we staff overall: roughly three senior professionals for every non-senior. Their time goes to approving mappings, judging flagged deviations, reviewing generated code, and shaping the taxonomy with your team.

## What it takes from your team

- **Read-only access** to each source CMS and the current site, so agents can crawl and extract without touching production.
- **A content owner** who can make decisions on the model and taxonomy, and approve or reject mappings on a regular cadence.
- **An engineering point of contact** to review the content model and generated front-end code, and to own the cutover plan with us.

## Run the numbers again

If a migration has been sitting on your roadmap, pull out the last estimate you got. Zaelot will walk your team through the pipeline against your actual site. We'll show you what the same project costs today and help you build the business case for your executive team.
