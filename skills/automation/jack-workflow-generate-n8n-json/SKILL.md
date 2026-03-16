---
name: "jack-workflow-generate-n8n-json"
description: "Generates n8n workflow JSON from text, screenshots, or transcripts using a Chrome extension and Gemini."
version: "1.0.0"
license: "MIT"
tags: ["n8n", "automation", "chrome extension", "ai"]
triggers:
  - "when you want to generate n8n workflows from a description instead of building manually"
allowed-tools: []
compatibility: "chrome, gemini, n8n"
metadata:
  difficulty: "medium"
  category: "nocode"
  tools_required: ["chrome", "gemini", "n8n"]
  estimated_setup_time: "15min"
---

# Workflow Generate N8n Json

## When to Use

Use this skill when you need to:
- when you want to generate n8n workflows from a description instead of building manually

## What This Does

Generates n8n workflow JSON from text, screenshots, or transcripts using a Chrome extension and Gemini.

## Workflow

1. Install the Chrome extension.
2. Provide text, screenshots, or transcripts describing the desired n8n workflow to the extension.
3. The extension uses Gemini to generate the n8n JSON.
4. Copy and paste the generated JSON into n8n.

## Configuration

**Required tools/platforms:**
- chrome
- gemini
- n8n

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
