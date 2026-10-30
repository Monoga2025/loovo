# ventas/prospecting

A small self-contained TypeScript sub-project: a SQLite prospect store (`better-sqlite3`) and a synthetic lead generator, ported from a public prototype.

Important: the "scraper" calls no website. `ScraperEngine` generates fictional businesses (generated names, `555` phone numbers, `example.com` addresses and assets). It is a data-model and idempotency prototype, not a live scraper. Never store real clinic or patient data here; real leads belong in private storage.

## Run

```bash
cd ventas/prospecting
npm ci
npm test            # vitest, 4 tests
npx tsc --noEmit    # type check
```

## Layout

- `src/database.ts`: schema and idempotent saves (`UNIQUE(business_name, city, state)`).
- `src/ScraperEngine.ts`: fake prospect generator.
- `src/types.ts`: shared types.
- `tests/database_scraper.test.ts`: schema, idempotency and generator tests.

Not ported: the original payment-link and e-mail generator tests (the modules they covered were not in the source) and any e-mail dispatching.
