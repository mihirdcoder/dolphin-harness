# DEC-004 — Per-task routing, review by impact and durable delivery state

Status: Approved
Date: decided in the originating project; carried into the harness on 2026-11-10
Approval: the harness author, 2026-11-10, confirming these decisions were taken and ship as approved. An adopting project inherits this decision; it changes it by recording a superseding decision of its own.

## Context

In the originating project, delivery and documentation closeout needed repeated intervention from the owner. One workflow was being applied to a whole chat. Reviews scoped too narrowly missed an affected consumer or a stale record, and a fixed review roster over-reviewed small fixes. Delivery state held in chat was lost between sessions.

## Decision and reason

- Route each task and reclassify at meaningful transitions. A side question keeps the parent task alive.
- Select review coverage by actual impact, from the completed diff and its consumers. Small bounded changes may use one qualified independent reviewer. Material deliveries get separate reviewers, including documentation.
- Independence cannot be self-certified. An unavailable required check is incomplete.
- Every delivery has an on-disk checkpoint and an appended transition history, discoverable from a work index and verified against reality on resume.
- Workflows describe a task's lifecycle and coordination. Skills are for reusable procedures that add more than repeated gates. No coordinator agent, review skill or task registry.

## Consequences and links

[Session protocol](../workflows/session.md); [review workflow](../workflows/review.md); [bounded change](../workflows/bounded-change.md); [delivery task records](../standards/documentation.md#delivery-task-records); [changing the harness](../workflows/knowledge-maintenance.md#changing-the-harness). No automatic enforcement is claimed.
