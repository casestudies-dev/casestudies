# casestudies.dev

Instant tech stack detection for any domain.

Pass a domain to our API and get back every tool a company uses — detected from public records in seconds. One call.

**Website**: [casestudies.dev](https://casestudies.dev)  
**Docs**: [docs.casestudies.dev](https://docs.casestudies.dev)

## Quick start

```bash
# 1. Get a free API key at casestudies.dev/signup

# 2. Scan a domain
curl https://api.casestudies.dev/v1/enrich/bestseller.com \
  -H "X-API-Key: YOUR_KEY"
```

Returns:

```json
{
  "domain": "bestseller.com",
  "tools_detected": 16,
  "by_category": {
    "CRM": ["Salesforce", "Microsoft Dynamics 365"],
    "Identity": ["Okta", "Duo Security"],
    "Cloud": ["AWS", "Azure"],
    "Collaboration": ["Microsoft 365", "Atlassian"],
    "Monitoring": ["Datadog", "Grafana Cloud"]
  }
}
```

## How it works

Every SaaS tool that requires domain verification leaves a permanent fingerprint in public records. We scan multiple sources in parallel:

- **MX records** — email provider (Google Workspace, Microsoft 365, etc.)
- **TXT records** — domain verification tokens for 100+ tools
- **SPF includes** — email senders (Mailchimp, SendGrid, HubSpot, etc.)
- **NS records** — DNS provider (AWS Route 53, Cloudflare, etc.)
- **Certificate Transparency logs** — internal subdomains revealing backend tooling
- **HTTP headers** — CDN, WAF, hosting provider

No scraping. No guessing. Only signals verified against the actual domain.

## Streaming

For real-time progressive results:

```bash
curl https://api.casestudies.dev/v1/enrich-stream/revolut.com \
  -H "X-API-Key: YOUR_KEY" \
  -H "Accept: text/event-stream"
```

Results stream in phase by phase as they are detected.

## Use cases

- **CRM enrichment** — auto-detect tech stack when new accounts are created
- **ICP filtering** — find companies using specific tools (e.g. Salesforce + AWS)
- **Competitive intelligence** — compare stacks across target accounts
- **AI agents** — give Claude or ChatGPT access via MCP server

## Integrations

| Platform | How |
|----------|-----|
| **Clay** | HTTP enrichment step |
| **Zapier** | Custom Request action |
| **Make** | HTTP module |
| **HubSpot** | Operations Hub custom code |
| **Salesforce** | Apex trigger + callout |
| **Claude / Cursor** | MCP server |

[Setup guides →](https://docs.casestudies.dev)

## MCP Server

Connect casestudies.dev directly to Claude, Cursor, or any MCP-compatible agent.

### Claude Code

```bash
claude mcp add casestudies python /path/to/mcp-server/server.py \
  -e CASESTUDIES_API_KEY=cs_live_your_key_here
```

### Claude Desktop

Add to `claude_desktop_config.json`:

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

### Available tools

| Tool | What it does |
|------|-------------|
| `get_company_analysis` | Full tech stack for any domain |
| `search_companies` | Find companies by name or industry |
| `compare_vendors` | Side-by-side tech stack comparison |
| `search_case_studies` | Semantic search across case studies |

Once connected, just ask: *"What tools does stripe.com use?"* or *"Compare the tech stacks of revolut.com and monzo.com"*

[MCP setup guide →](https://docs.casestudies.dev)

## Links

- [Website](https://casestudies.dev)
- [API Docs](https://docs.casestudies.dev)
- [Dashboard](https://casestudies.dev/dashboard)
