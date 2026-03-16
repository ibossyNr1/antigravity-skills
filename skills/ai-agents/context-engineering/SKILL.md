---
name: context-engineering
description: System for managing agentic memory and context using Airtable and Notion. Syncs project logs and research summaries to a structured database for long-term project intelligence. Uses Notion for higher-level project reporting.
version: 1.1.0
dependencies: ["pyairtable", "notion-client", "python-dotenv"]
inputs:
  - name: operation
    description: Sync, list, or query operation
  - name: data
    description: Data to sync or query parameters
outputs:
  - type: stdout
    description: Confirmation of sync or retrieved context
---

# Context Engineering Skill

## 🎯 Triggers

- Use this skill to preserve project state, logs, or research in Airtable.
- Triggered when architectural decisions are made or research rounds completed.
- Use for "agentic memory" to ensure different sessions/agents share the same high-level context.

## ⚡ Quick Start

1. Ensure `AIRTABLE_API_KEY` and `AIRTABLE_BASE_ID` are in `.env`.
2. Run `python scripts/run.py airtable_manager.py sync-logs` to sync recent activity.
3. Use `python scripts/run.py notion_reporter.py` to create project reports in Notion.

## 📋 Workflow

1. **Extraction**: Identify key context (logs, research, decisions).
2. **Formatting**: Convert to structured format (JSON/Dict).
3. **Sync**: Push to Airtable using `airtable_manager.py`.
4. **Retrieve**: Pull context in new sessions to "boot up" the agent's memory.

## 🛠️ Script Reference

- `scripts/airtable_manager.py`: Core logic for Airtable interaction.
- `scripts/notion_reporter.py`: Logic for Notion contextual reporting.
- `scripts/run.py`: Standard environment-managed wrapper.

## 🔐 Security

- API keys are stored in `.env` and never committed.
- Table IDs and Base IDs are managed via environment variables.
