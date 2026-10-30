export type ProspectStatus = 
  | 'DISCOVERED' 
  | 'WEBSITE_GENERATED' 
  | 'OUTREACH_READY' 
  | 'EMAIL_SENT' 
  | 'CONVERTED';

export type AssetType = 
  | 'LOGO' 
  | 'INSTAGRAM_PHOTO' 
  | 'SERVICES_TEXT';

export type OutreachStatus = 
  | 'QUEUED' 
  | 'SENT' 
  | 'FAILED';

export interface Prospect {
  id: string;
  business_name: string;
  niche: string;
  city: string;
  state: string;
  country: string;
  instagram_handle: string | null;
  phone: string | null;
  email: string | null;
  website_url: string | null;
  status: ProspectStatus;
  created_at: string;
}

export interface BusinessAsset {
  id: string;
  prospect_id: string;
  asset_type: AssetType;
  asset_url: string;
  local_path: string | null;
}

export interface GeneratedWebsite {
  id: string;
  prospect_id: string;
  template_id: string;
  preview_url: string | null;
  stripe_checkout_url: string | null;
  price_usd: number;
  status: string;
  created_at: string;
}

export interface OutreachEmail {
  id: string;
  prospect_id: string;
  email_subject: string;
  email_body: string;
  preview_image_path: string | null;
  stripe_payment_link: string | null;
  status: OutreachStatus;
  created_at: string;
}

export interface ProspectInput {
  business_name: string;
  niche: string;
  city: string;
  state: string;
  country?: string;
  instagram_handle?: string | null;
  phone?: string | null;
  email?: string | null;
  website_url?: string | null;
  status?: ProspectStatus;
  assets?: Array<{
    asset_type: AssetType;
    asset_url: string;
    local_path?: string | null;
  }>;
}
