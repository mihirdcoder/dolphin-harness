# Maintain knowledge

Layer: framework core. Authority: [DEC-001](../decisions/DEC-001-task-routed-guidance.md), [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

Stages: classified, written, connected, verified.

**Trigger.** A durable decision, a change to guidance or a reference, conflicting documentation, a meaningful delivery transition, handoff or completion, and any change to the harness itself.

Use the [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md) skill for the procedure, and [change-harness](../../.agents/skills/change-harness/SKILL.md) when the change is to a workflow, role, gate or skill. The [documentation standard](../standards/documentation.md) owns file lifecycle, record formats and authority. Read the affected capability and change sources and the approval evidence before editing. An idea that was discussed remains a proposal.

The main session owns reconciliation before completion review and after fixes. Agents report the constraints and affected consumers they discover. One editor owns each shared file. Apply the [closeout gate](../standards/documentation.md#closeout-gate) and [delivery task records](../standards/documentation.md#delivery-task-records). Link to those rules; do not copy them into prompts.

Independent verification is assigned through [review selection](review.md#proportional-executions-and-independence). A verified-unchanged result needs a source-based reason that is checked independently.

Do not rewrite role briefs for every feature decision. Update the authority the brief links to. Change a brief only when its responsibilities or required reading change.

## Changing the harness

Adding, changing or removing a workflow, a gate, a role, a skill or a standard is one lifecycle. Use it for all of them. The [change-harness](../../.agents/skills/change-harness/SKILL.md) skill carries out these steps for workflows, roles, gates and skills, including turning work that was just finished into a reusable, named item. A standard follows the same steps through maintain-knowledge.

1. **Evidence.** State what prompts the change: a kind of task that keeps recurring, work just finished that the owner wants to repeat, expertise that keeps recurring, a failure the process missed, or a step that no longer earns its cost. For a missed failure, trace where each finding came from and which existing gate could have caught it. One finished run is enough evidence when the owner says the work will recur; the decision records that it rests on one run. Without that statement, a new workflow or role needs more than one run.
2. **Check for extension.** Decide whether an existing workflow, role or standard can absorb the change. Use the creation conditions in the [file lifecycle table](../standards/documentation.md#file-lifecycle). Prefer extending.
3. **Decision.** Record the reason, the evidence and the actual approval in a [decision](../templates/decision.md). A removal supersedes the decision that added the item; the old decision is kept and linked. Approval covers only what it names: approving a workflow does not authorize creating roles for it, running them or committing. Check open branches before taking a decision number. Steps 4 to 6 may run before approval, on an unmerged branch, as evidence for the decision. Approval comes before merge, and until then the item is described as proposed.
4. **Write.** Use the [template](../templates/README.md). One canonical file. A workflow declares its stage names and links the decision beside each gate. A role brief contains no product facts.
5. **Connect.** Update every index and route that should lead to it: the [router](../README.md), the [workflow index](README.md) or [role index](../agents/README.md), the [review selection table](review.md#trigger-and-selection), entry files, and one loader per tool for a role. For a removal, remove every inbound link.
6. **Prove.** Run one real, bounded task through the change in a new session of each tool the team uses, asked in the words people will use and without naming the item, and record what happened. A probe that failed or could not run is a recorded limit. Final prose saying an agent read a file is not evidence.

A working convention that exists only in chat or in an agent's private memory is not part of the harness. When one proves useful, promote it through these six steps and remove the private copy.
