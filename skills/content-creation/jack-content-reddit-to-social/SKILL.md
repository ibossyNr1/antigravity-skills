---
name: "jack-content-reddit-to-social"
description: "Automate content repurposing from Reddit posts into social media updates (LinkedIn, Twitter, Facebook) using AI agents."
version: "1.0.0"
license: "MIT"
tags: ["content repurposing", "social media", "reddit", "gpt", "automation"]
triggers:
  - "When you want to quickly create social media content from Reddit posts."
  - "When you want to automate content distribution across multiple social platforms"
allowed-tools: []
compatibility: "make.com, perplexity.ai, openai"
metadata:
  difficulty: "hard"
  category: "content"
  tools_required: ["make.com", "perplexity.ai", "openai"]
  estimated_setup_time: "1hr"
---

# Content Reddit To Social

## When to Use

Use this skill when you need to:
- When you want to quickly create social media content from Reddit posts.
- When you want to automate content distribution across multiple social platforms

## What This Does

Automate content repurposing from Reddit posts into social media updates (LinkedIn, Twitter, Facebook) using AI agents.

## Workflow

1. Input Reddit URL to Perplexity AI for summary, perspectives, and data.
2. Route the output to three GPT specialist agents.
3. Each agent transforms the content into a tailored post for LinkedIn, Twitter, and Facebook respectively.

## Configuration

**Required tools/platforms:**
- make.com
- perplexity.ai
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
