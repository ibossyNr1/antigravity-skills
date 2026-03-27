<p align="center">
  <a href="https://agents-as-a-service.com">
    <img src="https://img.shields.io/badge/AaaS-Platform-0A0A0A?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCI+PHRleHQgeD0iNCIgeT0iMTgiIGZvbnQtc2l6ZT0iMTYiPvCfpJY8L3RleHQ+PC9zdmc+" alt="AaaS Platform">
  </a>
</p>

<h1 align="center">AaaS Vault</h1>
<h3 align="center">The Open Skill Registry for AI Agents</h3>

<p align="center">
  <strong>5,400+ production-ready skills across 52 categories for AI agents, automation, and intelligent workflows.</strong>
</p>

<p align="center">
  <a href="https://agents-as-a-service.com"><img src="https://img.shields.io/badge/Platform-agents--as--a--service.com-blue?style=flat-square" alt="Platform"></a>
  <a href="https://aaas.blog"><img src="https://img.shields.io/badge/Knowledge-aaas.blog-green?style=flat-square" alt="Blog"></a>
  <a href="https://aaas.select"><img src="https://img.shields.io/badge/Marketplace-aaas.select-orange?style=flat-square" alt="Marketplace"></a>
  <a href="https://aaas.academy"><img src="https://img.shields.io/badge/Academy-aaas.academy-purple?style=flat-square" alt="Academy"></a>
  <img src="https://img.shields.io/badge/Skills-5,400+-brightgreen?style=flat-square" alt="Skills Count">
  <img src="https://img.shields.io/badge/Categories-52-blue?style=flat-square" alt="Categories">
  <img src="https://img.shields.io/badge/Quality-Gold%20%7C%20Silver%20%7C%20Bronze-gold?style=flat-square" alt="Quality Tiers">
  <img src="https://img.shields.io/badge/License-Open-lightgrey?style=flat-square" alt="License">
</p>

---

## What is AaaS Vault?

**AaaS Vault** is the largest curated skill registry for AI agents. Each skill is a self-contained, portable capability that can be plugged into any agentic platform -- Claude Code, Agent Zero, Cursor, Windsurf, or your own custom agent framework.

Whether you are building AI automation workflows, deploying autonomous AI agents, or looking for the best AI tools and agent capabilities, this vault has what you need.

> **Part of [Agents-as-a-Service (AaaS)](https://agents-as-a-service.com)** -- the platform that makes AI agents accessible to everyone, from solo founders to enterprise teams.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Skill Categories](#skill-categories)
- [Quality Tiers](#quality-tiers)
- [Installation](#installation)
- [SKILL.md Format](#skillmd-format)
- [The AaaS Ecosystem](#the-aaas-ecosystem)
- [Who Is This For?](#who-is-this-for)
- [Contributing](#contributing)

---

## Quick Start

**Find a skill, drop it in, start building.**

```bash
# Browse the vault
ls skills/

# Pick a category
ls skills/ai-agents/

# Read any skill's documentation
cat skills/ai-agents/your-skill/SKILL.md

# Use it in your agent
cp -r skills/ai-agents/your-skill /path/to/your-agent/skills/
```

Ready to go further? **[Activate your AaaS account](https://agents-as-a-service.com)** for managed agent deployment, marketplace access, and AI automation education.

---

## Skill Categories

52 categories covering the full spectrum of AI agent capabilities:

### Core AI & Agents
| Category | Skills | What You Get |
|----------|--------|-------------|
| `ai-agents` | 56 | AI agent frameworks, orchestration, tool configs |
| `machine-learning` | 56 | ML training, deployment, model monitoring |
| `rag-knowledge` | 30 | RAG pipelines, vector search, knowledge bases |
| `research-intelligence` | 31 | Web research, competitive analysis, data gathering |

### Development & Engineering
| Category | Skills | What You Get |
|----------|--------|-------------|
| `frontend` | 26 | React, Next.js, Vue, UI frameworks |
| `backend` | 26 | Node.js, Python, Go, API services |
| `api-development` | 27 | API design, OpenAPI, SDK generation |
| `api-integration` | 25 | Third-party API connectors |
| `devops` | 50 | CI/CD, Docker, Kubernetes, IaC |
| `testing` | 51 | Test automation, TDD, E2E, coverage |
| `security` | 53 | OWASP, scanning, pentesting, hardening |

### Data & Analytics
| Category | Skills | What You Get |
|----------|--------|-------------|
| `data-engineering` | 39 | ETL, pipelines, data processing |
| `data-analytics` | 25 | BI, dashboards, statistical analysis |
| `data-scraping` | 5 | Web scraping, extraction, parsing |

### Cloud Platforms
| Category | Skills | What You Get |
|----------|--------|-------------|
| `cloud-aws` | 25 | AWS Lambda, S3, DynamoDB, CDK |
| `cloud-gcp` | 25 | Google Cloud Functions, Firestore, Vertex AI |

### Content & Marketing
| Category | Skills | What You Get |
|----------|--------|-------------|
| `content-creation` | 87 | Writing, repurposing, publishing automation |
| `email-automation` | 28 | Drip campaigns, deliverability, sequences |
| `social-media` | 11 | Posting, scheduling, analytics |
| `video-production` | 11 | Video creation, editing, distribution |
| `voice-audio` | 11 | TTS, voice cloning, audio processing |
| `visual-content` | 25 | Image generation, brand assets |
| `design-visual` | 34 | Design tools, UI/UX, brand systems |

### Business & Automation
| Category | Skills | What You Get |
|----------|--------|-------------|
| `automation` | 35 | General-purpose business automation |
| `enterprise` | 25 | Enterprise workflow, process orchestration |
| `sales-automation` | 24 | CRM, outreach, sales workflows |
| `lead-generation` | 17 | Lead discovery, qualification, nurturing |
| `no-code-tools` | 48 | Zapier, Make, Airtable, low-code platforms |

### Documentation & Knowledge
| Category | Skills | What You Get |
|----------|--------|-------------|
| `documentation` | 35 | Technical docs, knowledge management |
| `execution-scripts` | 33 | Ready-to-run automation scripts |

### Specialized
| Category | Skills | What You Get |
|----------|--------|-------------|
| `domain-specific` | 12 | Industry-specific solutions |
| `thinking-patterns` | 12 | Cognitive frameworks, mental models |
| `role-personas` | 12 | Behavioral models, agent personas |
| `problem-solving` | 12 | Methodologies, decision frameworks |
| `design-principles` | 12 | UX heuristics, design systems |
| `animation` | 12 | Motion design, animation types |
| `emotional-design` | 12 | Emotional UX, engagement patterns |
| `ui-elements` | 12 | Component patterns, design tokens |
| `industry-specific` | 12 | Vertical solutions |
| `tools-frameworks` | 12 | Tool and framework integrations |
| `time-based` | 12 | Scheduling, time-scale planning |
| `skill-levels` | 12 | Progressive learning, skill ladders |

**Plus** `protocols`, `best-practices`, `workflow-automation`, `setup-guides`, and more.

---

## Quality Tiers

Every skill is scored across 7 dimensions and assigned a quality tier:

| Tier | Score | Count | What It Means |
|------|-------|-------|---------------|
| **Gold** | 100% | 544 | Perfect -- complete SKILL.md, examples, references, deep content |
| **Silver** | >= 66.5% | 4,809 | Production-ready -- well-structured, normalized, documented |
| **Bronze** | >= 45% | 69 | Usable -- basic structure, functional |

**Scoring dimensions:** SKILL.md presence, description quality, instruction depth, usage examples, external references, content depth, copyright cleanliness.

---

## Installation

### Claude Code

```bash
git clone https://github.com/ibossyNr1/aaas-vault.git ~/.agents/skills/aaas-vault
```

### Agent Zero

```bash
git clone https://github.com/ibossyNr1/aaas-vault.git
cp -r aaas-vault/skills/* /path/to/agent-zero/work_dir/skills/
```

### Cursor / Windsurf / Other Agentic IDEs

Each skill is a self-contained directory with a `SKILL.md` file. Copy individual skill directories into your agent's skill path:

```bash
cp -r aaas-vault/skills/ai-agents/your-skill /path/to/your/skills/
```

### Cherry-Pick Individual Skills

Don't need the whole vault? Grab what you need:

```bash
# Clone just one category
git clone --depth 1 --filter=blob:none --sparse https://github.com/ibossyNr1/aaas-vault.git
cd aaas-vault
git sparse-checkout set skills/ai-agents
```

---

## SKILL.md Format

Every skill follows a standardized format with YAML frontmatter for machine-readable discovery:

```yaml
---
name: "skill-name"
description: "What this skill does and when to use it"
version: "1.0.0"
tags: ["ai-agents", "automation", "workflow"]
triggers:
  - "When you need to build an AI agent"
  - "When implementing agent orchestration"
compatibility: "agent-zero, claude-code, cursor"
---

# Skill Name

## When to Use
Describe the situations where this skill applies...

## Instructions
Step-by-step guide for the agent...

## Examples
Concrete usage examples...
```

---

## The AaaS Ecosystem

AaaS Vault is one piece of a larger ecosystem designed to make AI agents and automation accessible:

| Surface | URL | What It Does |
|---------|-----|-------------|
| **Agents-as-a-Service** | [agents-as-a-service.com](https://agents-as-a-service.com) | The main platform -- deploy, manage, and scale AI agents |
| **AI Knowledge Index** | [aaas.blog](https://aaas.blog) | 800+ entities covering AI tools, frameworks, and concepts |
| **AI Agent Marketplace** | [aaas.select](https://aaas.select) | 100+ curated AI agents ready to deploy |
| **AI Automation Academy** | [aaas.academy](https://aaas.academy) | Learn AI automation -- courses, tracks, and Action Packs |
| **Content Compiler** | [aaas.diy](https://aaas.diy) | Turn any content into structured learning materials |
| **AI Consultancy** | [aaas.boutique](https://aaas.boutique) | Custom AI solutions and agent development (EUR 3K--30K) |
| **Account Hub** | [aaas.company](https://aaas.company) | Single sign-on across all AaaS surfaces |

### Why AaaS?

- **For developers** -- Skip months of agent capability research. Use proven, scored skills.
- **For businesses** -- Find the right AI agent for your workflow at [aaas.select](https://aaas.select).
- **For learners** -- Go from zero to AI automation expert at [aaas.academy](https://aaas.academy).
- **For enterprises** -- Get custom AI agent solutions at [aaas.boutique](https://aaas.boutique).

---

## Who Is This For?

- **AI engineers** building autonomous agents and multi-agent systems
- **Developers** looking for best AI tools, frameworks, and automation patterns
- **Startup founders** who want AI agents without hiring an AI team
- **Automation specialists** connecting AI to business workflows
- **Agencies** deploying AI solutions for clients
- **Anyone searching for** the best AI agent marketplace, AI tools directory, or AI automation resources

---

## Repository Structure

```
skills/
  ai-agents/                  # 56 skills
  machine-learning/           # 56 skills
  security/                   # 53 skills
  testing/                    # 51 skills
  devops/                     # 50 skills
  no-code-tools/              # 48 skills
  content-creation/           # 87 skills
  data-engineering/           # 39 skills
  ...                         # 44 more categories
SKILLS_MANIFEST.json          # Machine-readable skill index
CATALOG.md                    # Full skill catalog with descriptions
README.md                     # This file
```

---

## Stats

| Metric | Value |
|--------|-------|
| Total Skills | 5,400+ |
| Categories | 52 |
| Gold Tier | 544 |
| Silver Tier | 4,809 |
| Compatible Platforms | Agent Zero, Claude Code, Cursor, Windsurf, custom agents |
| Last Updated | March 2026 |

---

## Contributing

Found a gap? Have a skill to share?

1. Fork this repo
2. Add your skill as a directory under the appropriate category in `skills/`
3. Include a `SKILL.md` following the [standard format](#skillmd-format)
4. Open a PR with a description of what your skill does

All contributions are reviewed for quality scoring before merge.

---

## Related Searches

This repository is useful if you are looking for:

- Best AI agent skills and capabilities
- AI tools directory and curated registry
- AI automation frameworks and patterns
- Production-ready AI agent templates
- Claude Code skills and extensions
- Agent Zero skill packs
- AI agent marketplace resources
- How to build AI agents
- AI workflow automation tools
- LLM application patterns and best practices
- RAG pipeline implementations
- AI-powered business automation

---

<p align="center">
  <strong>Built by <a href="https://agents-as-a-service.com">Agents-as-a-Service</a></strong><br>
  Making AI agents accessible to everyone.
</p>

<p align="center">
  <a href="https://agents-as-a-service.com">Platform</a> &middot;
  <a href="https://aaas.blog">Knowledge</a> &middot;
  <a href="https://aaas.select">Marketplace</a> &middot;
  <a href="https://aaas.academy">Academy</a> &middot;
  <a href="https://aaas.diy">DIY</a> &middot;
  <a href="https://aaas.boutique">Consultancy</a>
</p>
