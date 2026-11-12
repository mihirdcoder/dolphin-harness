# DEC-003 — Planning notes before a plan exists

Status: Approved
Date: decided in the originating project; carried into the harness on 2026-11-10
Approval: the harness author, 2026-11-10, confirming these decisions were taken and ship as approved. An adopting project inherits this decision; it changes it by recording a superseding decision of its own.

## Context

Feature delivery starts from a settled scope. The stage before it, settling with the product owner what a feature is, needs a home. In the originating project this began as a convention held only in one agent's private memory. Other agents could not follow it, and the agent following it presented its own proposal details as decisions for the owner, because nothing forbade that.

## Decision and reason

Add a planning workflow, selected before feature delivery. Planning uses a temporary notes file with no authority: the owner's requirements in their words, sourced facts, dated decisions and the agent's strikeable defaults. Only product decisions are put to the owner. On close, the contents move to requirements, decisions and the change plan, and the file is deleted.

A separate workflow, not a step inside feature delivery, because planning can end in no feature, a bounded change or an answer. Working conventions live in the repository and not in any agent's memory.

## Consequences and links

[Planning workflow](../workflows/planning.md); [planning notes template](../templates/planning-notes.md); the planning-notes row in the [file lifecycle table](../standards/documentation.md#file-lifecycle). Approving this workflow authorizes no implementation.
