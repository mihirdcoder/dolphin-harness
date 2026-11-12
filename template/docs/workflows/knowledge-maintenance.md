# Maintain knowledge

Layer: framework core. Authority: [DEC-001](../decisions/DEC-001-task-routed-guidance.md), [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

Stages: classified, written, connected, verified.

**Trigger.** A durable decision, a change to guidance or a reference, conflicting documentation, a meaningful delivery transition, handoff or completion, and any change to the harness itself.

Use the [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md) skill for the procedure. The [documentation standard](../standards/documentation.md) owns file lifecycle, record formats and authority. Read the affected capability and change sources and the approval evidence before editing. An idea that was discussed remains a proposal.

The main session owns reconciliation before completion review and after fixes. Agents report the constraints and affected consumers they discover. One editor owns each shared file. Apply the [closeout gate](../standards/documentation.md#closeout-gate) and [delivery task records](../standards/documentation.md#delivery-task-records). Link to those rules; do not copy them into prompts.

Independent verification is assigned through [review selection](review.md#proportional-executions-and-independence). A verified-unchanged result needs a source-based reason that is checked independently.

Do not rewrite role briefs for every feature decision. Update the authority the brief links to. Change a brief only when its responsibilities or required reading change.

## Changing the harness

Adding, changing or removing a workflow, a gate, a role, a skill or a standard is one lifecycle. Use it for all of them.

1. **Evidence.** State what prompts the change: a kind of task that keeps recurring, expertise that keeps recurring, a failure the process missed, or a step that no longer earns its cost. For a missed failure, trace where each finding came from and which existing gate could have caught it.
2. **Check for extension.** Decide whether an existing workflow, role or standard can absorb the change. Use the creation conditions in the [file lifecycle table](../standards/documentation.md#file-lifecycle). Prefer extending.
3. **Decision.** Record the reason, the evidence and the actual approval in a [decision](../templates/decision.md). A removal supersedes the decision that added the item; the old decision is kept and linked.
4. **Write.** Use the [template](../templates/README.md). One canonical file. A workflow declares its stage names and links the decision beside each gate. A role brief contains no product facts.
5. **Connect.** Update every index and route that should lead to it: the [router](../README.md), the [workflow index](README.md) or [role index](../agents/README.md), the [review selection table](review.md#trigger-and-selection), entry files, and one loader per tool for a role. For a removal, remove every inbound link.
6. **Prove.** Run one real, bounded task through the change in each tool the team uses, and record what happened. A probe that failed or could not run is a recorded limit. Final prose saying an agent read a file is not evidence.

A working convention that exists only in chat or in an agent's private memory is not part of the harness. When one proves useful, promote it through these six steps and remove the private copy.
