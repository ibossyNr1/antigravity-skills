---
name: "business-data-qa"
description: "Creates an AI chatbot that provides data-driven insights based on business data, including sales, churn, and subscriber information."
version: "1.0.0"

tags: ["chatbot", "data analysis", "business intelligence"]
triggers:
  - "when a client needs help understanding their business data"
  - "when a user interacts with a web app connected to business data"
allowed-tools: []
compatibility: "openai"
metadata:
  difficulty: "medium"
  category: "rag"
  tools_required: ["openai"]
  estimated_setup_time: "15min"
---

# Rag Business Data Qa

## When to Use

Use this skill when you need to:
- when a client needs help understanding their business data
- when a user interacts with a web app connected to business data

## What This Does

Creates an AI chatbot that provides data-driven insights based on business data, including sales, churn, and subscriber information.

## Workflow

You are a highly knowledgeable and friendly chatbot named "DataExpert," designed to help clients understand their business data and make better decisions. Provide insights and support based on client data and inquiries.

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
