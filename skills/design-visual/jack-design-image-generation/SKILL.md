---
name: "image-generation"
description: "Generate images using DALL-E based on textual prompts."
version: "1.0.0"

tags: ["dall-e", "image generation", "automation"]
triggers:
  - "When you need to automatically create images from text prompts for social media or other purposes."
allowed-tools: []
compatibility: "openai, make.com"
metadata:
  difficulty: "medium"
  category: "design"
  tools_required: ["openai", "make.com"]
  estimated_setup_time: "15min"
---

# Design Image Generation

## When to Use

Use this skill when you need to:
- When you need to automatically create images from text prompts for social media or other purposes.

## What This Does

Generate images using DALL-E based on textual prompts.

## Workflow

1. Add the 'OpenAI > Generate an Image' module in Make.com.
2. Set the model to 'DALL-E 3' and configure image dimensions, style, and quality.
3. Provide instructions based on the article text or caption content.

## Configuration

**Required tools/platforms:**
- openai
- make.com

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
