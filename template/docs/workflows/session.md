# Session entry and resume

Layer: framework core. Authority: [DEC-001](../decisions/DEC-001-task-routed-guidance.md), [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

## Continuous task routing

A chat can contain several [tasks](../glossary.md). Do not assign one workflow or one review roster to the whole chat. The main session routes meaningful transitions itself, with no separate router agent:

| Request | Coordinator action |
| --- | --- |
| Continue the active task | Keep its workflow, stage, ownership and authorization; refresh only affected context |
| Ask a side question | Answer through question or investigation while keeping the parent objective and next action |
| Change scope materially | Reclassify, and revisit the affected investigation, planning or design gates before dependent work |
| Authorize a next phase | Advance only within that authorization, keeping prerequisite gates |
| Start a different task | Establish its context and keep unfinished delivery checkpoints for later resume |
| Ask to make finished work reusable ("make this a workflow", "turn this into an agent") | Route it as a new task under [knowledge maintenance](knowledge-maintenance.md#changing-the-harness), using [change-harness](../../.agents/skills/change-harness/SKILL.md); the finished task's record and diff are its evidence |

Classify at these transitions, not after every message. A side question does not discard or restart a delivery. An assignment finishing is not the parent task finishing.

Before substantive work on a task, state briefly:

```text
Objective / scope; domain and capability:
Selected workflow / stage and responsible agent(s):
Required sources; authorized actions:
Owning checkpoint (delivery) or session context (transient question):
Unresolved findings / next action:
```

Inspect the current branch, revision and working-tree changes before repository work. Honor existing authorization; do not ask again for what is already authorized. A question or investigation does not authorize implementation. Every delivery has an on-disk checkpoint under [DOC-004](../standards/documentation.md#delivery-task-records), including a small local change before a pull request exists. Missing guidance is a gap to resolve; it is not permission to invent policy.

## Minimum sufficient context

1. Select the intent from the [workflow index](README.md) and the domain or capability from the [router](../README.md).
2. Read the selected role and workflow, the capability overview and the current requirements and reference the task needs. Read the development standard for development work. Choose topic standards by actual impact, not by job title.
3. Inspect current code and tests before making implementation claims or architectural recommendations. Follow dependencies when needed. Do not load every capability or decision.
4. Record the sources used in the plan, the assignment or the answer. If evidence conflicts, separate approved intended behavior from observed implementation and take the question to the applicable decision path.

Choose the responsible agent from [roles](../agents/README.md). Invoke a required independent role; do not adopt its label. If a registered role is unavailable, use the [documented fallback](../reference/agent-setup.md#when-a-role-is-unavailable) and disclose it. An unavailable required check stays incomplete under the [review workflow](review.md).

## Assignments and gate checks

Follow the [common agent protocol](../agents/common.md). Give the outcome, authorized actions, selected workflow and gate, source links, owned paths, dependencies, acceptance checks and expected handoff. Receiving agents inspect prerequisites themselves. Never claim review, approval or verification on the strength of an assignment alone. A failed gate means completing the authorized prerequisite work. Ask the user only for a decision or authorization that is truly theirs.

## Resume and handoff

Use the [work index](../work/README.md) to find unfinished deliveries, then read the owning checkpoint and its transition history. Before acting on the recorded next action, verify the checkpoint against the actual branch and base, the working diff, changed dependencies, pull request state and reviewer findings. If they disagree, reconcile the record first. A stale next action is not authority to repeat an operation. A dated check applies to its recorded revision and environment only.

When integrating a newer base branch, check for colliding decision or rule IDs and changed workflow prerequisites as well as textual conflicts. A clean merge does not establish that the guidance still agrees.

Write meaningful state transitions before handing off, pausing or completing. Before completion review, reconcile knowledge through [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md). Report delivered scope, checks, unresolved limits and the next action.
