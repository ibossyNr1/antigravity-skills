---
name: "jack-content-remove-special-characters"
description: "Removes special characters like newline, carriage return, tab, form feed, forward slash, backslash, and double quotes from a string."
version: "1.0.0"
license: "MIT"
tags: ["text processing", "string manipulation", "data cleaning"]
triggers:
  - "when cleaning text data for further processing"
  - "when preparing text for API requests"
allowed-tools: []
compatibility: "make.com"
metadata:
  difficulty: "medium"
  category: "content"
  tools_required: ["make.com"]
  estimated_setup_time: "15min"
---

# Content Remove Special Characters

## When to Use

Use this skill when you need to:
- when cleaning text data for further processing
- when preparing text for API requests

## What This Does

Removes special characters like newline, carriage return, tab, form feed, forward slash, backslash, and double quotes from a string.

## Workflow

{{replace(replace(replace(replace(replace(replace(replace(45.data.output[]; "/\n/g"; space); "/\r/g"; space); "/\t/g"; space); "/\f/g"; space); "/\//g"; "/"); "/\\/g"; "\\"); "/\"/g"; "\"")}}

## Configuration

**Required tools/platforms:**
- make.com

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
