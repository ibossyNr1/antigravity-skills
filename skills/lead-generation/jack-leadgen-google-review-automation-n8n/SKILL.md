---
name: "jack-leadgen-google-review-automation-n8n"
description: "Automates the collection of and replies to Google Reviews using n8n, increasing conversions and appointments."
version: "1.0.0"
license: "MIT"
tags: ["google reviews", "automation", "lead generation", "n8n", "customer feedback", "RAG"]
triggers:
  - "Upon receiving a new Google review."
  - "When a customer submits feedback."
allowed-tools: []
compatibility: "n8n, Google Business Profile, Pinecone, Tavily, Google Sheets, OpenAI, Anthropic"
metadata:
  difficulty: "medium"
  category: "leadgen"
  tools_required: ["n8n", "Google Business Profile", "Pinecone", "Tavily", "Google Sheets", "OpenAI", "Anthropic"]
  estimated_setup_time: "1hr"
---

# Leadgen Google Review Automation N8n

## When to Use

Use this skill when you need to:
- Upon receiving a new Google review.
- When a customer submits feedback.

## What This Does

Automates the collection of and replies to Google Reviews using n8n, increasing conversions and appointments.

## Workflow

See the provided n8n workflow file for the full automation logic.

## Configuration

**Required tools/platforms:**
- n8n
- Google Business Profile
- Pinecone
- Tavily
- Google Sheets
- OpenAI
- Anthropic

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
