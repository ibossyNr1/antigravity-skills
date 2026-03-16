---
name: "jack-workflow-ai-personalization"
description: "Personalize emails based on multiple factors (A, B, C, D, E) extracted from a webhook using OpenAI and update a Supabase database."
version: "1.0.0"
license: "MIT"
tags: ["n8n", "openai", "supabase", "gmail", "personalization", "email"]
triggers:
  - "when you need to personalize email content based on webhook data"
  - "when you want to automate data processing and storage from webhooks"
allowed-tools: []
compatibility: "n8n, openai, supabase, gmail"
metadata:
  difficulty: "hard"
  category: "workflow"
  tools_required: ["n8n", "openai", "supabase", "gmail"]
  estimated_setup_time: "1hr"
---

# Workflow Ai Personalization

## When to Use

Use this skill when you need to:
- when you need to personalize email content based on webhook data
- when you want to automate data processing and storage from webhooks

## What This Does

Personalize emails based on multiple factors (A, B, C, D, E) extracted from a webhook using OpenAI and update a Supabase database.

## Workflow

This workflow takes data from a webhook, uses OpenAI to analyze and personalize content based on factors A-E, updates a Supabase database, and creates a personalized email draft using Gmail.

## Configuration

**Required tools/platforms:**
- n8n
- openai
- supabase
- gmail

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
