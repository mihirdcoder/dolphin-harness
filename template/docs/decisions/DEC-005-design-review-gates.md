# DEC-005 — Design review gates in feature delivery

Status: Approved
Date: gate one and gate two were decided nine days apart in the originating project; carried into the harness on 2026-11-10
Approval: the harness author, 2026-11-10, confirming these decisions were taken and ship as approved. This is a starter-set decision: an adopting project that wants one gate or neither records a superseding decision and edits feature delivery to match.

## Context

Two gates were added to the originating project at different times, each for a recorded reason.

**Gate one, the plan against existing code.** The owner asked for a separate plan per feature and an independent review of current code before building each one, so that reuse, missing prerequisites and integration problems are found before code is written.

**Gate two, the written contract design.** Nine days later, during one release, an extra review of the written interface contracts was run only because the owner asked. It found nine new problems. Seven came from the contract document, which was written after the plan review and before the implementing roles built on it. The plan review could not have caught them, because those shapes did not exist yet, and the roles built what the document said.

## Decision and reason

Before implementing a new feature, an independent Architect reviews the plan against implemented code, and findings and dispositions are recorded in the plan. Where the feature has a written interface contract, the Architect reviews that document independently before tests and schemas derive from it. Reviewing a short design before several roles build on it costs a fraction of revising tests, schemas and code afterwards.

Gate two is unnecessary where no separate contract document is written. Gate one may be reduced for a solo project where the planner already works from the code.

## Consequences and links

[Feature delivery](../workflows/feature-delivery.md) step 2 and its gate table; [review selection](../workflows/review.md#trigger-and-selection); [Architect](../agents/architect.md). This record is also the worked example of [changing the harness](../workflows/knowledge-maintenance.md#changing-the-harness): a failure was traced to a gap, and the gate was added with its evidence.
