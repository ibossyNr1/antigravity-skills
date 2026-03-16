---
name: "jack-content-rag-client-intelligence"
description: "Create a client intelligence system that retrieves data from websites, emails, and meetings, vectorizing it into a RAG-powered knowledge base."
version: "1.0.0"
license: "MIT"
tags: ["rag", "client intelligence", "automation", "knowledge base"]
triggers:
  - "When a new email is received"
  - "On a schedule"
allowed-tools: []
compatibility: "n8n, airtable, pinecone, firecrawl, fireflies.ai, openai"
metadata:
  difficulty: "hard"
  category: "content"
  tools_required: ["n8n", "airtable", "pinecone", "firecrawl", "fireflies.ai", "openai"]
  estimated_setup_time: "1hr"
---

# Content Rag Client Intelligence

## When to Use

Use this skill when you need to:
- When a new email is received
- On a schedule

## What This Does

Create a client intelligence system that retrieves data from websites, emails, and meetings, vectorizing it into a RAG-powered knowledge base.

## Workflow

See source files for full workflow.

## Configuration

**Required tools/platforms:**
- n8n
- airtable
- pinecone
- firecrawl
- fireflies.ai
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
