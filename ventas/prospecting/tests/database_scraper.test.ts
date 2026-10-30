import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { RevenueEngineDatabase } from '../src/database';
import { ScraperEngine } from '../src/ScraperEngine';
import fs from 'fs';
import path from 'path';

describe('Revenue Engine SQLite Database & Scraper Engine Suite', () => {
  let db: RevenueEngineDatabase;
  let scraper: ScraperEngine;
  const testDbPath = path.join(__dirname, 'test_revenue_engine.db');

  beforeEach(() => {
    if (fs.existsSync(testDbPath)) {
      fs.unlinkSync(testDbPath);
    }
    db = new RevenueEngineDatabase(testDbPath);
    scraper = new ScraperEngine(db);
  });

  afterEach(() => {
    db.close();
    if (fs.existsSync(testDbPath)) {
      fs.unlinkSync(testDbPath);
    }
  });

  it('1. Should initialize SQLite database tables correctly', () => {
    const tables = db.getRawDb()
      .prepare(`SELECT name FROM sqlite_master WHERE type='table'`)
      .all() as { name: string }[];
    
    const tableNames = tables.map(t => t.name);
    expect(tableNames).toContain('prospects');
    expect(tableNames).toContain('business_assets');
    expect(tableNames).toContain('generated_websites');
    expect(tableNames).toContain('outreach_emails');
  });

  it('2. Should insert and query prospects idempotently', () => {
    const prospectInput = {
      business_name: 'The Barber Club',
      niche: 'Barbershops',
      city: 'Miami',
      state: 'FL',
      country: 'US',
      instagram_handle: '@barberclubmiami',
      phone: '+1 (555) 555-0100',
      email: 'contact@example.com',
      website_url: 'https://barberclubmiami.com',
      status: 'DISCOVERED' as const,
      assets: [
        {
          asset_type: 'LOGO' as const,
          asset_url: 'https://cdn.example.com/logo.png',
          local_path: '/assets/logo.png'
        }
      ]
    };

    const saved1 = db.saveProspectIdempotent(prospectInput, 'prospect_001');
    expect(saved1.id).toBe('prospect_001');
    expect(saved1.business_name).toBe('The Barber Club');

    // Attempt duplicate insert
    const saved2 = db.saveProspectIdempotent(prospectInput, 'prospect_002');
    expect(saved2.id).toBe('prospect_001'); // Should return existing record

    const prospects = db.getProspects({ city: 'Miami' });
    expect(prospects.length).toBe(1);

    const assets = db.getAssetsByProspectId('prospect_001');
    expect(assets.length).toBe(1);
    expect(assets[0].asset_type).toBe('LOGO');
  });

  it('3. Should update prospect status correctly', () => {
    const prospectInput = {
      business_name: 'Luxe Spa Orlando',
      niche: 'Luxury Spas',
      city: 'Orlando',
      state: 'FL'
    };

    db.saveProspectIdempotent(prospectInput, 'prospect_spa');
    const updated = db.updateProspectStatus('prospect_spa', 'WEBSITE_GENERATED');
    expect(updated).toBe(true);

    const prospect = db.getProspectById('prospect_spa');
    expect(prospect?.status).toBe('WEBSITE_GENERATED');
  });

  it('4. Should scrape/search hyper-realistic US prospects and store them in SQLite', async () => {
    const results = await scraper.searchAndStoreProspects({
      city: 'Houston',
      state: 'TX',
      niche: 'Car Detailing',
      limit: 3
    });

    expect(results.length).toBe(3);
    expect(results[0].city).toBe('Houston');
    expect(results[0].state).toBe('TX');
    expect(results[0].niche).toBe('Car Detailing');
    expect(results[0].email).toBeDefined();

    const storedProspects = db.getProspects({ city: 'Houston', niche: 'Car Detailing' });
    expect(storedProspects.length).toBe(3);

    const assets = db.getAssetsByProspectId(results[0].id);
    expect(assets.length).toBe(3); // LOGO, INSTAGRAM_PHOTO, SERVICES_TEXT
    expect(assets.some(a => a.asset_type === 'INSTAGRAM_PHOTO')).toBe(true);
  });
});
