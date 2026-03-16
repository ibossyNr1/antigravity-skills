---
name: "youtube-transcript-troubleshoot"
description: "Instructions for troubleshooting issues with 0CodeKit and YouTube transcriptions by scraping the transcript directly."
version: "1.0.0"

tags: ["youtube", "scraping", "transcript", "troubleshooting"]
triggers:
  - "when 0CodeKit fails to transcribe a YouTube video"
  - "when YouTube blocks 0CodeKit's IP addresses"
allowed-tools: []
compatibility: "make.com"
metadata:
  difficulty: "medium"
  category: "scraping"
  tools_required: ["make.com"]
  estimated_setup_time: "15min"
---

# Scraping Youtube Transcript Troubleshoot

## When to Use

Use this skill when you need to:
- when 0CodeKit fails to transcribe a YouTube video
- when YouTube blocks 0CodeKit's IP addresses

## What This Does

Instructions for troubleshooting issues with 0CodeKit and YouTube transcriptions by scraping the transcript directly.

## Workflow

1. Make an HTTP call to the YouTube URL.
2. Get the HTML page.
3. Use regex to find the transcript link: (https\:\/\/www\.youtube\.com\/api\/timedtext[\S][^"]*).
4. Make an HTTP call to get the transcript.
5. Clean up the data to get the desired output.

## Configuration

**Required tools/platforms:**
- make.com

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
