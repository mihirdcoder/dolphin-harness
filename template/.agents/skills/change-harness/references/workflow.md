# Workflows, variants and clauses

Read with [SKILL.md](../SKILL.md). The [workflow template](../../../../docs/templates/workflow.md) is the format. The [file lifecycle table](../../../../docs/standards/documentation.md#file-lifecycle) owns when a workflow file exists.

## Choose the smallest fit

- **Clause.** One more step or condition in a stage that already exists. Example from the originating project: after the integration and production branches diverged, the release variant gained one clause about how releases merge. Edit the stage and link the decision beside the clause.
- **Variant.** The same stages and gates with a different reading list, owner or reviewer. Examples: frontend and backend corrections inside bounded change; release and incident inside operations. Add a short named section to the existing workflow. Do not copy the workflow.
- **New workflow.** Justify it with at least one of these:
  - The work has its own intent, and the index routes by intent.
  - It can end without reaching any existing workflow. Planning can end in an answered question, a bounded change or no feature at all.
  - An existing workflow's trigger assumes something this work has not yet established. Feature delivery assumes a settled scope.
  - Its ownership or gates differ from every existing workflow.

  A different team, technology or folder is not a reason.

## Write the workflow

Fill every line of the template. Decide:

- **Stages.** Short names a checkpoint can use. Every checkpoint for this workflow uses exactly these names.
- **Requested as and trigger.** Put the request phrase in the "Requested as" line and in the index row. Selection depends on them.
- **Exclusions.** Name the neighbouring workflows and when to use them instead.
- **Owners.** One role or the main session per step. Use roles that exist; a missing role is a separate change.
- **Gates.** Each gate names the evidence it needs and links its decision. See [gate](gate.md).
- **Authorization.** What needs the owner's go-ahead, from the owner's answers.
- **Output and resume.** What a finished run leaves behind, and where its record lives.

Keep out role expertise, feature-specific contracts, one run's values and copies of standards. Link them.

## Files to change

| File | Change |
| --- | --- |
| `docs/decisions/DEC-NNN-<topic>.md` and the [decision index](../../../../docs/decisions/README.md) | The decision and its row |
| `docs/workflows/<task>.md` | The new workflow, or the clause or variant in the existing one |
| [Workflow index](../../../../docs/workflows/README.md) | One row: the intent in the owner's words, the link, the boundary, the layer |
| [Router](../../../../docs/README.md) | A row when the workflow is the entry for a domain or kind of task. Check it even when you think it is not |
| `AGENTS.md` | A route line when the workflow is a common entry. `CLAUDE.md` imports it; do not edit both |
| Neighbouring workflows | A pointer at the step where work hands over, in both directions |
| [Session protocol](../../../../docs/workflows/session.md) | A row in its routing table when the workflow changes how requests are routed |
| [Review selection](../../../../docs/workflows/review.md#trigger-and-selection) | A row when the workflow adds a gate or a kind of coverage |
| [File lifecycle table](../../../../docs/standards/documentation.md#file-lifecycle) | A row when the workflow creates a new kind of file |
| Role briefs | Only when a role's responsibility or required reading changes |
| [Glossary](../../../../docs/glossary.md) | Only for a new term |

For a variant or clause, usually only the decision, the workflow and the index's boundary text change. Check the router and the review table anyway.

In the originating project a new planning workflow updated the index, the entry file, the next workflow and the lifecycle table. Its router row and a link from the session protocol were never added. The check script cannot see that kind of gap; this table is how you catch it.
