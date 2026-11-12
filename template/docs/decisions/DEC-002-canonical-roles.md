# DEC-002 — One canonical role brief with thin tool registrations

Status: Approved
Date: decided in the originating project; carried into the harness on 2026-11-10
Approval: the harness author, 2026-11-10, confirming these decisions were taken and ship as approved. An adopting project inherits this decision; it changes it by recording a superseding decision of its own.

## Context

The team may use more than one coding tool in the same repository. Each tool has its own format for registering a specialist agent. Writing a role's instructions separately in each format produces roles that diverge.

## Decision and reason

Each role has one brief in `docs/agents/<role>.md`, read together with a shared [common protocol](../agents/common.md). Each tool gets a registration that carries only the name, a one-line description, tool access and the instruction to read the brief. Skills live once in `.agents/skills/` and other tools discover them through relative symlinks. A role is created only for demonstrated recurring expertise or ownership, never per feature. A role brief holds no product facts; it says what the role reads, owns, checks and returns.

Chosen over per-tool role definitions so that every tool behaves the same and a role changes in one place.

## Consequences and links

[Role index](../agents/README.md); [agent setup](../reference/agent-setup.md); file lifecycle rows for role briefs, registrations and skills in the [documentation standard](../standards/documentation.md#file-lifecycle). Registrations provide neither permanent memory nor task authorization.
