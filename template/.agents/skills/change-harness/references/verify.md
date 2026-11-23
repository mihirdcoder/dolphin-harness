# Verify a harness change

Read with [SKILL.md](../SKILL.md). The [verification rules](../../../../docs/standards/documentation.md#verification-of-guidance-changes) apply; this is how to meet them.

## 1. Static check

From the repository root:

```bash
python3 .agents/skills/change-harness/scripts/check_harness.py
```

It reads `AGENTS.md`, `CLAUDE.md`, `docs/`, `.agents/`, `.claude/` and `.codex/`, and checks that:

- every role has a brief, a registration for each tool in use and a row in the role index;
- registration names match their files, and descriptions are identical across tools;
- every registration points to its brief and stays thin;
- every skill's frontmatter has a name equal to its folder and a description under 1024 characters, and its Claude Code symlink resolves to it;
- nothing in `.claude/skills/` exists without a canonical skill;
- every workflow is linked from the workflow index, and every workflow in the index table declares stages;
- every decision is in the decision index with a matching status and a unique number;
- relative links and anchors resolve, outside `docs/templates/`;
- no `{{NAME}}` placeholder remains. Pass `--allow-placeholders` only in the unadopted template.

Fix every failure before probing. The script cannot judge meaning: whether the router, review table and neighbouring workflows lead to the item. The file table in the kind's reference covers that. It does not check reference-style links or setext headings.

## 2. Probe each tool

For each tool the team uses, start a new session at the repository root, as the [registration rules](../../../../docs/reference/agent-setup.md#registrations) describe.

- Prompt with the request phrase, as the owner would ask. Do not name the new item.
- The probe passes when the session selects the item: reads the workflow, invokes the role or loads the skill. Judge from the tool calls in the session's transcript or log, not from its final message.
- For a role, also check that it read its brief and the common protocol.

Example for a workflow captured as "price-change": prompt "Prices change next quarter; let's do the price update." Not "Use the price-change workflow."

Record for each probe the tool and version, the date, the prompt, what was selected, where the evidence is and the outcome. A probe that failed, timed out or could not run is a recorded limit, never a pass. An earlier probe does not certify a later tool version or a later change.

## 3. Independent review

A reviewer who did not write the change checks it under the [review workflow](../../../../docs/workflows/review.md#proportional-executions-and-independence): the decision's evidence and approval, every file in the kind's file table, gate ordering, rules copied where they should be linked, and the probe evidence. In the starter roster this is the [Documentation Reviewer](../../../../docs/agents/documentation-reviewer.md).

## 4. Record

Put the check result, the probes and the review in the change's record or its `evidence.md`. Logs in temporary directories do not last; quote the relevant lines instead.
