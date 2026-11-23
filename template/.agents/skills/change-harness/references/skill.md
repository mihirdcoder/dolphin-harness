# Skills

Read with [SKILL.md](../SKILL.md). The [skill template](../../../../docs/templates/skill.md) is the format. [Agent setup](../../../../docs/reference/agent-setup.md#how-the-pieces-load) owns how each tool finds and calls a skill.

## Is it a skill?

A skill is a procedure with concrete steps, called from a workflow step or by name. Make one when:

- the same steps recur: earlier runs exist, or the owner says they will ([evidence](../../../../docs/workflows/knowledge-maintenance.md#changing-the-harness));
- calling it by name saves explaining it again;
- it is not a lifecycle with owners and gates (a workflow) and not a rule (a standard).

Do not make a skill that only repeats a workflow's gates, a skill that coordinates reviews, or a second skill for what an existing skill already does. Extend the existing skill instead.

## Write it

- **Folder:** `.agents/skills/<name>/SKILL.md`. Put detail that only some cases need in `references/`, and checks that have actually been repeated by hand in `scripts/`.
- **Frontmatter:** `name` equal to the folder name. `description` says what the skill does and when to use it, including the request phrase. Tools choose a skill from its description alone. Keep it under 1024 characters.
- **Body:** inputs, steps, validation, output and limits. Link the workflow and standards it serves. Keep the body short so an agent loads only what its case needs.
- **Sandbox:** a tool's sandbox may block writing under `.agents/`; see the [registration rules](../../../../docs/reference/agent-setup.md#registrations).
- **Scripts** use only what every project machine already has. In the originating project a frontmatter check failed because a YAML library was not installed.

## Discovery link

Claude Code needs a relative symlink in `.claude/skills/`. Create it in the same change, from the repository root:

```bash
ln -s ../../.agents/skills/<name> .claude/skills/<name>
```

In the originating project it was forgotten twice, for two and five days.

## Overlap

Search the descriptions of the project's skills, and of user-level and bundled skills such as a general skill creator, for the same trigger phrases. When two skills answer the same request, the wrong one can run. Narrow the project's older description in the same change, and make the new one name this repository. A legacy skill with a broad description had to be narrowed to stop it taking the new skill's requests.

## Files to change

| File | Change |
| --- | --- |
| Decision and [decision index](../../../../docs/decisions/README.md) | Why a skill, rather than a workflow section or an extension of an existing skill |
| `.agents/skills/<name>/` | The skill |
| `.claude/skills/<name>` | The relative symlink, when Claude Code is used |
| Overlapping skills | Narrowed descriptions |
| The workflow step that calls it | A link at that step |
| [Router](../../../../docs/README.md) and [session protocol](../../../../docs/workflows/session.md) | A row when the skill is the entry for a kind of request |
| `AGENTS.md` | A route line, when it is a common entry |
| [Agent setup](../../../../docs/reference/agent-setup.md) | Only when discovery rules change |

## Probe discovery

Probe in a new session of each tool with the request phrase, without naming the skill. A probe that names the skill tests the procedure, not discovery. Check the session's tool calls for the skill being loaded; its final message saying so is not evidence.
