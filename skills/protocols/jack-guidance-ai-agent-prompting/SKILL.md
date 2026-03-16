---
name: "jack-guidance-ai-agent-prompting"
description: "Provides a structured template for creating effective prompts for AI agents in multi-agent systems. Improves agent performance and collaboration."
version: "1.0.0"
license: "MIT"
tags: ["AI agent", "prompt engineering", "multi-agent system", "automation"]
triggers:
  - "when designing AI agents for specific roles"
  - "when setting up multi-agent systems requiring coordinated tasks"
allowed-tools: []
compatibility: "openai, any LLM"
metadata:
  difficulty: "medium"
  category: "content"
  tools_required: ["openai", "any LLM"]
  estimated_setup_time: "15min"
---

# Guidance Ai Agent Prompting

## When to Use

Use this skill when you need to:
- when designing AI agents for specific roles
- when setting up multi-agent systems requiring coordinated tasks

## What This Does

Provides a structured template for creating effective prompts for AI agents in multi-agent systems. Improves agent performance and collaboration.

## Workflow

```
[ROLE]
- You are the [Name of Agent / Role].
- Your main responsibility is to [Primary Objective].

[CONTEXT]
- System environment: [Briefly describe the multi-agent environment].
- Known details: [Facts, references, previous conversation context].

[TASK]
- Goal: [Specific outcome you want].
- Constraints: [Time limit, length limit, etc.].
- Style: [Tone, formatting guidelines].
- Output format: [Plain text, HTML, JSON, etc.].

[COLLABORATION]
- Other agents: [Who they are, what they provide].
- Interaction: [How and when this agent should interact with them].

[EXAMPLES]
- Good response example: [...]
- Bad response example: [...]

[FINAL REQUIREMENTS]
- QA checks: [Spelling, grammar, factual accuracy].
- Ethical guidelines: [Allowed/Disallowed content].
- Error handling: [Instructions if something goes wrong].
```

## Configuration

**Required tools/platforms:**
- openai
- any LLM

## Rules & Constraints

- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
