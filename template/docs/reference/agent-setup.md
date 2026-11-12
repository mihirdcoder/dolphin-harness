# Agent setup

Layer: framework core. Authority: [DEC-002](../decisions/DEC-002-canonical-roles.md). Record the tools and versions this project has actually verified in the last section.

## How the pieces load

| Piece | Canonical location | How each tool finds it |
| --- | --- | --- |
| Entry instructions | `AGENTS.md` | Codex reads it directly. `CLAUDE.md` imports it with `@AGENTS.md`. |
| Scoped entry instructions | An `AGENTS.md` inside a code root | A neighbouring `CLAUDE.md` imports it the same way. Keep these short: routing pointers, no rules. |
| Role briefs | `docs/agents/<role>.md` | `.claude/agents/<role>.md` and `.codex/agents/<role>.toml` each say "read the brief". |
| Skills | `.agents/skills/<skill>/SKILL.md` | `.claude/skills/<skill>` is a relative symlink to the canonical directory. |
| Everything else | `docs/` | Reached by links from the entry file and router. |

## Where to edit

| Change | Edit here |
| --- | --- |
| A role's responsibilities or required reading | `docs/agents/<role>.md`, the one canonical brief |
| A role's name, description or tool access | The loader for each tool. Keep names and descriptions identical across tools. Never copy the brief into a loader. |
| Behavior, standards or documentation procedure | The owning document reached from the [router](../README.md), using [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md) |
| A skill's procedure | The canonical file in `.agents/skills/`. Edit the target, never a copy. |
| Entry discovery | `AGENTS.md` and `CLAUDE.md`, kept short |

Adding or removing a role or skill follows [changing the harness](../workflows/knowledge-maintenance.md#changing-the-harness).

## Symlinks

Clones must preserve symlinks. On Windows, check Git symlink support before assuming skill discovery works. If symlinks cannot be used, say so here and document the replacement; do not maintain two copies of a skill.

## Starting a session

Open the session at the repository root or inside a code root. Either way, the entry file routes to the same canonical sources. Loaders locate the repository root before reading role briefs, so a role works from a nested directory.

Guidance routing does not isolate the filesystem and does not stop unrelated context from entering a session.

## When a role is unavailable

1. If the registered role cannot be selected in the current session, start a fresh-context general agent and instruct it to read the role's brief, the common protocol and the required sources.
2. If delegation is unavailable altogether, say so, follow the same brief in the main session, and state that independence was not achieved.
3. A required independent check that did not run independently is recorded as incomplete under the [review workflow](../workflows/review.md). Never report that a role ran when it did not.

## Verified tools

Record each tool and version in which registration, skill discovery and one nested delegation have actually been exercised, with the date and any limits. An earlier check does not certify a later version.

| Tool and version | Date | What was exercised | Result and limits |
| --- | --- | --- | --- |
