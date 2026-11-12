# DEC-001 — Task-routed guidance with one source of truth

Status: Approved
Date: decided in the originating project; carried into the harness on 2026-11-10
Approval: the harness author, 2026-11-10, confirming these decisions were taken and ship as approved. An adopting project inherits this decision; it changes it by recording a superseding decision of its own.

## Context

Agents need repository guidance. A single long instruction file is read in full for every task and still misses detail. Guidance copied into prompts, role files and feature documents drifts until two versions disagree.

## Decision and reason

Keep entry files short and route by intended action to topic documents. Give each kind of knowledge one home: capability requirements for approved behavior, standards for reusable technical obligations with stable IDs, decisions for rationale and approval, implementation references for verified facts, and change records for one effort's plan, state and evidence. Keep a capability's current documents separate from its delivery history. Reconcile knowledge as part of finishing every delivery, through one maintenance skill and a closeout gate.

Chosen over one comprehensive instruction file because routed, single-owner documents let an agent read only what a task needs and leave one place to correct when something changes.

## Consequences and links

[Router](../README.md); [documentation standard](../standards/documentation.md) DOC-001 to DOC-005, file lifecycle and closeout gate; [knowledge maintenance](../workflows/knowledge-maintenance.md); [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md). The gates are agent obligations and are not enforced by tooling.
