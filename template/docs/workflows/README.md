# Choose a workflow

Layer: framework core. The rows marked starter can be edited or removed.

Choose per task and reclassify at meaningful transitions under [session](session.md), not once per chat. A delivery can pass through planning, verification, review and knowledge maintenance while keeping one owning record. Persistence rules live in [DOC-004](../standards/documentation.md#delivery-task-records).

| Intent | Workflow | Boundary | Layer |
| --- | --- | --- | --- |
| Explain behavior or locate implementation | [Question](question.md) | Read-only answer; no repair inferred | Core |
| Trace a problem or assess alternatives | [Investigation](investigation.md) | Evidence and findings before any change decision | Core |
| Settle with the product owner what a feature or change is | [Planning](planning.md) | Only product decisions go to the owner; no code, design artifact or commit | Starter |
| Create or revise interaction designs | [Design](design.md) | A design artifact does not authorize production edits | Starter |
| New feature or material change to behavior, contracts or architecture | [Feature delivery](feature-delivery.md) | Plan, design review, implementation and independent verification | Starter |
| Small correction or refactor that keeps approved behavior and contracts | [Bounded change](bounded-change.md) | Known impact; compact record and an independent check | Core |
| Test existing behavior without repairs | [Verification](verification.md) | Scoped tests and results; no implied fix | Starter |
| Review a plan, implementation or pull request | [Review](review.md) | Coverage selected by impact; independent closure; no automatic fixes | Core |
| Release, provider operation or incident recovery | [Operations](operations.md) | Inspection, source change and execution are separate authorizations | Starter |
| Maintain decisions, references, routing, roles or workflows, or make finished work reusable as a workflow, role or skill | [Knowledge maintenance](knowledge-maintenance.md) | Classify the authority and reconcile affected readers; includes [changing the harness](knowledge-maintenance.md#changing-the-harness) with [change-harness](../../.agents/skills/change-harness/SKILL.md) | Core |

Use [session](session.md) on entry and on resume. Workflows apply to the main session and to assigned agents.

## What a workflow file contains

Use the [workflow template](../templates/workflow.md): trigger and exclusions, required context and authorization, steps and responsible roles, declared stage names, gates and evidence, failure handling, output, and resume. Every gate links the decision that added it. Shared obligations stay in their standard and are linked, not copied.

## When to add one

Extend an existing lifecycle before creating another. A new workflow needs a distinct lifecycle with its own selection, ownership or gates, and is added through [changing the harness](knowledge-maintenance.md#changing-the-harness) with the [change-harness](../../.agents/skills/change-harness/SKILL.md) skill, which also turns a task you just finished into a named workflow or variant. Do not create per-team copies of one lifecycle, a coordinator agent, a skill that only repeats a workflow's gates, or a task registry.
