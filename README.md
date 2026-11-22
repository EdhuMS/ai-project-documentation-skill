# AI Project Documentation Skill

**Portable project documentation, evidence-based progress tracking, and verifiable handoffs between AI coding agents.**

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](https://github.com/EdhuMS/ai-project-documentation-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-blueviolet)](https://agentskills.io/specification)

> **Status:** initial public release. The local Python CLI and unit tests are implemented. Compatibility with every agent and cloud provider is **not** guaranteed or tested.

## Why this exists

Long-running software projects lose context when a coding agent, developer, or chat session changes. This skill establishes a vendor-neutral workflow that records **what was actually built, what was verified, why decisions were made, and what should happen next**. A new agent must verify handoff claims against code and evidence rather than trust an old summary blindly.

### Features
- **Cross-agent continuity:** structured handoffs with verified facts, unknowns, blockers, commit references, test evidence, and the precise next action.
- **Storage independence:** works with Markdown/JSON on local disk; Git, GitHub, GitLab, Drive, Notion, or other services are *optional* depending on tools and access.
- **Documentation profiles:** light, professional, critical — proportional to project risk.
- **Evidence-first governance:** clear distinction between `verified`, `reported`, `inferred`, `unknown`; and between `passed`, `failed`, `skipped`, `not_run` tests.
- **Architecture decisions and releases:** reusable ADR, state, and handoff templates.
- **Safety:** read-only by default when authorization is unclear; no unilateral publishes, merges, deletions or destructive operations.
- **Local CLI:** initialize a documentation folder and validate structured project state with Python's standard library.

## Requirements

A compatible AI assistant able to read Markdown instructions. **Python 3.9+** is optional for the local helper script. No cloud account, external API, database, or Python package installation is required.

## Install

### Option A — Agent Skills compatible clients

1. Download or clone this repository:
   ```bash
   git clone https://github.com/EdhuMS/ai-project-documentation-skill.git
   ```
2. Copy the **entire repository folder** (including `SKILL.md`, `references/`, and `templates/`) into a user or project skill directory supported by your specific agent.
3. Restart or refresh the agent's skill discovery if required. Verify that it reads `SKILL.md`. **Installation paths and activation behavior vary by host.** See [Agent Skills specification](https://agentskills.io/specification).
4. Invoke: `Use AI Project Documentation Skill in light mode. Audit my project and prepare a verified handoff. Do not modify code.`

### Option B — Manual / host without skills

Open `SKILL.md` and provide its instructions to your assistant along with the relevant `references/` files. This is a manual protocol and does not automatically provide filesystem or cloud access.

### Option C — Local-only documentation (no AI required)

From this repository directory:
```bash
python scripts/pdc.py init /path/to/my-project --project-id my-project
python scripts/pdc.py validate /path/to/my-project/docs/continuity/PROJECT-STATE.json
```
On Windows, replace `python` with `py` if needed. Initialization refuses to overwrite existing nonempty documentation directories.

## Use it

**Resume a project:**
> Use AI Project Documentation Skill. Inspect the current repository and latest handoff, verify the real branch/commit and test status, and tell me the next milestone. Read-only.

**Document a completed task:**
> Use the skill in professional mode to update requirements, architectural decisions, test evidence, project state, and a handoff. Only write to the documentation folder I've authorized.

**Prepare a handoff:**
> Prepare a verified agent handoff: completed changes, evidence, tests passed/failed/not run, blockers, permissions and the next exact action. Never invent a commit.

**Use cloud storage:**
> Use the skill with my chosen documentation destination. First verify access and permissions, identify the canonical source, and propose changes before writing.

## Documentation levels

| Profile | Intended use | Typical artifacts |
| --- | --- | --- |
| Light | Small projects, individual work | README, PROJECT-STATE.json, HANDOFF.md |
| Professional | Maintained products and teams | Light + requirements, architecture, ADRs, test evidence, changelog |
| Critical | Higher-risk / regulated contexts | Professional + risk, traceability, security and restore evidence |

Profiles are guidelines, not certifications or mandatory paperwork.

## How storage works

Each document has **one canonical location** and optionally controlled mirrors. Local files work out of the box. Git can version those files. Third-party storage requires a compatible integration already available to the executing agent and the user's authorization. This project **does not ship cloud API adapters or automatic cross-platform sync in v0.1.0**. Conflicting copies must not be silently overwritten.

## Project layout

```text
SKILL.md                         Agent instructions
references/                      Documentation, storage, handoff, security protocols
templates/                       Project state, ADR and handoff templates
examples/                        Fictional example
docs/decisions/                  Architecture decisions for this skill
scripts/pdc.py                   Optional local init / validate CLI
tests/                           Standard library unit tests
CHANGELOG.md                     Version history
```

## Test
```bash
python -m unittest discover -s tests -v
python scripts/pdc.py validate templates/PROJECT-STATE.json
```

## Releases

| Version | Highlights |
| --- | --- |
| **[v0.1.0](https://github.com/EdhuMS/ai-project-documentation-skill/releases)** | First public version: portable skill, evidence-based handoffs, three documentation profiles, local initializer/validator, templates and tests |

Release history is also maintained in [CHANGELOG.md](CHANGELOG.md). The link above opens GitHub's Releases section; a GitHub-hosted release is not implied until published there.

## Limitations

- The skill is a set of instructions and templates, **not** a permissions/security sandbox.
- Local CLI does not call providers or synchronize across services.
- Provider-specific integrations and multi-agent activation tests remain future work.
- AI-generated documentation still requires human review and verification against primary evidence.

## Contributing

Issues and pull requests are welcome. Please include reproducible examples, describe expected versus actual behavior, avoid real client or private project data, and run the tests before submitting.

## Sources and acknowledgments

Design references: [Agent Skills](https://agentskills.io/specification), [Architecture Decision Records](https://adr.github.io/madr/), [Diátaxis](https://diataxis.fr/), and [Keep a Changelog](https://keepachangelog.com/).

**License:** [MIT](LICENSE). © 2026 EdhuMS.
