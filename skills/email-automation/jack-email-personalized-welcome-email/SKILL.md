---
name: "jack-email-personalized-welcome-email"
description: "Generates a personalized welcome email using Anthropic Claude based on client onboarding data."
version: "1.0.0"
license: "MIT"
tags: ["email", "personalization", "anthropic claude", "welcome email", "automation"]
triggers:
  - "When a new client onboarding form is submitted and processed."
allowed-tools: []
compatibility: "make.com, anthropic claude"
metadata:
  difficulty: "medium"
  category: "email"
  tools_required: ["make.com", "anthropic claude"]
  estimated_setup_time: "30min"
---

# Email Personalized Welcome Email

## When to Use

Use this skill when you need to:
- When a new client onboarding form is submitted and processed.

## What This Does

Generates a personalized welcome email using Anthropic Claude based on client onboarding data.

## Workflow

This Make.com module creates a personalized welcome email using Anthropic Claude based on client data captured from a Paperform submission, using a template.

## Configuration

**Required tools/platforms:**
- make.com
- anthropic claude

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
