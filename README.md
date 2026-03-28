# casestudies.dev

Programmatic access to millions of real-life company case studies.

We crawl, structure, and index case studies from hundreds of company websites so you can search them via API.

**Docs**: [docs.casestudies.dev](https://docs.casestudies.dev)

## Quick start

```bash
# 1. Get a free API key
curl -X POST https://whatsapp-backend-knd2.onrender.com/v1/keys \
  -H "Content-Type: application/json" \
  -d '{"email": "you@company.com"}'

# 2. Semantic search
curl -X POST https://whatsapp-backend-knd2.onrender.com/v1/casestudies/semantic \
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
| Starter | 200 | No | Free |
| Growth | 5,000 | Yes | $79/mo |
| Scale | 25,000 | Yes | $249/mo |
| Enterprise | Custom | Yes | Contact us |

## MCP Server — connect to Claude, ChatGPT, and AI agents

Give your AI agents direct access to case study search, company analysis, and vendor comparison. No API calls to write — just ask in natural language.

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "casestudies": {
      "command": "python",
      "args": ["/path/to/mcp-server/server.py"],
      "env": {
        "CASESTUDIES_API_KEY": "cs_live_your_key_here"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add casestudies python /path/to/mcp-server/server.py -e CASESTUDIES_API_KEY=cs_live_xxx
```

### Available tools

| Tool | Description |
|------|-------------|
| `search_case_studies` | Semantic search with natural language queries |
| `get_case_study` | Get full details of a specific case study |
| `search_companies` | Find companies by name or industry |
| `get_company_analysis` | Competitor analysis — top industries, clients, outcomes |
| `compare_vendors` | Side-by-side comparison of up to 5 companies |
| `get_company_timeline` | Chronological view for due diligence |

### Example prompts

- "Find case studies about companies that improved onboarding conversion"
- "Compare GoCardless, Checkout.com, and Paddle for ecommerce payments"
- "What industries does Stripe serve? Show me their notable clients"

[Full MCP docs →](https://docs.casestudies.dev)

## API spec

The full OpenAPI 3.1 specification is available at [`openapi.yaml`](openapi.yaml).

## Links

- [API Docs](https://docs.casestudies.dev)
- [Website](https://casestudies.dev)
- [MCP Server](mcp-server/)
