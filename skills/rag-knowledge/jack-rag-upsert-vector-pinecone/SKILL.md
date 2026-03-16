---
name: "jack-rag-upsert-vector-pinecone"
description: "Upserts a vector along with metadata to Pinecone."
version: "1.0.0"
license: "MIT"
tags: ["pinecone", "vector database", "upsert", "metadata", "automation"]
triggers:
  - "When you need to store a vector embedding and associated metadata in Pinecone."
allowed-tools: []
compatibility: "make.com, pinecone"
metadata:
  difficulty: "medium"
  category: "rag"
  tools_required: ["make.com", "pinecone"]
  estimated_setup_time: "30min"
---

# Rag Upsert Vector Pinecone

## When to Use

Use this skill when you need to:
- When you need to store a vector embedding and associated metadata in Pinecone.

## What This Does

Upserts a vector along with metadata to Pinecone.

## Workflow

This Make.com module upserts a vector to Pinecone, including specifying the ID, values, and metadata (content, title, unique hash).

## Configuration

**Required tools/platforms:**
- make.com
- pinecone

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
