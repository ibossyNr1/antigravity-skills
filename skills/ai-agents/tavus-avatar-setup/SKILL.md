---
name: tavus-avatar-setup
description: This skill should be used when the user asks to "create a Tavus avatar", "set up a Tavus persona", "configure an AI avatar", "create a conversational video agent", or mentions Tavus.io, avatar setup, replica selection, or persona configuration. Creates and manages Tavus.io CVI (Conversational Video Interface) personas with persona bibles, stock replica assignments, and API deployment.
---

# Tavus Avatar Setup

Create, configure, and deploy AI avatar personas on Tavus.io using the CVI (Conversational Video Interface) platform.

## Keywords

tavus, avatar, persona, replica, CVI, conversational video, AI avatar, video agent, digital human, persona bible, stock replica, tavus api

## CRITICAL: No Automated Conversation Testing

**Creating personas and listing replicas via the API is allowed.** These are setup operations.

**NEVER create or launch Tavus conversations (POST /v2/conversations).** Every conversation costs credits and must be tested manually by the user.

What agents CAN do:
1. Create/update persona bibles with Section 8 JSON config
2. Run `setup_persona.py` to create personas (POST /v2/personas) — this is free setup
3. List existing personas (`--list`) and replicas (`--list-replicas`)
4. Prepare `.env` with the correct API key

What agents MUST NOT do:
1. Create conversations (POST /v2/conversations) — costs credits
2. Launch or test avatar video sessions — costs credits
3. Any interaction that starts a live CVI session

## Prerequisites

- **Tavus API Key**: Set `TAVUS_API_KEY` in the project `.env` file
- **Default Account**: `jorian@intrinsic.com.de` (AntiGravity master Tavus account)
- **API Base**: `https://tavusapi.com/v2`

## Quick Start

1. Create a persona bible markdown file with Section 8 (Tavus JSON config)
2. Run `setup_persona.py` to deploy to Tavus API
3. Use the returned `persona_id` + `replica_id` to launch CVI conversations

## Execution Workflow

### Step 1: Persona Bible Design

Every Tavus avatar requires a **persona bible** — a markdown document with these sections:

| Section | Purpose |
|---------|---------|
| 1. Identity | Role, experience, relationship to brand |
| 2. Visual Identity | Replica selection, attire, environment, gestures, lighting |
| 3. Personality & Values | Core traits, triggers, frustrations |
| 4. Voice & Language | Speaking style, cadence, register, key phrases |
| 5. Content Themes | Primary topics, engagement style |
| 6. Grounding Sources | Research docs, knowledge base |
| 7. Elevator Pitch | ~40s opening monologue |
| 8. Tavus Persona Configuration | API JSON payload (see template below) |

### Step 2: Replica Selection

Browse stock replicas or use a custom replica. Common stock replicas:

| Replica ID | Name | Style |
|------------|------|-------|
| `r92debe21318` | James | Male, professional, authoritative |
| `r9fa0878977a` | Olivia - Office | Female, professional, authoritative |
| `r044d76f4490` | Diego - Office V2 | Male, energetic, modern |
| `r6c7a6cb6d9b` | Rose - Business | Female, approachable, professional |
| `r62baeccd777` | Danny | Male, casual, energetic |

To discover more replicas, run:
```bash
python3 setup_persona.py --list-replicas
```

### Step 3: Section 8 JSON Template

The persona bible must contain a Section 8 with this structure.

**CRITICAL — Minimal Layer Pattern:** Only include layers/fields you are actively overriding with real values. Tavus treats empty strings (`""`) and empty objects (`{}`, `[]`) as intentional overrides, NOT as "use defaults." Omitting a layer entirely lets Tavus use its own defaults, which is almost always correct.

- Do NOT include the `llm` layer (Tavus uses its default LLM — adding empty `base_url`/`api_key`/`tools` breaks the pipeline)
- Do NOT set `tts_engine` explicitly (let Tavus route to its default engine)
- Do NOT include the `perception` layer (Tavus enables perception by default)
- Do NOT set `greeting` unless you specifically need a TTS-only opening line before the LLM responds. The system prompt's opening behavior handles greetings via LLM.

```markdown
## 8. TAVUS PERSONA CONFIGURATION

### API Payload Template

\```json
{
  "persona_name": "Name Role",
  "pipeline_mode": "full",
  "system_prompt": "Full system prompt here including opening/greeting behavior...",
  "default_replica_id": "rXXXXXXXXXXXX",
  "layers": {
    "stt": {
      "stt_engine": "tavus-advanced",
      "hotwords": "comma, separated, domain, terms"
    },
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "medium",
      "replica_interruptibility": "medium"
    },
    "tts": {
      "tts_emotion_control": true,
      "tts_model_name": "sonic-3"
    }
  }
}
\```
```

### Step 4: Deploy

```bash
# From the project directory containing the persona bible:
python3 /Users/user/.agents/skills/shared/tavus-avatar-setup/setup_persona.py \
  --persona-file docs/personas/my-persona.md

# Or deploy all personas in a directory:
python3 /Users/user/.agents/skills/shared/tavus-avatar-setup/setup_persona.py \
  --persona-dir docs/personas/

# List existing personas in account:
python3 /Users/user/.agents/skills/shared/tavus-avatar-setup/setup_persona.py --list

# List available stock replicas:
python3 /Users/user/.agents/skills/shared/tavus-avatar-setup/setup_persona.py --list-replicas

# Dry run (show payloads without creating):
python3 /Users/user/.agents/skills/shared/tavus-avatar-setup/setup_persona.py \
  --persona-file docs/personas/my-persona.md --dry-run
```

### Step 5: Launch a Conversation

After deployment, use the persona_id to create a conversation:

```json
// POST https://tavusapi.com/v2/conversations
{
  "persona_id": "pXXXXXXXXXXXX",
  "replica_id": "rXXXXXXXXXXXX",
  "conversational_context": "Additional context for this specific call",
  "callback_url": "https://your-app.com/tavus-webhook",
  "properties": {
    "language": "english",
    "max_call_duration": 1800,
    "participant_left_timeout": 120,
    "participant_absent_timeout": 300
  }
}
```

The response contains a `conversation_url` — embed this in an iframe or redirect the user.

## CRITICAL: Avatar Sits Silently / Looks Unresponsive

If the avatar joins but doesn't speak, check:

1. **System prompt has opening behavior** — Include greeting/opening instructions in the `system_prompt` so the LLM generates the first message. This is more reliable than the `greeting` field.
2. **Do NOT rely on the `greeting` field** — While `greeting` fires a TTS-only line before LLM processing, it can conflict with the LLM's first response and in practice, personas without `greeting` (relying on system prompt opening behavior) have been more reliable.
3. **Do NOT over-specify layers** — Explicitly setting `llm`, `tts_engine`, or `perception` layers with empty/default values can break the pipeline (see Minimal Layer Pattern above).

## Common "Avatar Can't Hear You" Fixes

### 1. Language Property (Most Common)

The `language` property is set at **conversation creation** time, NOT at persona creation. If omitted, Tavus defaults to `"english"` STT. If your avatar speaks another language (e.g., German), the STT literally cannot parse the user's speech.

Supported values: full language names (`"german"`, `"spanish"`, `"french"`, etc.) or `"multilingual"` for auto-detection.

For multilingual avatars, always use `"multilingual"`:
```json
"properties": { "language": "multilingual" }
```

### 2. Iframe Microphone Permissions

When embedding the conversation URL in an iframe, the `allow` attribute MUST include microphone:

```html
<iframe
  src="CONVERSATION_URL"
  allow="camera; microphone; fullscreen; display-capture"
  style="width: 100%; height: 500px; border: none;">
</iframe>
```

Missing `microphone` in the `allow` attribute silently blocks audio input.

### 3. Testing Directly on Tavus Dashboard

When testing from the Tavus dashboard, ensure:
- Browser has granted microphone permission to tavus.io
- No other tab/app is using the microphone
- You're using Chrome/Edge (best WebRTC support)

## Configuration Reference

### Layer Options

Only include layers you need to override. Omitted layers use Tavus defaults (recommended).

| Layer | Key Fields | Notes |
|-------|-----------|-------|
| `stt` | `stt_engine`: `tavus-advanced` | Best transcription engine. Include `hotwords` for domain terms. |
| `conversational_flow` | `turn_taking_patience`: low/medium/high | How quickly avatar responds |
| | `replica_interruptibility`: low/medium/high | Whether user can interrupt |
| `tts` | `tts_emotion_control`: true/false | Emotional expression in voice |
| | `tts_model_name`: `sonic-3` | TTS model. Do NOT set `tts_engine` — let Tavus route. |

**Layers to AVOID setting explicitly:**
| Layer | Why |
|-------|-----|
| `llm` | Empty `base_url`/`api_key`/`tools` breaks the pipeline. Tavus defaults work. |
| `perception` | Tavus enables this by default. Only set if you need to disable it. |
| `tts.tts_engine` | Let Tavus pick the engine. Only set `tts_model_name`. |
| `tts.voice_settings` | Avoid unless you need a specific speed override. |

### System Prompt Best Practices

1. **Opening behavior**: Define the elevator pitch the avatar delivers when a conversation starts
2. **Core identity**: Who is this persona? What do they care about?
3. **Conversation guidelines**: Guardrails, tone, escalation rules
4. **Goal**: What action should the avatar drive toward?
5. **Hard rules**: Things the avatar must NEVER say (critical for legal/compliance)
