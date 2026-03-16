---
name: "caption-generation"
description: "Use an OpenAI Assistant to generate engaging social media captions."
version: "1.0.0"

tags: ["openai", "social media", "captions", "automation"]
triggers:
  - "When you need to automatically generate creative captions for social media posts."
allowed-tools: []
compatibility: "openai, make.com"
metadata:
  difficulty: "medium"
  category: "social"
  tools_required: ["openai", "make.com"]
  estimated_setup_time: "30min"
---

# Social Caption Generation

## When to Use

Use this skill when you need to:
- When you need to automatically generate creative captions for social media posts.

## What This Does

Use an OpenAI Assistant to generate engaging social media captions.

## Workflow

1. Create a new assistant on platform.openai.com with a specific agent persona and instructions.
2. Add the 'Message an Assistant' module in Make.com.
3. Connect the module to your OpenAI assistant, feeding it the desired input text.

## Configuration

**Required tools/platforms:**
- openai
- make.com

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
