---
name: "apify-lead-scraper"
description: "Scrapes leads from various platforms using Apify based on provided job titles and locations."
version: "1.0.0"

tags: ["lead generation", "apify", "n8n", "scraping"]
triggers:
  - "When needing to extract lead information (name, company, contact details) based on specific criteria"
  - "To automate lead data collection from online sources"
allowed-tools: []
compatibility: "n8n, apify"
metadata:
  difficulty: "medium"
  category: "leadgen"
  tools_required: ["n8n", "apify"]
  estimated_setup_time: "30min"
---

# Leadgen Apify Lead Scraper

## When to Use

Use this skill when you need to:
- When needing to extract lead information (name, company, contact details) based on specific criteria
- To automate lead data collection from online sources

## What This Does

Scrapes leads from various platforms using Apify based on provided job titles and locations.

## Workflow

Refer to 'Scraperrrr.json' for the n8n workflow.

## Configuration

**Required tools/platforms:**
- n8n
- apify

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
