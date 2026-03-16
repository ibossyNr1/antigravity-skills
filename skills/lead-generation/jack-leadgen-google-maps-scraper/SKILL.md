---
name: "google-maps-scraper"
description: "Scrapes business data from Google Maps based on search terms and locations."
version: "1.0.0"

tags: ["lead generation", "google maps", "scraping", "n8n"]
triggers:
  - "When needing to extract business contact information (name, address, phone, website) from Google Maps listings"
  - "To automate local business data collection"
allowed-tools: []
compatibility: "n8n, apify"
metadata:
  difficulty: "medium"
  category: "leadgen"
  tools_required: ["n8n", "apify"]
  estimated_setup_time: "30min"
---

# Leadgen Google Maps Scraper

## When to Use

Use this skill when you need to:
- When needing to extract business contact information (name, address, phone, website) from Google Maps listings
- To automate local business data collection

## What This Does

Scrapes business data from Google Maps based on search terms and locations.

## Workflow

Refer to 'Scraper_ Google Maps (1).json' for the n8n workflow.

## Configuration

**Required tools/platforms:**
- n8n
- apify

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
