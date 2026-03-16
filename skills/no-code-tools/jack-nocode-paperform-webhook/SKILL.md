---
name: "jack-nocode-paperform-webhook"
description: "Triggers an automation workflow from a Paperform submission, capturing form data for further processing."
version: "1.0.0"
license: "MIT"
tags: ["paperform", "webhook", "nocode automation"]
triggers:
  - "when you need to capture data from a Paperform submission in an external system"
  - "when you want to automate actions based on form data"
allowed-tools: []
compatibility: "paperform, automation platform (make.com, n8n)"
metadata:
  difficulty: "easy"
  category: "nocode"
  tools_required: ["paperform", "automation platform (make.com, n8n)"]
  estimated_setup_time: "15min"
---

# Nocode Paperform Webhook

## When to Use

Use this skill when you need to:
- when you need to capture data from a Paperform submission in an external system
- when you want to automate actions based on form data

## What This Does

Triggers an automation workflow from a Paperform submission, capturing form data for further processing.

## Workflow

1. Configure a webhook in Paperform settings to point to your automation platform.
2. Ensure custom fields in Paperform (e.g., employees, turnover, dream outcome) are properly set up.
3. Map the Paperform webhook data to the subsequent modules in your workflow.


## Configuration

**Required tools/platforms:**
- paperform
- automation platform (make.com, n8n)

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
