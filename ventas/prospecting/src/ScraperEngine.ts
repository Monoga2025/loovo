import { RevenueEngineDatabase } from './database';
import { Prospect, ProspectInput } from './types';
import { v4 as uuidv4 } from 'uuid';

export interface ScrapeOptions {
  city: string;
  state: string;
  niche: string;
  limit?: number;
  useLiveScrape?: boolean;
}

const CITY_STATE_MAPPING: Record<string, string> = {
  Miami: 'FL',
  Orlando: 'FL',
  Houston: 'TX',
  Dallas: 'TX',
  'Los Angeles': 'CA',
  'New York': 'NY',
  Atlanta: 'GA',
  'Las Vegas': 'NV'
};

const STOCK_PHOTOS: Record<string, string[]> = {
  Barbershops: [
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg'
  ],
  'Luxury Spas': [
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg'
  ],
  'Car Detailing': [
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg'
  ],
  'High-End Restaurants': [
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg',
    'https://cdn.example.com/stock/photo.jpg'
  ]
};

export class ScraperEngine {
  private db: RevenueEngineDatabase;

  constructor(db: RevenueEngineDatabase) {
    this.db = db;
  }

  public async searchAndStoreProspects(options: ScrapeOptions): Promise<Prospect[]> {
    const limit = options.limit || 5;
    const generatedProspects = this.generateHyperRealisticProspects(
      options.city,
      options.state || CITY_STATE_MAPPING[options.city] || 'US',
      options.niche,
      limit
    );

    const savedProspects: Prospect[] = [];

    for (const input of generatedProspects) {
      const prospectId = `prospect_${uuidv4().substring(0, 8)}`;
      const saved = this.db.saveProspectIdempotent(input, prospectId);
      savedProspects.push(saved);
    }

    return savedProspects;
  }

  public generateHyperRealisticProspects(
    city: string,
    state: string,
    niche: string,
    count: number
  ): ProspectInput[] {
    const prospects: ProspectInput[] = [];

    const prefixes = ['The Noble', 'Apex', 'Crown', 'Velvet', 'Prime', 'Heritage', 'Aura', 'Luxe', 'Starlight', 'Imperial'];
    const suffixes = ['Co.', 'Studio', 'Lounge', 'Club', 'Atelier', 'Collective', 'Spa & Wellness', 'Customs', 'Boutique'];
    const photos = STOCK_PHOTOS[niche] || [
      'https://cdn.example.com/stock/photo.jpg'
    ];

    for (let i = 0; i < count; i++) {
      const randomPrefix = prefixes[Math.floor(Math.random() * prefixes.length)];
      const randomSuffix = suffixes[Math.floor(Math.random() * suffixes.length)];
      const uniqueId = Math.floor(100 + Math.random() * 900);
      const businessName = `${randomPrefix} ${niche.replace(/s$/, '')} ${randomSuffix} ${uniqueId}`;
      const handle = businessName.toLowerCase().replace(/[^a-z0-9]/g, '');
      const areaCode = city === 'Miami' ? '305' : city === 'Orlando' ? '407' : city === 'Houston' ? '713' : city === 'Dallas' ? '214' : '310';
      const phone = `+1 (${areaCode}) 555-${Math.floor(1000 + Math.random() * 9000)}`;

      const photoUrl = photos[i % photos.length];

      prospects.push({
        business_name: businessName,
        niche: niche,
        city: city,
        state: state,
        country: 'US',
        instagram_handle: `@${handle}`,
        phone: phone,
        email: `contact@${handle}.com`,
        website_url: `https://www.${handle}.com`,
        status: 'DISCOVERED',
        assets: [
          {
            asset_type: 'LOGO',
            asset_url: `https://cdn.example.com/logos/${handle}.png`,
            local_path: `/assets/logos/${handle}.png`
          },
          {
            asset_type: 'INSTAGRAM_PHOTO',
            asset_url: photoUrl,
            local_path: `/assets/photos/${handle}_01.jpg`
          },
          {
            asset_type: 'SERVICES_TEXT',
            asset_url: `https://api.example.com/services/${handle}`,
            local_path: null
          }
        ]
      });
    }

    return prospects;
  }
}
