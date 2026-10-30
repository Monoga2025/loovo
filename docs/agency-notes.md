# Agency notes: managed WhatsApp assistants for local clinics

Ideas from an earlier "managed WhatsApp AI assistant" agency project for dental and aesthetic clinics in Colombia. They complement the Loovo offer and do not override the `ventas/` rules. Nothing here is a real client price.

## Positioning

Do not sell "chatbots". Sell an assistant that answers patients, captures data, schedules or hands off to a human, and follows up so the clinic does not lose opportunities. Promise: more replies, more appointments, fewer lost messages. Never promise guaranteed sales or appointments.

## Stage guidance

- Sell first, deliver simply, measure, document, convert real cases.
- Do not build a SaaS, a login app or unlimited custom automation yet.
- Single outbound channel until the first founding clients close: hand-built lists plus manual WhatsApp.
- Ads and organic content come after the first paying client.
- Before building anything ask: does this help close a client? If not, not now.

## Niches

Priority: dental, then aesthetic medicine. Defer small restaurants, small barbershops, complex general health, lawyers and clients with no traffic.

## Fixed-scope offer (what is included)

- One WhatsApp number, one main AI flow built from the clinic's knowledge base.
- Up to 10 frequently asked questions answered automatically.
- Data capture (name, service, contact, urgency) and lead qualification cold / warm / hot.
- Up to 2 automatic follow-up messages.
- Human handoff through a shared inbox.
- A simple lead base, one monthly adjustment (up to 2 hours), a monthly report, support during business hours, one onboarding meeting (max 45 min) and one monthly review (max 30 min).

Not included (priced separately): paid ads, community management, advanced CRM or dashboards, several locations or numbers, complex integrations (billing, POS, ERP), mass broadcasts, 24/7 human support, sales guarantees and third-party costs (Meta, WhatsApp Cloud API, own servers). Small extras are quoted per item.

## Pricing ideas

- Anchor with a public price ladder (starter / growth / pro) and recommend the middle plan.
- A founding-client discount for a handful of clinics, justified as case-study and feedback value, is shown only to warm leads who saw the demo or asked price. Never in a cold message.
- Setup fee waived if the clinic activates after the pilot.
- Filter out a prospect who haggles in the first message or asks for unlimited custom work at the discounted price.
- A good founding client receives at least about 20 commercial conversations per month.

## Funnel sketch

Cold personalized WhatsApp, under-one-minute demo with the clinic's name, 10-15 minute diagnosis, close anchored on the middle plan, 45-minute onboarding, first result within 48 hours, report at day 3, day 7 and monthly, retention with a recovered-opportunities report, upsell, referrals. See `../ventas/playbooks/funnel.md` for the unified version.

## Selling rules

- Never say "cheap".
- Do not talk about n8n, models, webhooks or infrastructure to the prospect.
- Ask permission before sending a long demo.
- Personalize with a real observation (name, city, service).

## Suggested stack (internal, invisible to the client)

n8n for flows, a shared inbox such as Chatwoot for human handoff, Evolution API or WAHA for quick WhatsApp and the official WhatsApp Cloud API for serious or high-volume clients, Postgres or Supabase for data, a low-cost LLM through a router, a simple dashboard for reporting and a local payment provider. For premium clients, a third-party WhatsApp platform may be used if the client pays for it.

## Housekeeping rules from that project

- Keep few living files; archive old research rather than deleting.
- One decision lives in one place; if it changes, update that place and its dashboard.
- Remove old prices that contradict the current offer.
