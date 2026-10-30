# Agent rules (Director and Scout)

Generic rules distilled from an earlier autonomous sales-agent prototype. They describe how a rule-based orchestrator and a prospect scout should behave. They are design guidance, not shipped code.

Loovo override: wherever the prototype sent messages automatically, Loovo does not. Sends are manual and AI only drafts, except replying to a doctor who already wrote to Loovo. Contact hours follow Ley 2300 (Mon-Fri 07:00-19:00, Sat 08:00-15:00, never Sundays or holidays).

## Director (orchestrator)

1. Rule-based, no LLM. The orchestrator decides from pipeline state with plain business rules so that the loop never stalls on model quota or outages.
2. Each cycle reads the state (prospects, contacted, interested, paying, pending follow-ups) and creates work items with an explicit kind: `operation` (recurring work) or `improvement` / `research` / `experiment` (real business improvements).
3. Recurring operations, in priority order:
   - A paying client without a configured assistant: set it up immediately.
   - Prospects with no message drafted: draft first-touch messages.
   - Interested prospects: draft the closing follow-up.
   - Contacted prospects without a reply after 2 to 10 days: draft one follow-up.
   - Too few prospects (below a threshold such as 15): ask the Scout for more.
4. Improvement triggers: 10 or more messages with no reply, investigate why; 5 or more handled replies, audit tone; 3 or more prospects of an uncovered business type, propose a new template; first paying client, document what worked; 20 or more contacted, run a short-vs-long opening A/B test.
5. Never create a duplicate of a work item that is already pending.
6. Show improvements prominently on the board; hide recurring operations by default.

## Scout (prospect finder)

1. No LLM needed. Use structured data from a maps or directory source (name, phone, category, rating, review count).
2. Deduplicate by normalized phone and by name before saving.
3. Keep only plausible mobile numbers for the target country; discard landlines and malformed numbers.
4. Infer the business type from the category string with a plain mapping; unmapped categories fall back to a generic type and are reported so a new template can be written.
5. Store a short note with the evidence (rating, reviews, why it qualifies). Never store personal data of private individuals.
6. Target a limited set of city and sector combinations per run; never scrape in bulk.

## Seller / Responder conventions

1. Outbound messages are templates written in a warm, human register, split into short bubbles. They are queued as drafts, never sent by the agent directly.
2. One message per prospect per day at most.
3. Detect automatic replies from WhatsApp Business (fast, formal, long, "thanks for contacting us", "office hours") and do not treat them as a human answer. Wait several hours, then have a human follow up directly.
4. Replies avoid corporate filler and aggressive calls to action.
5. Notify the owner only on strong buying signals (demo request, price question, intent to hire).

## Engineering conventions worth keeping

- Template fallbacks are first-class: the loop must complete even if the LLM is down.
- Do not run LLM calls in parallel against a strict rate limit; serialize them.
- Normalize phones to E.164 and match exactly; matching by last digits causes collisions.
- Match payment references by full id, not by prefix.
- Keep recurring-run state (is the loop running, current session) in storage, not in memory, so a restart does not orphan it.
- Keep business-hour logic in one function and reuse it everywhere.
- Secrets live only in environment variables; never in files, chat or logs.
