---
name: "jack-rag-airtable-chat"
description: "Orchestrates a Make.com scenario to fetch data from Airtable, aggregate it, and use OpenAI to generate a response based on user input."
version: "1.0.0"
license: "MIT"
tags: ["make.com", "airtable", "openai", "rag", "chatbot"]
triggers:
  - "to create a chatbot powered by airtable and openai"
allowed-tools: []
compatibility: "make.com, airtable, openai"
metadata:
  difficulty: "hard"
  category: "rag"
  tools_required: ["make.com", "airtable", "openai"]
  estimated_setup_time: "1hr"
---

# Rag Airtable Chat

## When to Use

Use this skill when you need to:
- to create a chatbot powered by airtable and openai

## What This Does

Orchestrates a Make.com scenario to fetch data from Airtable, aggregate it, and use OpenAI to generate a response based on user input.

## Workflow

The Make.com scenario includes modules for a custom webhook, searching Airtable records, aggregating the results, and generating a response using OpenAI's GPT-4o.

## Configuration

**Required tools/platforms:**
- make.com
- airtable
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
