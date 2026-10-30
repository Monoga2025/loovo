# Railway exit and local preservation
Objective: preserve Railway-hosted projects and persistent data before a possible exit. Remote access: current Railway CLI session only.
Delivery: local backups and evidence; no shutdown, deletion, migration, purchases or commits authorized. Verification: inventory, hashes, archive checks and isolated restore where feasible.

## Specs
S1. User: "Si porfavor claro es que lo ams probable es que bajemos todo y dejemos de usar railway yo no tengo plata para pagar eso". Inventory and back up projects, databases and persistent files locally; do not stop or delete Railway resources.
S2. Keep customer data outside servicios/ and landings/. Never print or write secrets; use credentials only in process environment. Stop a backup surface that cannot satisfy those constraints and report missing recovery prerequisites.
S3. Report verified versus incomplete backups. A repository copy alone is not a database or persistent-files backup. Any resource shutdown needs a separate user confirmation after backup verification.

## Tasks
T1 | S1-S2 | delegated: worker with terminal (explorer lacked terminal) | done | Verified 16 projects/environments, 25 services and 13 volumes; corrected maral-os ID against live CLI; pagination complete | commit: none (not authorized).
T2 | S1-S2 | in_progress (blocked) | Back up eligible code and persistent data without storing secrets; preserve access restrictions. Needs Docker Desktop running, protected destination and secure human-controlled encryption setup | commit: none.
T3 | S3 | pending | Verify archives, hashes and restoration feasibility; report missing assets and propose precise shutdown scope | commit: none.

## Log
L1. Original request: "Si porfavor claro es que lo ams probable es que bajemos todo y dejemos de usar railway yo no tengo plata para pagar eso".
L2. Previous read-only audit: previous period usage USD40.68, memory USD39.79; current usage USD2.06 and forecast USD19.73. No workspace limit. Invoice/payment not verified.
L3. Authorization covers local backup using current authenticated Railway CLI, not destructive changes or other remote sessions. Credentials must never appear in output or files. No runtime checks have yet verified any backup.
L4. Initial report of 28 associations superseded by independent live verification: 16 projects/environments, 25 services, 13 volumes; all pagination complete. Reported usage 3701.399552 MB, capacity 65000 MB. 22 latest deployments SUCCESS, maral-os Postgres FAILED, 2 null. Corrected maral-os ID. Evidence: odd/reports/railway-exit-inventory.md.
L5. T2 started, no backups downloaded. Native dump clients absent in PATH; docker/gpg/openssl present but functionality unverified. Credentials remain process-only, data protected outside product modules. No shutdown authorized.
