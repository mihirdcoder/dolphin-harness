# Investigate

Layer: framework core. Stages: question stated, evidence gathered, findings returned.

State the question or hypothesis, the authorized inspection or reproduction, and the evidence needed. Load the relevant capability requirements, implementation reference and domain owner. Inspect current code, tests and configuration. Reproduce only within authorized resources.

Return confirmed behavior, causes supported by evidence, unresolved hypotheses, affected consumers and a recommended next action. Investigation is not permission to repair, reset, deploy or change policy. If a fix is authorized, select [bounded change](bounded-change.md) or [feature delivery](feature-delivery.md) from the impact you found, before editing.

Resume by checking current source and prior findings under [session](session.md#resume-and-handoff). A transient investigation needs no delivery record. If it becomes an authorized delivery, create its checkpoint under [DOC-004](../standards/documentation.md#delivery-task-records) before dependent changes. Keep the parent delivery when investigation is a phase of that work.
