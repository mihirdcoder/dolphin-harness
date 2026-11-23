# Gates

Read with [SKILL.md](../SKILL.md). A gate is evidence that must exist before a delivery moves to the next stage ([glossary](../../../../docs/glossary.md)). [DEC-005](../../../../docs/decisions/DEC-005-design-review-gates.md) is the worked example.

## Evidence for a gate

Trace each finding the process missed:

1. Which step introduced the defect?
2. At which stage did the evidence needed to see it first exist?
3. Which existing gate could have caught it, and why did it not?

If an existing gate could have caught it, fix that gate's instructions instead of adding a gate. If none could, put the new gate at the earliest stage where its evidence exists. A gate placed before its evidence exists checks nothing. A gate placed after dependent work is built costs rework. Compare what the gate reviews with the rework it prevents, and write that comparison in the decision.

Do not add a gate from a single preference. Do not apply a new gate to deliveries that already finished; never write a retrospective review that did not happen.

## Place it

In the owning workflow, a gate needs:

- the step that produces the evidence;
- the gate itself, after every gate it depends on. Check the ordering: in the originating project a new contract gate was first placed before the plan review it depended on;
- the step that consumes the result, now asking for the reviewed version;
- the assignments that carry it;
- the row in the workflow's gate table and its verify line;
- what reopens the gate (a material deviation) and what does not (a wording correction);
- the decision link beside the gate.

## Files to change

| File | Change |
| --- | --- |
| Decision and [decision index](../../../../docs/decisions/README.md) | Each finding, where it came from, and why no existing gate caught it |
| Owning workflow | Every place listed above |
| [Workflow index](../../../../docs/workflows/README.md) | The boundary text, when it names the workflow's gates |
| [Review selection](../../../../docs/workflows/review.md#trigger-and-selection) | A row: impact, required coverage, who. In the originating project this was the step that got missed |
| [Build plan](../../../../docs/templates/build-plan.md) or [compact record](../../../../docs/templates/compact-change.md) template | A field for the gate's evidence, when checkpoints must record it |
| The role that performs the check | Its brief, only if its responsibility or required reading changes |
| The standard the gate enforces | The rule, if the gate enforces a rule that is not yet written |

## Relax or remove a gate

A gate that costs more than it catches is removed the way it was added; see [retire](retire.md). In the originating project, mandatory separate review runs for every delivery were replaced within three days by review selected by impact, because they cost too much on small changes. Record the cost evidence the same way as failure evidence.
