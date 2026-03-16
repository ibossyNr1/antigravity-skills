---
name: "airtable-client-search"
description: "Searches for client information in Airtable and formats the data for a vector database search using OpenAI."
version: "1.0.0"

tags: ["airtable", "openai", "vector database", "client search", "automation"]
triggers:
  - "When client data is updated in Airtable."
allowed-tools: []
compatibility: "make.com, airtable, openai"
metadata:
  difficulty: "hard"
  category: "rag"
  tools_required: ["make.com", "airtable", "openai"]
  estimated_setup_time: "1hr"
---

# Rag Airtable Client Search

## When to Use

Use this skill when you need to:
- When client data is updated in Airtable.

## What This Does

Searches for client information in Airtable and formats the data for a vector database search using OpenAI.

## Workflow

This Make.com module watches for changes in Airtable, searches for client details, and uses OpenAI to format the info as a search term for a vector database.

## Configuration

**Required tools/platforms:**
- make.com
- airtable
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
