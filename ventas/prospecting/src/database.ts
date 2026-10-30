import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';
import fileUrl from 'url';
import { Prospect, BusinessAsset, GeneratedWebsite, OutreachEmail, ProspectInput, ProspectStatus } from './types.js';

export class RevenueEngineDatabase {
  private db: Database.Database;

  constructor(dbPath?: string) {
    let finalPath = dbPath;
    if (!finalPath) {
      finalPath = path.join(process.cwd(), 'revenue_engine.db');
    }
    
    // Ensure directory exists if path is file-based
    if (finalPath !== ':memory:') {
      const dir = path.dirname(finalPath);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
    }

    this.db = new Database(finalPath);
    this.db.pragma('journal_mode = WAL');
    this.db.pragma('foreign_keys = ON');
    this.initTables();
  }

  private initTables(): void {
    const schema = `
      CREATE TABLE IF NOT EXISTS prospects (
        id TEXT PRIMARY KEY,
        business_name TEXT NOT NULL,
        niche TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        country TEXT NOT NULL DEFAULT 'US',
        instagram_handle TEXT,
        phone TEXT,
        email TEXT,
        website_url TEXT,
        status TEXT CHECK(status IN ('DISCOVERED', 'WEBSITE_GENERATED', 'OUTREACH_READY', 'EMAIL_SENT', 'CONVERTED')) NOT NULL DEFAULT 'DISCOVERED',
        created_at TEXT NOT NULL DEFAULT (datetime('now')),
        UNIQUE(business_name, city, state)
      );

      CREATE TABLE IF NOT EXISTS business_assets (
        id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        asset_type TEXT CHECK(asset_type IN ('LOGO', 'INSTAGRAM_PHOTO', 'SERVICES_TEXT')) NOT NULL,
        asset_url TEXT NOT NULL,
        local_path TEXT,
        FOREIGN KEY (prospect_id) REFERENCES prospects(id) ON DELETE CASCADE
      );

      CREATE TABLE IF NOT EXISTS generated_websites (
        id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        template_id TEXT NOT NULL,
        preview_url TEXT,
        stripe_checkout_url TEXT,
        price_usd REAL NOT NULL DEFAULT 499.00,
        status TEXT NOT NULL DEFAULT 'DRAFT',
        created_at TEXT NOT NULL DEFAULT (datetime('now')),
        FOREIGN KEY (prospect_id) REFERENCES prospects(id) ON DELETE CASCADE
      );

      CREATE TABLE IF NOT EXISTS outreach_emails (
        id TEXT PRIMARY KEY,
        prospect_id TEXT NOT NULL,
        email_subject TEXT NOT NULL,
        email_body TEXT NOT NULL,
        preview_image_path TEXT,
        stripe_payment_link TEXT,
        status TEXT CHECK(status IN ('QUEUED', 'SENT', 'FAILED')) NOT NULL DEFAULT 'QUEUED',
        created_at TEXT NOT NULL DEFAULT (datetime('now')),
        FOREIGN KEY (prospect_id) REFERENCES prospects(id) ON DELETE CASCADE
      );
    `;

    this.db.exec(schema);
  }

  public getRawDb(): Database.Database {
    return this.db;
  }

  public saveProspectIdempotent(input: ProspectInput, prospectId: string): Prospect {
    const existing = this.db.prepare(`
      SELECT * FROM prospects WHERE business_name = ? AND city = ? AND state = ?
    `).get(input.business_name, input.city, input.state) as Prospect | undefined;

    if (existing) {
      return existing;
    }

    const createdAt = new Date().toISOString();
    const country = input.country || 'US';
    const status: ProspectStatus = input.status || 'DISCOVERED';

    const insertProspect = this.db.prepare(`
      INSERT INTO prospects (id, business_name, niche, city, state, country, instagram_handle, phone, email, website_url, status, created_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `);

    insertProspect.run(
      prospectId,
      input.business_name,
      input.niche,
      input.city,
      input.state,
      country,
      input.instagram_handle || null,
      input.phone || null,
      input.email || null,
      input.website_url || null,
      status,
      createdAt
    );

    if (input.assets && input.assets.length > 0) {
      const insertAsset = this.db.prepare(`
        INSERT INTO business_assets (id, prospect_id, asset_type, asset_url, local_path)
        VALUES (?, ?, ?, ?, ?)
      `);

      for (const asset of input.assets) {
        const assetId = `asset_${Math.random().toString(36).substring(2, 10)}`;
        insertAsset.run(
          assetId,
          prospectId,
          asset.asset_type,
          asset.asset_url,
          asset.local_path || null
        );
      }
    }

    return this.getProspectById(prospectId)!;
  }

  public getProspectById(id: string): Prospect | undefined {
    return this.db.prepare(`SELECT * FROM prospects WHERE id = ?`).get(id) as Prospect | undefined;
  }

  public getProspects(filter?: { niche?: string; city?: string; status?: ProspectStatus }): Prospect[] {
    let query = `SELECT * FROM prospects WHERE 1=1`;
    const params: any[] = [];

    if (filter?.niche) {
      query += ` AND niche = ?`;
      params.push(filter.niche);
    }
    if (filter?.city) {
      query += ` AND city = ?`;
      params.push(filter.city);
    }
    if (filter?.status) {
      query += ` AND status = ?`;
      params.push(filter.status);
    }

    query += ` ORDER BY created_at DESC`;
    return this.db.prepare(query).all(...params) as Prospect[];
  }

  public getAssetsByProspectId(prospectId: string): BusinessAsset[] {
    return this.db.prepare(`SELECT * FROM business_assets WHERE prospect_id = ?`).all(prospectId) as BusinessAsset[];
  }

  public updateProspectStatus(id: string, status: ProspectStatus): boolean {
    const result = this.db.prepare(`UPDATE prospects SET status = ? WHERE id = ?`).run(status, id);
    return result.changes > 0;
  }

  public close(): void {
    this.db.close();
  }
}
