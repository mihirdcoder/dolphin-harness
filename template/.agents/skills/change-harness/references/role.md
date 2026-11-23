# Roles (agents)

Read with [SKILL.md](../SKILL.md). The [role template](../../../../docs/templates/agent.md) and the [registration template](../../../../docs/templates/registration.md) are the formats. [DEC-002](../../../../docs/decisions/DEC-002-canonical-roles.md) owns the one-brief rule. [Agent setup](../../../../docs/reference/agent-setup.md) owns how each tool loads a role.

## New, extend, split or none

- **Extend** when the same expertise is needed at a new point. In the originating project the architect took on contract review; no contract-reviewer role was created.
- **New role** when a responsibility recurs and owns something no existing role owns: files, contracts, an external provider or a kind of check. Back it with the standard or workflow that holds its rules. A provider specialist got a role because the provider's configuration and code needed one owner, and giving it to either of two existing roles would have merged their boundaries.
- **Split** when two parts have separate owners and separate standards. Database and backend work were split because the owner wanted them kept apart and each had its own standard.
- **No role** when the need is a sequence (a workflow), a procedure (a skill), a perspective inside an existing review (a section in that role's brief), or one feature. A role per component was rejected in the originating project, and several older reviewer perspectives became sections of one reviewer brief.

A role is not an execution. On a small change one qualified reviewer may cover several rows of the review table.

## Write the brief

First make sure the rules the role follows exist in a standard or workflow. The brief routes to them; it does not hold them.

Fill the role template:

- **Purpose** in one or two sentences.
- **Boundaries:** what neighbouring roles own that this one does not, and who.
- **When selected:** the workflow step or review-table row that names this role.
- **Required context**, chosen by actual impact. Name the documents that own the rules, not a list of decision numbers that will keep changing.
- **Owned responsibilities and limits**, including whether it is read-only.
- **Project tools** it depends on, by name.
- **Checks and handoff:** what it returns, in what form.
- **Unavailable capability:** what it reports when a tool, connector or delegation is missing. It never substitutes self-review.

Keep out product facts, one feature's assignment text, copies of [common protocol](../../../../docs/agents/common.md) rules and roster counts. In the originating project one brief had accumulated an old assignment and shrank to about a third once that was removed.

## Write the registrations

Write one registration per tool the team uses, from the [registration template](../../../../docs/templates/registration.md) and under the [registration rules](../../../../docs/reference/agent-setup.md#registrations). Write the description from the request phrase; the tool chooses the role from it. A registration only points to the brief. In the originating project the first roles lived entirely inside one tool's registration files, and the other tool had no roles until the bodies were moved into canonical briefs.

## Files to change

| File | Change |
| --- | --- |
| Decision and [decision index](../../../../docs/decisions/README.md) | Evidence, boundaries with neighbouring roles, and what creating the role does not do: run it, implement anything or give it memory |
| The owning standard or workflow | The rules the role follows, if they are not yet written |
| `docs/agents/<role>.md` | The brief |
| `.claude/agents/<role>.md`, `.codex/agents/<role>.toml` | One registration per tool in use |
| [Role index](../../../../docs/agents/README.md) | One row. Write the "Use for" text; do not paste the registration description |
| Workflows and [review selection](../../../../docs/workflows/review.md#trigger-and-selection) | The step or row that selects the role |
| [Router](../../../../docs/README.md) | The owner column, when the role owns a domain |
| [Capability index](../../../../docs/capabilities/README.md) and capability READMEs | The default owners and owning roles, when the role owns a capability |
| [Agent setup](../../../../docs/reference/agent-setup.md) | Only when registration rules change, or to record a verified tool version. Do not keep roster counts there |
| Skills the role needs | Their discovery links, per [skill](skill.md) |

## Change, rename or retire a role

Edit a brief when its responsibility or required reading changes, not for every feature decision. Renaming or retiring follows [retire](retire.md): put a remaining role or "main session" in every owner slot it held, delete its registration in every tool, and leave no old name discoverable.
