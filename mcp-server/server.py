"""
casestudies.dev MCP Server

Gives Claude, ChatGPT, and other AI agents access to thousands of
structured company case studies via natural language.

Usage:
    CASESTUDIES_API_KEY=cs_live_xxx python server.py

Or add to your Claude Desktop config:
    {
      "mcpServers": {
        "casestudies": {
          "command": "python",
          "args": ["/path/to/server.py"],
          "env": {"CASESTUDIES_API_KEY": "cs_live_xxx"}
        }
      }
    }
"""

import json
import os
import sys
from typing import Any

import httpx

# MCP protocol implementation (stdio transport)
BASE_URL = "https://whatsapp-backend-knd2.onrender.com"
API_KEY = os.environ.get("CASESTUDIES_API_KEY", "")

TOOLS = [
    {
        "name": "search_case_studies",
        "description": "Search case studies using natural language. Returns the most relevant case studies based on semantic similarity. Use this when someone asks about how companies solved a problem, achieved an outcome, or implemented a solution.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural language search query, e.g. 'companies that reduced churn with better onboarding'"
                },
                "industry": {
                    "type": "string",
                    "description": "Optional industry filter, e.g. 'fintech', 'hr-tech', 'ecommerce'"
                },
                "company": {
                    "type": "string",
                    "description": "Optional company slug filter, e.g. 'stripe', 'checkout'"
                },
                "limit": {
                    "type": "integer",
                    "description": "Max results to return (default 5, max 20)",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "get_case_study",
        "description": "Get full details of a specific case study by ID. Use this after search_case_studies to get the complete text, problem, solution, and outcomes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The case study UUID"
                }
            },
            "required": ["id"]
        }
    },
    {
        "name": "search_companies",
        "description": "Search for companies indexed on casestudies.dev. Returns company name, industry, logo, and number of case studies.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search by company name"
                },
                "industry": {
                    "type": "string",
                    "description": "Filter by industry"
                }
            }
        }
    },
    {
        "name": "get_company_analysis",
        "description": "Get a rolled-up analysis of a company's case study portfolio. Shows top industries they serve, notable clients, common themes, and outcome highlights. Use this for competitor analysis or due diligence.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "slug": {
                    "type": "string",
                    "description": "Company slug, e.g. 'checkout', 'stripe'"
                }
            },
            "required": ["slug"]
        }
    },
    {
        "name": "compare_vendors",
        "description": "Compare up to 5 companies side-by-side based on their case studies. Use this for procurement decisions or vendor evaluation. Optionally filter by the evaluator's industry.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "companies": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of company slugs to compare (max 5)"
                },
                "industry": {
                    "type": "string",
                    "description": "Optional industry filter to see case studies relevant to your industry"
                },
                "limit_per_company": {
                    "type": "integer",
                    "description": "Max case studies per company (default 5)",
                    "default": 5
                }
            },
            "required": ["companies"]
        }
    },
    {
        "name": "get_company_timeline",
        "description": "Get a chronological view of a company's case studies with industry breakdown over time. Use this for tracking a company's growth trajectory during due diligence.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "slug": {
                    "type": "string",
                    "description": "Company slug"
                }
            },
            "required": ["slug"]
        }
    },
]


def _api_call(method: str, path: str, body: dict | None = None) -> dict:
    """Make an authenticated API call to casestudies.dev."""
    headers = {"X-API-Key": API_KEY, "Content-Type": "application/json"}
    if method == "GET":
        params = body or {}
        resp = httpx.get(f"{BASE_URL}{path}", headers=headers, params=params, timeout=30)
    else:
        resp = httpx.post(f"{BASE_URL}{path}", headers=headers, json=body or {}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def handle_tool_call(name: str, arguments: dict) -> str:
    """Execute a tool and return the result as a string."""
    try:
        if name == "search_case_studies":
            result = _api_call("POST", "/v1/casestudies/semantic", {
                "query": arguments["query"],
                "industry": arguments.get("industry"),
                "company": arguments.get("company"),
                "limit": min(arguments.get("limit", 5), 20),
            })
            # Format for readability
            studies = result.get("data", [])
            if not studies:
                return "No case studies found matching your query."
            lines = [f"Found {len(studies)} case studies:\n"]
            for s in studies:
                lines.append(f"**{s['title']}** (similarity: {s['similarity']:.0%})")
                lines.append(f"  Client: {s.get('featured_client', 'N/A')} | Industry: {s.get('industry', 'N/A')}")
                if s.get('summary'):
                    lines.append(f"  {s['summary']}")
                if s.get('outcomes'):
                    lines.append(f"  Outcomes: {s['outcomes']}")
                if s.get('source_url'):
                    lines.append(f"  Source: {s['source_url']}")
                lines.append(f"  ID: {s['id']}")
                lines.append("")
            return "\n".join(lines)

        elif name == "get_case_study":
            result = _api_call("GET", f"/v1/casestudies/{arguments['id']}")
            return json.dumps(result, indent=2)

        elif name == "search_companies":
            params = {}
            if arguments.get("query"):
                params["q"] = arguments["query"]
            if arguments.get("industry"):
                params["industry"] = arguments["industry"]
            result = _api_call("GET", "/v1/companies", params)
            companies = result.get("data", [])
            if not companies:
                return "No companies found."
            lines = [f"Found {len(companies)} companies:\n"]
            for c in companies:
                lines.append(f"**{c['name']}** ({c['slug']}) — {c.get('industry', 'N/A')} — {c['total_case_studies']} case studies")
            return "\n".join(lines)

        elif name == "get_company_analysis":
            result = _api_call("GET", f"/v1/companies/{arguments['slug']}/analysis")
            return json.dumps(result, indent=2)

        elif name == "compare_vendors":
            result = _api_call("POST", "/v1/compare", {
                "companies": arguments["companies"][:5],
                "industry": arguments.get("industry"),
                "limit_per_company": arguments.get("limit_per_company", 5),
            })
            return json.dumps(result, indent=2)

        elif name == "get_company_timeline":
            result = _api_call("GET", f"/v1/companies/{arguments['slug']}/timeline")
            return json.dumps(result, indent=2)

        else:
            return f"Unknown tool: {name}"

    except httpx.HTTPStatusError as e:
        return f"API error: {e.response.status_code} — {e.response.text}"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """MCP server main loop — reads JSON-RPC messages from stdin, writes to stdout."""
    if not API_KEY:
        print("Error: CASESTUDIES_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = msg.get("method", "")
        msg_id = msg.get("id")

        if method == "initialize":
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {
                        "name": "casestudies-dev",
                        "version": "1.0.0",
                    },
                },
            }
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {"tools": TOOLS},
            }
        elif method == "tools/call":
            params = msg.get("params", {})
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            result_text = handle_tool_call(tool_name, arguments)
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [{"type": "text", "text": result_text}],
                },
            }
        else:
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }

        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
