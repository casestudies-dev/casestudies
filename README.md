# casestudy.dev

Programmatic access to millions of real-life company case studies.

We crawl, structure, and index case studies from hundreds of company websites so you can search them via API.

**Docs**: [docs.casestudy.dev](https://docs.casestudy.dev)

## Quick start

```bash
# 1. Get a free API key
curl -X POST https://api.casestudy.dev/v1/keys \
  -H "Content-Type: application/json" \
  -d '{"email": "you@company.com"}'

# 2. Semantic search
curl -X POST https://api.casestudy.dev/v1/casestudies/semantic \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "companies that reduced churn with better onboarding", "limit": 5}'
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/casestudies` | GET | Search with filters (company, industry, tag, full-text) |
| `/v1/casestudies/semantic` | POST | Natural language search with vector similarity |
| `/v1/casestudies/batch` | POST | Multiple semantic queries in one call (max 10) |
| `/v1/casestudies/{id}` | GET | Get a single case study |
| `/v1/companies` | GET | List indexed companies |
| `/v1/companies/{slug}` | GET | Company with its case studies |
| `/v1/companies/{slug}/analysis` | GET | Top industries, notable clients, outcome highlights |
| `/v1/companies/{slug}/timeline` | GET | Chronological view with industry breakdown |
| `/v1/compare` | POST | Side-by-side vendor comparison (max 5) |
| `/v1/stats` | GET | Total case studies and companies (no auth) |
| `/v1/keys` | POST | Register for an API key (no auth) |

## What you get

Every case study includes:

- **Title** and **summary**
- **Featured client** and their industry
- **Problem** the client faced
- **Solution** that was implemented
- **Outcomes** with real metrics
- **Tags** for filtering
- **Source URL** to the original

## Use cases

- **Sales teams** — find social proof for your next pitch
- **AI agents** — RAG over real-world business outcomes
- **Competitor analysis** — see how competitors position themselves
- **Procurement** — compare vendors with real customer evidence
- **VC due diligence** — validate a company's customer claims

## Pricing

| Tier | Requests/month | Full text | Price |
|------|---------------|-----------|-------|
| Free | 100 | No | Free |
| Pro | 10,000 | Yes | $49/mo |
| Enterprise | Custom | Yes | Contact us |

## API spec

The full OpenAPI 3.1 specification is available at [`openapi.yaml`](openapi.yaml).

## Links

- [API Docs](https://docs.casestudy.dev)
- [Website](https://casestudy.dev)
