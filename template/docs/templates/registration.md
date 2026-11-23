# <Role> registrations

One registration per tool the team uses. Each holds only the name, a description, tool access and the instruction to read the brief. Keep `name` and `description` identical across tools. Never copy the brief here. The rules are under "Registrations" in `docs/reference/agent-setup.md`.

`.claude/agents/<role>.md`:

```text
---
name: <role>
description: Use when <the situations, in the words people use, that should select this role>.
tools: <by role type; see agent setup>
---

Locate the repository root using git rev-parse --show-toplevel when available, or search upward for AGENTS.md and docs/README.md. Read docs/agents/<role>.md in full and follow its required sources and the selected task workflow. Read docs/agents/common.md. A missing required file is a visible blocker; do not proceed silently. Repository-prefixed paths are root-relative; Markdown links resolve from their containing file. Confirm the role and the bounded assignment. That brief is canonical. It does not replace applicable repository instructions or grant task authorization.
```

`.codex/agents/<role>.toml`:

```text
name = "<role>"
description = "<the same description as the Claude Code registration>"
developer_instructions = """
<the same paragraph as the Claude Code registration body>
"""
```

Add a model setting only when the owner asks for one; otherwise the role uses the session's model.
