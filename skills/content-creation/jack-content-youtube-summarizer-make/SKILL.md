---
name: "jack-content-youtube-summarizer-make"
description: "Automates YouTube video summarization and key takeaway extraction using webhooks, ChatGPT, and Make.com."
version: "1.0.0"
license: "MIT"
tags: ["youtube", "summarization", "automation", "make.com", "chatgpt"]
triggers:
  - "When you need a summary of a YouTube video's transcript."
  - "When you want to automate the process of extracting key insights from video content."
allowed-tools: []
compatibility: "make.com, openai"
metadata:
  difficulty: "medium"
  category: "content"
  tools_required: ["make.com", "openai"]
  estimated_setup_time: "30min"
---

# Content Youtube Summarizer Make

## When to Use

Use this skill when you need to:
- When you need a summary of a YouTube video's transcript.
- When you want to automate the process of extracting key insights from video content.

## What This Does

Automates YouTube video summarization and key takeaway extraction using webhooks, ChatGPT, and Make.com.

## Workflow

This workflow listens for a webhook containing YouTube transcript data, uses ChatGPT to summarize it and extract key takeaways, then responds via webhook.

## Configuration

**Required tools/platforms:**
- make.com
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
