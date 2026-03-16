---
name: "competitor-intelligence-make"
description: "Automates competitor website change detection & review analysis using Make.com, Airtable, OpenAI, and HTTP requests."
version: "1.0.0"

tags: ["competitor intelligence", "automation", "make.com", "airtable", "openai", "web scraping"]
triggers:
  - "When you need to automatically monitor competitor website changes and analyze customer reviews."
  - "When you want to build a system that provides ongoing competitive intelligence."
allowed-tools: []
compatibility: "make.com, airtable, openai"
metadata:
  difficulty: "hard"
  category: "research"
  tools_required: ["make.com", "airtable", "openai"]
  estimated_setup_time: "1hr"
---

# Workflow Competitor Intelligence Make

## When to Use

Use this skill when you need to:
- When you need to automatically monitor competitor website changes and analyze customer reviews.
- When you want to build a system that provides ongoing competitive intelligence.

## What This Does

Automates competitor website change detection & review analysis using Make.com, Airtable, OpenAI, and HTTP requests.

## Workflow

This composite skill contains the Make.com scenarios for automated competitor intelligence.  It uses Airtable to store data, scrapes websites, uses OpenAI to analyze content changes and customer reviews. Requires setup of Airtable base, OpenAI API key, and Make.com connections.

## Configuration

**Required tools/platforms:**
- make.com
- airtable
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
