---
name: change-harness
description: Add, change, split, rename or retire a workflow, role (agent), gate or skill in this repository's harness, including turning work that was just finished into a reusable, named workflow, role or skill. Use when someone says "make this a workflow", "turn this into an agent" or "a role", "we'll do this again", "make this reusable", "add a check or gate to <workflow>", "add a skill to this repository's harness", "split or retire a role", or when a review traces a missed failure to a gap in the process. Not for product requirements, technical standards or delivery records; use maintain-knowledge for those.
---

# Change the harness

Layer: framework core. Authority: [DEC-006](../../../docs/decisions/DEC-006-change-harness-skill.md). [Changing the harness](../../../docs/workflows/knowledge-maintenance.md#changing-the-harness) owns the six steps, their order, what counts as evidence and when approval is needed. This skill is how to carry them out for workflows, roles, gates and skills. Each section below names the step it serves. Requirements, standards, references and delivery records go through [maintain-knowledge](../maintain-knowledge/SKILL.md).

A role is also called an agent; see the [glossary](../../../docs/glossary.md).

## Inputs

When the skill is called with arguments and the first word is a kind (`workflow`, `role`, `agent`, `gate`, `skill` or `retire`), the rest is the name. Otherwise take the kind and the name from the request. Keep the owner's name. The kind is your classification below and may differ from what was asked; say so when it does.

A harness change is itself a delivery. Before writing, open its record at `docs/work/changes/<change>/record.md` from the [compact template](../../../docs/templates/compact-change.md), or a plan and build plan when the change is large. Link it from the [work index](../../../docs/work/README.md) and use the stage names of [knowledge maintenance](../../../docs/workflows/knowledge-maintenance.md).

## Evidence (step 1)

**Capture: the owner just did the work and wants it reusable.** Reconstruct the run from the conversation, `git log` and `git diff`, and the owning change record. Note what started it, what was read, the steps in order and who did each. Note the checks that ran, what went wrong and how it was fixed, and what waited for the owner's go-ahead. Then separate the run's one-off facts (this run's values, dates, files and names) from its repeatable shape. One-off facts stay in that run's record. Only the shape goes into the harness. A mistake corrected during the run is a candidate gate or check.

**Design: no finished run.** A review found a failure the process missed, the owner describes a new kind of work, or a step no longer earns its cost. For a missed failure, trace each finding to the step that introduced it and to the earliest stage at which its evidence existed.

In both cases, search for earlier runs of the same work: `git log --grep`, change records, the work index and capability history files. Report how many you found and whether the owner said the work will recur. Step 1 of changing the harness says when that is enough.

## The owner's answers (step 1)

Ask one at a time, in plain words, and record the answers in the owner's words:

1. How will you ask for this next time? The answer is the **request phrase**. It becomes the trigger in the index or the description, and the prompt for the probe.
2. What must be true before it counts as done?
3. What must never happen without your go-ahead?

Decide everything else yourself (stage names, file names, owning role, reviewer, wording) and show it as a default the owner can strike. Do not ask about details the repository can settle.

## Classify (step 2, check for extension)

Take the first row that fits, and write down the evidence for it.

| The evidence shows | Make | Read |
| --- | --- | --- |
| Same lifecycle as an existing workflow, with a different reading list, owner or reviewer | A variant inside that workflow | [workflow](references/workflow.md) |
| One more step, check or condition inside an existing stage | A clause in that workflow | [workflow](references/workflow.md) |
| A defect enters at a hand-off between existing stages, and nothing before the next stage catches it | A gate | [gate](references/gate.md) |
| A distinct intent with its own trigger, ending and ownership, which can end without reaching any existing workflow | A new workflow | [workflow](references/workflow.md) |
| The same expertise needed at a new point | An extension of an existing role | [role](references/role.md) |
| Separate, recurring ownership of files, contracts or checks, backed by its own standard | A new role, or a split | [role](references/role.md) |
| A repeated step-by-step procedure that is useful to call by name | A skill | [skill](references/skill.md) |
| A workflow, gate, role or skill that no longer earns its cost, or is being replaced or renamed | A retirement or relaxation | [retire](references/retire.md) |
| A reusable technical obligation, or approved product behavior | Not this skill | [maintain-knowledge](../maintain-knowledge/SKILL.md) |

Tell the owner the result under the name they gave. Wanting a slash command for something is a sign that it is a procedure, so a skill, not a workflow.

A new kind of task is a row in the [workflow index](../../../docs/workflows/README.md) that points to a workflow or a variant. Individual tasks are routed by the session; they are never created as files.

Do not create a task registry, a coordinator or dispatcher agent, per-team copies of one workflow, a role per feature or per component, or a skill that only repeats a workflow's gates.

## Decision (step 3)

Write a decision from the [decision template](../../../docs/templates/decision.md):

- **Context:** the evidence, including how many runs it rests on.
- **Decision and reason:** the classification, and why it beats the next row of the table.
- **Consequences:** every file that will change, the boundaries with neighbouring workflows or roles, and what the change does not authorize.
- **Approval:** the owner's words and the date. Until then the status is Proposed.

Numbering, what an approval covers and when it must come are in step 3 of [changing the harness](../../../docs/workflows/knowledge-maintenance.md#changing-the-harness).

## Write and connect (steps 4 and 5)

Open only the reference for the kind you chose and follow its file table. Write one canonical file for the item. Everything else links to it and does not repeat it. Use the [templates](../../../docs/templates/README.md).

## Prove (step 6)

Follow [verify](references/verify.md): run the check script, probe each tool the team uses in a new session with the request phrase, and hand the change to an independent reviewer. Record results and limits in the change record.

## Output

Return, and record in the change record:

- the classification and its evidence;
- the decision, its number and status;
- files created and changed;
- the request phrase and where it was recorded;
- the check script result;
- probe results for each tool, with the tool version;
- limits, and what still needs the owner: approval, commit, publication.

## Limits

This skill does not approve product behavior, authorize implementation, commit, push or change external systems. A harness item stays proposed until its decision is approved, and unverified until its probes have run; say so in those words. Keep secrets, user data and private rulebooks out of the harness. A convention kept only in chat or in one agent's private memory is promoted with this skill, and the private copy is then removed.
