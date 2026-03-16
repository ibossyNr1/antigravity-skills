---
name: "onboarding-form-to-pinecone"
description: "Automates onboarding by capturing data from Paperform, generating embeddings, and storing it in Pinecone."
version: "1.0.0"

tags: ["paperform", "onboarding", "openai", "pinecone", "automation"]
triggers:
  - "When a new client submits the onboarding form in Paperform."
allowed-tools: []
compatibility: "make.com, paperform, openai, pinecone"
metadata:
  difficulty: "hard"
  category: "leadgen"
  tools_required: ["make.com", "paperform", "openai", "pinecone"]
  estimated_setup_time: "1hr"
---

# Leadgen Onboarding Form To Pinecone

## When to Use

Use this skill when you need to:
- When a new client submits the onboarding form in Paperform.

## What This Does

Automates onboarding by capturing data from Paperform, generating embeddings, and storing it in Pinecone.

## Workflow

This Make.com scenario captures client data from Paperform submissions, transforms it to JSON, creates embeddings using OpenAI, and upserts the data into Pinecone.

## Configuration

**Required tools/platforms:**
- make.com
- paperform
- openai
- pinecone

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
