---
name: "jack-email-beehiiv-subscriber"
description: "Adds a subscriber to Beehiiv via a webhook trigger. Useful for automating email list growth from form submissions."
version: "1.0.0"
license: "MIT"
tags: ["email marketing", "beehiiv", "automation", "webhook"]
triggers:
  - "when a form is submitted"
  - "when a new user signs up"
allowed-tools: []
compatibility: "make.com, beehiiv"
metadata:
  difficulty: "medium"
  category: "email"
  tools_required: ["make.com", "beehiiv"]
  estimated_setup_time: "30min"
---

# Email Beehiiv Subscriber

## When to Use

Use this skill when you need to:
- when a form is submitted
- when a new user signs up

## What This Does

Adds a subscriber to Beehiiv via a webhook trigger. Useful for automating email list growth from form submissions.

## Workflow

Make.com workflow to create a subscriber in Beehiiv from a webhook.  The workflow triggers on a webhook event, then creates a subscriber in Beehiiv with email and UTM source parameters.

## Configuration

**Required tools/platforms:**
- make.com
- beehiiv

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
