---
name: "jack-workflow-airtable-email-draft"
description: "Watches Airtable for new records, filters based on status, and creates email drafts with a personalized image."
version: "1.0.0"
license: "MIT"
tags: ["automation", "make.com", "airtable", "email", "personalized emails"]
triggers:
  - "When you need to send personalized emails with images based on data stored in Airtable."
  - "When you want to automate the process of creating email drafts for leads/contacts in Airtable."
allowed-tools: []
compatibility: "make.com, airtable, gmail"
metadata:
  difficulty: "medium"
  category: "leadgen"
  tools_required: ["make.com", "airtable", "gmail"]
  estimated_setup_time: "30min"
---

# Workflow Airtable Email Draft

## When to Use

Use this skill when you need to:
- When you need to send personalized emails with images based on data stored in Airtable.
- When you want to automate the process of creating email drafts for leads/contacts in Airtable.

## What This Does

Watches Airtable for new records, filters based on status, and creates email drafts with a personalized image.

## Workflow

This workflow monitors an Airtable base for new records, filters them based on the 'Status' field, and creates drafts in Gmail with a personalized message including an image URL from Airtable.

Modules:
1. **Airtable: Watch Records:** Triggers when a record is created/updated in Airtable.
2. **Google Email: Create Draft:** Creates a draft email with a subject, HTML content (including image URL), and recipient based on Airtable data. Filter module checks status to be 'approved'.

## Configuration

**Required tools/platforms:**
- make.com
- airtable
- gmail

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
