# Operations

Layer: starter set. Keep this workflow when the project releases or operates external systems. Authority: [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

Stages: prepared, authorized, executed, verified, recorded.

**Trigger.** A release, a change to an external provider or environment, or incident recovery. Source-only infrastructure changes also keep their delivery and review route.

## Shared boundaries

Identify the target environment and account, current state, expected effects, recovery path and authorization. Inspection, source edits, plan generation and external execution are four distinct actions. Reuse existing authorization when it covers the exact operation. Prepare a concrete, reviewable result before requesting any missing approval. Review or a source change alone never authorizes execution.

## Release

1. Identify the exact candidate, environment and prerequisites from current source and live state. Separate merge readiness from deployment readiness.
2. Prepare the execution and recovery plan, owner handoffs, and health and journey checks. Resolve missing prerequisites and verify authorization.
3. Execute only the authorized plan and candidate. Inspect the actual result, health and the relevant user journey. Source tests or a successful command exit do not prove deployed behavior.
4. Record the date, target, revision, actual checks and results, recovery taken and limits, without secrets. Reconcile current references through [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md). A merge never implies deployment.

## Incident and recovery

1. Establish observed impact and uncertainty from current evidence; identify the owners and permitted actions.
2. Contain and recover within authorization, preserving evidence. Urgency does not permit resetting shared data or changing unrelated services.
3. Verify health and affected journeys after recovery, then record what happened and the remaining risks.
4. Route permanent repairs through [bounded change](bounded-change.md) or [feature delivery](feature-delivery.md), and durable prevention guidance through [knowledge maintenance](knowledge-maintenance.md).

**Resume.** Keep the checkpoint and transitions under [DOC-004](../standards/documentation.md#delivery-task-records). On resume, verify the actual environment state before continuing. Do not repeat a possibly completed operation from a stale next action.
