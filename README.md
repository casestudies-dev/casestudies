# casestudies.dev

Know what tools your prospects are using.

Pass a domain to our API and get back every case study that company appears in — what vendors they use, what problems they solved, what outcomes they got. One call.

**Docs**: [docs.casestudies.dev](https://docs.casestudies.dev)

## Quick start

```bash
# 1. Get a free API key
curl -X POST https://api.casestudies.dev/v1/keys \
  -H "Content-Type: application/json" \
  -d '{"email": "you@company.com"}'

# 2. Enrich a lead
curl https://api.casestudies.dev/v1/enrich/bamboohr.com \
  -H "X-API-Key: YOUR_KEY"
```

Returns:

```json
{
  "domain": "bamboohr.com",
  "found": true,
  "featured_in": {
    "total": 2,
    "vendors": [
      {
        "vendor": { "name": "Remote.com", "domain": "remote.com" },
        "case_studies": [{
          "title": "BambooHR global hiring integration",
          "problem": "Needed to hire in 90+ countries",
          "outcomes": "90+ countries, full compliance"
        }]
      },
      {
        "vendor": { "name": "Brex", "domain": "brex.com" },
        "case_studies": [{
          "title": "BambooHR curbs unmanaged spend",
          "outcomes": "50% cost reduction"
        }]
      }
    ]
  }
}
```

## Enrich response fields

| Field | What it contains |
|-------|-----------------|
| `company.name` | Company name |
| `company.industry` | Their industry |
| `company.logo_url` | Logo URL |
| `featured_in.total` | Number of vendor mentions |
| `featured_in.vendors[].vendor.name` | Vendor they use |
| `featured_in.vendors[].vendor.domain` | Vendor's domain |
| `featured_in.vendors[].case_studies[].title` | Case study title |
| `featured_in.vendors[].case_studies[].problem` | Problem they faced |
| `featured_in.vendors[].case_studies[].solution` | How it was solved |
| `featured_in.vendors[].case_studies[].outcomes` | Results and metrics |
| `featured_in.vendors[].case_studies[].source_url` | Link to original |

## Integrations

Works with any platform that can make HTTP requests:

| Platform | How |
|----------|-----|
| **Clay** | HTTP enrichment step |
| **Zapier** | Webhooks by Zapier → Custom Request |
| **Make** | HTTP module |
| **HubSpot** | Operations Hub custom code action |
| **Salesforce** | Flow HTTP Callout or Apex trigger |
| **n8n** | HTTP Request node |
| **Claude** | MCP server |

[Setup guides →](https://docs.casestudies.dev/integrations/clay)

## All endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/enrich/{domain}` | GET | **Primary** — enrich a lead with vendor intelligence |
| `/v1/casestudies` | GET | Search with filters (company, industry, tag) |
| `/v1/casestudies/semantic` | POST | Natural language search |
| `/v1/casestudies/batch` | POST | Multiple queries in one call |
| `/v1/casestudies/{id}` | GET | Single case study detail |
| `/v1/companies` | GET | List indexed companies |
| `/v1/companies/{slug}` | GET | Company + case studies |
| `/v1/companies/{slug}/analysis` | GET | Top industries, clients, outcomes |
| `/v1/companies/{slug}/timeline` | GET | Chronological view |
| `/v1/compare` | POST | Vendor comparison |
| `/v1/stats` | GET | Platform stats (no auth) |
| `/v1/keys` | POST | Register API key (no auth) |

## MCP Server

Connect to Claude Desktop or Claude Code:

```bash
claude mcp add casestudies -e CASESTUDIES_API_KEY=cs_live_xxx \
  -- python /path/to/mcp-server/server.py
```

[MCP setup guide →](https://docs.casestudies.dev/guides/mcp-server)

## Pricing

| Tier | Requests/month | Price |
|------|---------------|-------|
| Starter | 200 | Free |
| Growth | 5,000 | $79/mo |
| Scale | 25,000 | $249/mo |
| Enterprise | Custom | Contact us |

## Links

- [Website](https://casestudies.dev)
- [API Docs](https://docs.casestudies.dev)
- [Integrations](https://docs.casestudies.dev/integrations/clay)
- [MCP Server](mcp-server/)
