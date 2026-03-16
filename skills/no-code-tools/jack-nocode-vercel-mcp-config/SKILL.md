---
name: "vercel-mcp-config"
description: "Add Vercel Model Context Protocol (MCP) to Antigravity config to manage Vercel deployments from within Antigravity."
version: "1.0.0"

tags: ["vercel", "mcp", "antigravity", "deployment"]
triggers:
  - "when wanting to integrate Vercel deployments with Antigravity"
  - "when setting up Model Context Protocol for Vercel"
allowed-tools: []
compatibility: "vercel, antigravity"
metadata:
  difficulty: "medium"
  category: "nocode"
  tools_required: ["vercel", "antigravity"]
  estimated_setup_time: "15min"
---

# Nocode Vercel Mcp Config

## When to Use

Use this skill when you need to:
- when wanting to integrate Vercel deployments with Antigravity
- when setting up Model Context Protocol for Vercel

## What This Does

Add Vercel Model Context Protocol (MCP) to Antigravity config to manage Vercel deployments from within Antigravity.

## Workflow

```json
"vercel": {
  "command": "npx",
  "args": [
    "-y",
    "@robinson_ai_systems/vercel-mcp"
  ],
  "env": {
    "VERCEL_TOKEN": "INSERT_VERCEL_API_KEY"
  }
}
```
Replace INSERT_VERCEL_API_KEY with your Vercel token.

## Configuration

**Required tools/platforms:**
- vercel
- antigravity

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
