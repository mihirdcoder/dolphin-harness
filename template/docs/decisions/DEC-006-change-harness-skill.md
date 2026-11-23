# DEC-006 — A skill for changing the harness

Status: Approved
Date: 2026-11-23
Approval: the harness author, 2026-11-23, in chat: "Approve DEC-006". An adopting project inherits this decision; it changes it by recording a superseding decision of its own.

## Context

[Changing the harness](../workflows/knowledge-maintenance.md#changing-the-harness) gives six steps for every workflow, role, gate and skill. They say what to do, not how to do it for each kind of item. In the originating project the steps were followed and the decisions were well recorded, but the wiring and the proof were incomplete in a recurring way:

- The first specialist roles were registered in one tool only, each with its whole brief inside that tool's registration file. The other tool had no roles until the briefs were moved into canonical files.
- Two skills were added without the second tool's discovery link, which stayed missing for two and five days.
- A new contract-review gate was placed before the plan review it depended on, and the review selection table was not updated. An architect review in a later change found both.
- A new planning workflow was added without a router row or a link from the session protocol.
- Five reviewer roles were added in one change of more than fifty files, and one of the five was probed. After a folder move, sessions that were already running kept the old registrations and failed.

There was also no route for the most common trigger: the owner finishes some work and wants it reusable next time, under a name.

## Decision and reason

Add a `change-harness` skill. Its main entry is capturing work that was just finished as a workflow, role, gate or skill; its other entry is designing one from evidence. It asks the owner only for the words they will use to ask for it, what counts as done and what needs their go-ahead. It classifies the request in a fixed order and keeps one reference per kind of item, each with the files to change, plus references for retirement and verification. A standard-library script checks registrations, discovery links, indexes, links and placeholders. The role and workflow templates gain the fields that history showed were missing, and skill and registration templates are added.

A separate skill rather than a larger maintain-knowledge, because maintain-knowledge runs at the end of every delivery while harness changes are rare and their checklists are long. Merging them would load role-registration rules into every closeout. The originating project kept one maintenance skill for all guidance changes; this decision departs from that for the context cost, and narrows the maintain-knowledge description so the two skills do not compete for the same requests.

## Consequences and links

[change-harness](../../.agents/skills/change-harness/SKILL.md); [changing the harness](../workflows/knowledge-maintenance.md#changing-the-harness), which still owns the six steps; [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md), narrowed; the [skill](../templates/skill.md), [registration](../templates/registration.md), [role](../templates/agent.md) and [workflow](../templates/workflow.md) formats; [registration rules](../reference/agent-setup.md#registrations); a harness-change row in [review selection](../workflows/review.md#trigger-and-selection); a capture row in the [session protocol](../workflows/session.md#continuous-task-routing). An adopting project inherits this decision as part of the framework. The skill authorizes no implementation, commit or publication, and an item it writes stays proposed until that item's own decision is approved.
