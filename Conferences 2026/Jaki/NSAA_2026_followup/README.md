# NSAA 2026 "Mountains of Data" Follow-up

Event: NSAA Mountain Technology Symposium, Hood River, OR, 2026-10-08. Speakers: Jaki Levy (Zaelot), Brandon Quinn (Get Ski Bots).
Sender: Jaki Levy. Deck: `../Mountains of Data Managing the New Data Economy (1).pdf` (27 slides).

## Files
- `email_template.html`: HubSpot coded email template, merge tags for first name and company.
- `email_preview.html`: local preview with sample values (not for upload).
- `optin_landing_page.hubl.html`: opt-in landing page source (built in HubSpot once the form exists).

## Merge tags used
| Tag | HubSpot property | Fallback |
|---|---|---|
| `{{ personalization_token('contact.firstname', 'there') }}` | Contact First name | "there" |
| `{{ personalization_token('contact.company', 'your team') }}` | Contact Company name | "your team" |

Suggested subject: `{{ personalization_token('contact.firstname', 'Hi') }}, the Mountains of Data deck`
Alt subject: `The Mountains of Data deck, as promised`
Preview text (already in template): "Slides from our NSAA session in Hood River, plus the three questions we left you with."

## Steps (in order)

### 1. Attendee segment (Jaki's badge scans / notes)
- [ ] Get Jaki's list into `Marketing/NSAA_2026_followup/attendees.csv` (columns: First name, Last name, Email, Company, Title).
- [ ] Match against existing HubSpot contacts, create the missing ones (approval needed).
- [ ] Create static segment "NSAA Mountain Tech Summit 2026 - Attendees" and add them (approval needed).
- [ ] Set new contacts as Marketing contacts so they can receive the email (HubSpot UI).

### 2. Upload the deck (HubSpot UI, ~1 min)
- [x] Uploaded 2026-10-09: https://24292391.fs1.hubspotusercontent-na1.net/hubfs/24292391/Zaelot%20Mountains%20of%20Data%20Managing%20the%20New%20Data%20Economy.pdf
- [x] `deck_url` filled in email template and landing page.

### 3. Opt-in form (HubSpot UI)
- [ ] Marketing > Forms > Create > Embedded form, name "NSAA 2026 - Keep me posted".
- [ ] Fields: First name, Last name, Email (required), Company name.
- [ ] Data privacy and consent: "Consent checkbox for communications" bound to the Marketing subscription type, unchecked by default.
- [ ] Thank-you message: "Thanks, you're on the list. Grab the deck any time from the link on this page."
- [x] Published 2026-10-09: "NSAA 2026 - Keep me posted", GUID 18a22a8b-d320-4e0f-8719-9b86d601ea96, share link https://share.hsforms.com/1GKIqi9MgTg-HGZuG1gHqlgego4n

### 4. Landing page
- [x] Draft created 2026-10-09: landing page ID 223966724978, template ID 223972352630 (custom/content-mcp/pages/nsaa-2026-keep-me-posted.html), slug `nsaa-2026-keep-me-posted`. Editor: https://app.hubspot.com/pages/24292391/editor/223966724978
- [x] Published 2026-10-09: https://24292391.hs-sites.com/nsaa-2026-keep-me-posted
- [x] `optin_url` filled in email template.

### 5. Email
- [ ] Design Tools > new coded email template, paste `email_template.html`.
- [ ] Create marketing email from that template, From: Jaki Levy, reply-to jaki.levy@zaelot.com.
- [ ] Confirm Jaki's meetings link (`meet_url` defaults to meetings.hubspot.com/jaki-levy1).
- [ ] Recipients: the NSAA 2026 segment. Send test to Jeff and Jaki, then schedule.

## Open questions
- Brandon Quinn / Get Ski Bots: OK to name him and share the co-presented deck? UNKNOWN, confirm with Jaki.
- Jaki's list size and format: UNKNOWN.
- Which Jaki meetings link is current (`jaki-levy` vs `jaki-levy1`): UNKNOWN.

## Log
- 2026-10-09: Slack DM to Jaki asking for attendee list, email review, Brandon OK, booking link. https://zaelot.slack.com/archives/D08NSLE0ZMM/p1791511783931979
- 2026-10-09: Gated version tried and reverted; email links straight to the PDF, landing page is opt-in only (draft, ID 223966724978).
