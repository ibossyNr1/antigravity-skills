---
name: "jack-nocode-improve-html-code-prompt"
description: "Prompts to refine HTML code to fix display issues, adding timer and animations while removing whitespace."
version: "1.0.0"
license: "MIT"
tags: ["HTML", "animations", "timer"]
triggers:
  - "debugging HTML code with display issues"
  - "Adding visual enhancements to an existing web page"
allowed-tools: []
compatibility: "OpenAI, Claude"
metadata:
  difficulty: "medium"
  category: "nocode"
  tools_required: ["OpenAI", "Claude"]
  estimated_setup_time: "30min"
---

# Nocode Improve Html Code Prompt

## When to Use

Use this skill when you need to:
- debugging HTML code with display issues
- Adding visual enhancements to an existing web page

## What This Does

Prompts to refine HTML code to fix display issues, adding timer and animations while removing whitespace.

## Workflow

The make automation worked well, however, the messages did not appear in the website. please re-write the entire html code to ensure that it both sends and recieves the data.
please also:
* add in a 30 second timer that stops once the data appears
* add the confetti animation on submission back in
* remove all of the dead whitespace underneath the submission bar

## Configuration

**Required tools/platforms:**
- OpenAI
- Claude

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
