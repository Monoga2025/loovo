# Unified sales funnel (6 stages)

One funnel for Loovo outreach to aesthetic and dental clinics. It merges three earlier copies: the six-stage funnel prototype, the "phases" checklist in `../checklist_ejecucion.md` and the funnel notes of the agency project. Where they disagreed, this file keeps the version closest to how Loovo actually sells (mystery-shopper audit, manual sends, deposit before build).

## Non-negotiable rules

1. Sends are manual. The AI drafts; a person sends. The only exception: the AI may reply on its own to a doctor who already wrote to Loovo (from touch 2 on), speaking as Loovo, inventing no data or prices and never posing as a patient. Mystery-shopper chats are never continued by AI. The AI never starts calls.
2. Contact window (Ley 2300): Monday to Friday 07:00-19:00, Saturday 08:00-15:00 (Colombia time). Never Sundays or public holidays.
3. A message that still contains a placeholder (`[LINK_...]`, `{{field}}`) is never sent. If data is missing, a human takes the case.
4. Never invent results, testimonials or figures. Use only evidence in `../state.json`.
5. Cold messages never reveal promotional or founder pricing. Price appears only after the prospect saw the demo or asked.
6. Never promise guaranteed sales or appointments.

## Stages

| # | Stage | Goal | Exit criterion | Reference |
|---|---|---|---|---|
| 1 | Verifiable problem | Qualify the clinic before spending effort | At least one observable response leak (slow reply, no welcome message, generic answers) | criteria below |
| 2 | Consultative diagnosis | Quantify the leak with the doctor | Doctor accepts to see a demo | script below |
| 3 | Specific AI demo | Show an assistant configured with the clinic's own services | Doctor tries the demo or asks for price | `../agentes/` |
| 4 | Pilot | Deliver a fixed-scope pilot after a deposit | Service order signed, deposit received | `../orden_de_servicio_loovo.md` |
| 5 | Measured result | Report numbers from the pilot | Metrics report delivered; fail-safe never triggered unattended | checklist below |
| 6 | Continuity | Convert the pilot into a monthly service, ask for referrals | Monthly plan or documented refusal | this file |

### Stage 1 - Verifiable problem

Qualify only if all four hold:

1. A physical location verifiable on a map or real storefront photos.
2. An active commercial WhatsApp number published on Instagram, Google Business or the website.
3. A catalog of several high-value services (for clinics: smile design, implants, aesthetic medicine).
4. At least one visible leak: replies slower than 2 hours, no welcome message, or answers that do not qualify the patient.

Evidence from the mystery-shopper audit goes in the evidence folder and the failure in `state.json`.

### Stage 2 - Consultative diagnosis (15 minutes)

Tone: technical colleague, no sales pressure. Three blocks:

- 0-3 min, framing: mention one real, specific thing about the clinic's work, then ask who answers the chats today.
- 4-10 min, quantifying the pain: time to reply during procedures, evening and weekend inquiries, repetitive questions, leads that said "I already quoted elsewhere".
- 11-15 min, synthesis: summarize the leak in the clinic's own numbers and offer a no-commitment prototype with the clinic's name.

Money-leak estimate (use the clinic's real numbers, never as a claim):

```text
lost leads / month  = chats per day x 30 x share answered late
estimated loss      = lost leads / month x average ticket x close rate
```

Break-even framing: if the pilot price is below the margin of one rescued high-ticket patient, one rescued patient pays for the pilot. State it as arithmetic on the clinic's numbers, not as a promise.

### Stage 3 - Specific AI demo

A short (about 60 seconds) demo with the clinic's name and real services. Ask permission before sending anything long. Official WhatsApp channels are preferred over unofficial ones for clinics that care about number safety; explain the ban risk of unofficial bridges plainly.

### Stage 4 - Pilot

Fixed scope, deposit up front (50 percent), balance when the clinic sees it working. Scope and exclusions are written in the service order; extras are quoted separately.

### Stage 5 - Measured result

14-day rollout checklist:

| Day | Milestone | Acceptance |
|---|---|---|
| 1 | Deposit confirmed | Payment proof validated |
| 2 | Service catalog and hours received | Clear prices and rules |
| 3 | Catalog loaded into the assistant prompt | Automated test passes |
| 4 | Joint test session with the client (20 min) | Express approval, balance paid |
| 5 | Go live on the client's WhatsApp line | Flow in production |
| 6-13 | Daily monitoring and small adjustments | Zero open incidents |
| 14 | Close-out and metrics report | Count of rescued quotes and booked appointments |

Fail-safe: if an API fails, the server goes down or WhatsApp disconnects, (1) pause the automation immediately, (2) let chats reach the clinic's own WhatsApp Business app untouched, (3) if a holding message is needed, a human sends a transparent one ("we are attending directly, a team member will answer you shortly"), (4) alert the Loovo team and restore service within 15 minutes.

### Stage 6 - Continuity

Monthly report of recovered opportunities, one offer to move to a monthly plan, a referral request, and a note in `../state.json`. Upsells (campaigns, scheduling, CRM integrations) are separate quotes.

## Outreach cadence (draft only, human sends)

Three low-pressure touches, spaced across about a week, always inside the Ley 2300 window:

1. Day 1, courtesy audit: praise one real piece of work, name one observed leak, offer a short video. Sell nothing.
2. Day 3, silent value: one factual data point relevant to the clinic, no reproach.
3. Day 6, graceful exit: leave the door open, ask for nothing.

Any prospect who asks not to be contacted is archived immediately and never messaged again.

## Related files

- Operational detail and message templates: `../flujo_maestro_reactivacion_loovo.md`, `../toques_2_3_lote1.md`.
- Pipeline state: `../state.json`.
- Objection handling: `objections.md`. Agent rules: `agent-rules.md`.
