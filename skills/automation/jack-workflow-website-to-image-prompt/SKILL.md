---
name: "website-to-image-prompt"
description: "Downloads website content, extracts text, and generates an image prompt using Claude."
version: "1.0.0"

tags: ["automation", "make.com", "website content", "image generation"]
triggers:
  - "When you need to automatically generate an image prompt from a given website URL."
  - "When you want to create a workflow that fetches website content and leverages Claude for image prompt generation."
allowed-tools: []
compatibility: "make.com, claude"
metadata:
  difficulty: "medium"
  category: "leadgen"
  tools_required: ["make.com", "claude"]
  estimated_setup_time: "30min"
---

# Workflow Website To Image Prompt

## When to Use

Use this skill when you need to:
- When you need to automatically generate an image prompt from a given website URL.
- When you want to create a workflow that fetches website content and leverages Claude for image prompt generation.

## What This Does

Downloads website content, extracts text, and generates an image prompt using Claude.

## Workflow

This workflow downloads the content of a website, extracts the text, and then uses Claude to generate an image prompt.

Modules:
1. **Custom Webhook:** Receives a URL.
2. **HTTP: Get File:** Downloads the HTML content from the URL.
3. **Regexp: HTMLToText:** Extracts the text from the HTML content.
4. **Anthropic Claude: Create a Message:** Uses the extracted text to generate an image prompt using Claude.

## Configuration

**Required tools/platforms:**
- make.com
- claude

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
