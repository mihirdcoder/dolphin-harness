# {{PROJECT}} guidance

Layer: framework core. The table rows are project slots.

Start with the [session protocol](workflows/session.md), then select the active task's [workflow](workflows/README.md) and the domain below. Reclassify at meaningful task transitions; do not choose one workflow for the whole chat. Read current capability knowledge and the applicable standards before deciding or editing. Load historical decisions only for approval, rationale or a conflict. Do not reconstruct current behavior from past delivery plans.

| Domain or task | Entry | Owner (project slot) |
| --- | --- | --- |
| Product behavior, capability discovery, current journeys | [Capability index](capabilities/README.md); [question workflow](workflows/question.md) | [Domain Expert](agents/domain-expert.md) |
| Architecture or feature delivery | The selected capability and change; [feature delivery](workflows/feature-delivery.md) | [Architect](agents/architect.md) |
| Test existing functionality without repairs | [Verification](workflows/verification.md) | [Tester](agents/tester.md) |
| Review selection, domain review or final pull request readiness | [Review workflow](workflows/review.md) | The selected [reviewer role](agents/README.md) |
| Guidance or durable knowledge updates | [Documentation standard](standards/documentation.md) and [maintain-knowledge](../.agents/skills/maintain-knowledge/SKILL.md) | Main session |
| Resume existing work | [Work index](work/README.md), the owning checkpoint and verified current Git state | Main session |

<!-- Add one row per additional domain (for example infrastructure, data, a core library): its entry document and owning role. -->

[Roles](agents/README.md) define responsibility. [Workflows](workflows/README.md) define sequence. [Standards](standards/README.md) define obligations. [Decisions](decisions/README.md) preserve rationale and approval. The [glossary](glossary.md) defines the terms used across all of them.

Tool setup: [agent registration](reference/agent-setup.md). Superseded guidance is kept in Git history under the [retirement protocol](standards/documentation.md#retiring-superseded-guidance), not in an archive folder.
