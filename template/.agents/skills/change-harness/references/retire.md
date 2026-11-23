# Retire, relax or rename

Read with [SKILL.md](../SKILL.md). The [retirement rules](../../../../docs/standards/documentation.md#retiring-superseded-guidance) own what happens to removed text and how history stays reachable.

## Evidence

State the cost: how often the item ran, what it caught, what it cost, and what replaces it. Removal follows the same six steps as addition.

## Procedure

1. **Find every place it appears.** Search for its name, file name, decision number and anchors in workflows, the router, indexes, role briefs, registrations, templates, review selection, `AGENTS.md`, skills and checklists. A retired gate often appears in several stages and in a checklist as well.
2. **Record the superseding decision.** Set the old decision's status to "Superseded by DEC-NNN" and link both ways. When only part of it is superseded, say which part in a line under its status. Never rewrite the old decision's reasoning.
3. **Move what is still true** under the retirement rules, and record where each part went in a retirement record in the change. Publishing a retention tag before a squash merge needs its own authorization.
4. **Remove or replace.** Delete the file or section and fix every inbound link found in step 1. For a role, put a remaining role or "main session" in each owner slot it held. For a role or skill, remove it from every tool so the old name cannot be discovered.
5. **Leave a pointer where agents would look.** Where an agent might still reach for the old item, a short line such as "the X loop is retired; use Y" stops it being rebuilt.

A rename is a retirement of the old name and an addition of the new one, in the same change. Probe the result as [verify](verify.md) describes.
