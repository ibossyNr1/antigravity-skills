---
name: "jack-content-summarize-rss-email"
description: "Summarizes RSS feed articles and sends them via email using DeepSeek R1."
version: "1.0.0"
license: "MIT"
tags: ["rss", "summarization", "email", "deepseek", "make.com"]
triggers:
  - "to automatically summarize and email new articles from an RSS feed"
allowed-tools: []
compatibility: "make.com, rss, openrouter, gmail"
metadata:
  difficulty: "medium"
  category: "content"
  tools_required: ["make.com", "rss", "openrouter", "gmail"]
  estimated_setup_time: "30min"
---

# Content Summarize Rss Email

## When to Use

Use this skill when you need to:
- to automatically summarize and email new articles from an RSS feed

## What This Does

Summarizes RSS feed articles and sends them via email using DeepSeek R1.

## Workflow

This Make.com scenario fetches the latest article from an RSS feed, extracts the text, summarizes it using DeepSeek R1, and sends the summary via email.

## Configuration

**Required tools/platforms:**
- make.com
- rss
- openrouter
- gmail

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
