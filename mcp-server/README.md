# casestudies.dev MCP Server

Give your AI agents access to thousands of structured company case studies.

## Setup

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

### Requirements

- Python 3.10+
- `httpx` (`pip install httpx`)
- A casestudies.dev API key ([get one free](https://casestudies.dev))

## Tools

| Tool | Description |
|------|-------------|
| `search_case_studies` | Semantic search with natural language queries |
| `get_case_study` | Get full details of a specific case study |
| `search_companies` | Find companies by name or industry |
| `get_company_analysis` | Competitor analysis — top industries, clients, outcomes |
| `compare_vendors` | Side-by-side comparison of up to 5 companies |
| `get_company_timeline` | Chronological view for due diligence |

## Example prompts

Once connected, ask your AI agent:

- "Find case studies about companies that improved onboarding conversion"
- "What industries does Checkout.com serve? Show me their notable clients"
- "Compare GoCardless, Checkout.com, and Paddle for ecommerce payments"
- "Show me how fintech companies have reduced customer churn"
- "What's Stripe's case study portfolio look like over time?"
