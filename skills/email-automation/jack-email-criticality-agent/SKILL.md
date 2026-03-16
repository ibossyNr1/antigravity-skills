---
name: "jack-email-criticality-agent"
description: "Determines the criticality of an email and sends a notification if it requires immediate attention."
version: "1.0.0"
license: "MIT"
tags: ["email", "priority", "notification", "ai agent"]
triggers:
  - "when an email might be urgent"
  - "to avoid missing important emails"
allowed-tools: []
compatibility: "n8n, openai"
metadata:
  difficulty: "medium"
  category: "email"
  tools_required: ["n8n", "openai"]
  estimated_setup_time: "30min"
---

# Email Criticality Agent

## When to Use

Use this skill when you need to:
- when an email might be urgent
- to avoid missing important emails

## What This Does

Determines the criticality of an email and sends a notification if it requires immediate attention.

## Workflow

You are a criticality agent. Your job is to receive information from emails and determine whether or not they are important or critical. If you think that it is, you should send a webhook request . If you think it is important, then make sure you send a text message to check it out.

## Configuration

**Required tools/platforms:**
- n8n
- openai

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
