---
name: "gemini-image-edit"
description: "Edits an image using Google Gemini's image generation capabilities via an n8n workflow.  It downloads an image, prompts Gemini to alter it, and uploads the result."
version: "1.0.0"

tags: ["gemini", "image editing", "n8n", "google drive"]
triggers:
  - "when you need to modify an image using AI"
  - "when you want to automate image editing workflows"
allowed-tools: []
compatibility: "n8n, google drive, gemini API"
metadata:
  difficulty: "hard"
  category: "content"
  tools_required: ["n8n", "google drive", "gemini API"]
  estimated_setup_time: "1hr"
---

# Content Gemini Image Edit

## When to Use

Use this skill when you need to:
- when you need to modify an image using AI
- when you want to automate image editing workflows

## What This Does

Edits an image using Google Gemini's image generation capabilities via an n8n workflow.  It downloads an image, prompts Gemini to alter it, and uploads the result.

## Workflow

N8n workflow to edit images using Gemini:
1. **Google Drive (Download):** Downloads an image from Google Drive.
2. **Extract from File:** Extracts binary data.
3. **HTTP Request:** Sends the image to Gemini with a prompt.
4. **Code:** Converts the base64 response to binary data.
5. **Google Drive (Upload):** Uploads the edited image to Google Drive.

## Configuration

**Required tools/platforms:**
- n8n
- google drive
- gemini API

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
