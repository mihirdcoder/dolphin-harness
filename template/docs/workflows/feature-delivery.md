# Feature delivery

Layer: starter set. The sequence and its gates are one project's choices. Edit them to fit; each gate names the decision that added it, so removing a gate means superseding that decision. Authority: [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md), [DEC-005](../decisions/DEC-005-design-review-gates.md).

Stages: scope, plan reviewed, contracts reviewed, tests derived, implementation, integrated, ready for review, verified, complete.

**Trigger.** A new feature or a material change to behavior, contracts or architecture, with a settled scope. Unsettled scope goes to [planning](planning.md) first. A small correction that keeps approved behavior and contracts uses [bounded change](bounded-change.md).

**Rule.** The coordinating agent keeps a short visible plan before coding. Scope, contracts, acceptance and review findings live in the change's `plan.md`. Ownership, dependencies, gates and the checkpoint live in its `build-plan.md`. The [work index](../work/README.md) holds only a link. A slice has one observable outcome.

During planning, identify coverage under the [review workflow](review.md#trigger-and-selection): design-review gates, who derives independent test expectations, interface scenarios, documentation destinations and anticipated reviewers. Late review cannot replace early gates.

## Delivery sequence

1. **Scope and contracts.** State the outcome, exclusions, applicable rules, accepted designs and acceptance checks. Assign one owner to each shared contract and name who connects the parts. Resolve material missing decisions; do not design product policy silently.
2. **Design review before implementation** ([DEC-005](../decisions/DEC-005-design-review-gates.md)). The [Architect](../agents/architect.md) inspects the relevant existing code, tests and contracts against the candidate plan and identifies reuse, missing prerequisites, integration issues and failure cases. Record findings and dispositions in the plan and resolve blockers before coding. A review recommendation cannot override approved requirements.
   **Then, where the feature has written interface contracts:** write the exact contract design (shapes, errors, bounds, examples) from what each consumer needs and from the plan review's dispositions. The Architect reviews that written design independently before tests or schemas derive from it. These are two gates: the plan first, the written contracts second. A material deviation in fields, errors, authorization or persistence reopens the affected gate. Wording corrections do not.
3. **Independent tests first.** The [Tester](../agents/tester.md) derives behavior tests from the reviewed design before implementation, where executable boundaries exist. Separate expected missing-behavior failures from broken test setup.
4. **Build bounded parts.** Each part has one owner and non-overlapping files. Work in parallel only after shared interfaces are settled. Labelled fixtures can unblock work but cannot prove integration.
5. **Connect, exercise and reconcile knowledge.** The named integration owner connects the real parts, removes temporary substitutes and runs developer checks and the agreed journey. The main session reconciles documentation through [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md) and records the ready-for-review transition. The integration owner's run is not independent verification.
6. **Independent verification and fixes.** Finalize assignments from the actual diff under the [review workflow](review.md). The Tester executes its independently derived expectations after integration. Reviewers selected by impact check code quality, feature consistency and documentation. Implementers fix findings; only the reviewer assigned the affected coverage rechecks it.
7. **Close the slice.** Summarize delivered behavior, exact checks and results, limitations and the next action. Complete the [closeout gate](../standards/documentation.md#closeout-gate). Before calling a pull request ready, assess its whole diff under the [final gate](review.md#final-pull-request-readiness).

## Assignments

Each assignment includes the plan link, applicable review findings, requirement and contract links, owned files, allowed edits, dependencies and expected handoff, under the [common protocol](../agents/common.md). The coordinator owns cross-agent integration and overall completion. An owned-paths constraint never forbids exporting a shared helper from its owning module. Test files have a named author; implementers do not rewrite independent expectations to obtain a pass.

## Gates

| Gate | Evidence before advancing |
| --- | --- |
| Scope | Outcome, exclusions, affected capability, authorized actions |
| Context | Current requirements and standards read; existing code, tests and reuse inspected |
| Plan reviewed | Independent code-grounded findings, dispositions and resolved blockers |
| Ready to build | Approved behavior; reviewed contract design where one exists; settled interfaces, owned paths, integration owner and test expectations |
| Implemented | Real connected behavior; temporary substitutes removed |
| Ready for completion review | Developer checks and knowledge reconciliation complete; review assignments and checkpoint recorded |
| Verified | Applicable independent tests, domain reviews and documentation verification, with results and limits |

Complete authorized prerequisites; do not ask repeatedly for permission. A partial slice is labelled partial. Passing builds, an accepted mockup or simulated providers alone do not establish that the feature is ready. Do not claim untested behavior.

**Resume.** Use the checkpoint and transition history in the build plan, verified against Git and review state under [session](session.md#resume-and-handoff).
