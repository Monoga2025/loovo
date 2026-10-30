# ventas/evolution-railway

Operations script for the hosted CRM. `purgar_no_clinicas.ps1` (PowerShell) deletes from the hosted database every contact whose number is not in the allow-list of clinics in the environment variable `EVOLUTION_ALLOWED_NUMBERS`.

## What it does

1. Makes a backup of the database on the hosting volume before deleting anything.
2. Runs a small Node script with `node:sqlite` against the hosted database.
3. Keeps only the allow-listed numbers and reports how many contacts were removed.

## Before you run it

- It is destructive. Read the script first and confirm the allow-list.
- It needs hosting access and credentials from your own environment. Nothing in this repository provides them, and no value is stored here.
- Connections: it targets the CRM in `../../servicios/omni-sales-crm/` and relies on the clinic list in `../state.json`.
