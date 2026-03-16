---
name: "basic-personalized-template"
description: "A basic email template for personalized outreach including video and a call to action."
version: "1.0.0"

tags: ["email", "template", "personalized", "video"]
triggers:
  - "when sending personalized email outreach"
  - "when sharing a video with potential clients"
allowed-tools: []
metadata:
  difficulty: "easy"
  category: "email"
  estimated_setup_time: "5min"
---

# Email Basic Personalized Template

## When to Use

Use this skill when you need to:
- when sending personalized email outreach
- when sharing a video with potential clients

## What This Does

A basic email template for personalized outreach including video and a call to action.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email from Jack</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <p>Hey {{13.`Name 👋`}},</p>

    <p>I love what you're doing, and I'd like to help.</p>

    <p>Here's a quick video I recorded: <a href="{{2.data[].url}}" style="color: #0066cc; text-decoration: none;">Watch Video</a></p>

    <p>All the best,<br>
    <strong>Jack</strong></p>
</body>
</html>

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
