# ADR-0001: Portable documentation and explicit storage ownership

- Status: Accepted for initial design
- Date: 2026-11-21
- Owner: Project maintainer

## Context
A document protocol tied to one SaaS product cannot reliably serve local-first or other-agent workflows.

## Decision
Maintain a Markdown/JSON portable core. Local storage is the baseline; Git and cloud providers are optional. Each artifact has one canonical owner and mirrors may not silently overwrite divergent copies.

## Alternatives
Required cloud provider (vendor lock-in); Git-only (excludes non-Git users); universal synchronization (too risky to claim without tested provider adapters).

## Consequences
v0.1.0 supports local operations directly. External provider integration remains an agent-capability- and permission-dependent procedure, not a shipped synchronizer.
