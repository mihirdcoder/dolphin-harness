# Bounded change

Layer: framework core. Authority: [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

Stages: scoped, implementation, ready for review, verified, complete.

**Trigger.** A focused correction or refactor with understood impact, unchanged approved behavior and unchanged public contracts, and no material architecture decision. Correcting an implementation to match its existing contract qualifies. Unknown impact goes to [investigation](investigation.md). A material change to behavior, contracts or architecture goes to [feature delivery](feature-delivery.md) before dependent edits.

## Sequence

1. Read the affected capability context and standards; inspect code, consumers and reuse. State the intended correction, authorization, owned paths and acceptance checks.
2. Keep a compact on-disk checkpoint under [DOC-004](../standards/documentation.md#delivery-task-records), even before a pull request exists. Reuse the existing change record, or create one from the [compact template](../templates/compact-change.md). Do not create a feature dossier for a typo.
3. The main session may implement a small change and run existing checks, or assign the relevant implementer. Inspect representative shared consumers. Correcting a component is not permission to redesign its behavior.
4. Reconcile affected knowledge with [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md) before completion review. One qualified independent reviewer may check the correction, code quality, existing test evidence and documentation, under [review proportionality](review.md#proportional-executions-and-independence). New independent expectations and changed interface behavior keep their own verification.
5. Owners fix findings and return only the affected coverage to its assigned reviewer. Record results, limits and the next action. Complete the [closeout gate](../standards/documentation.md#closeout-gate).

**Resume.** Through [session verification](session.md#resume-and-handoff), not from an unchecked next-action line. Scope uncertainty pauses dependent edits for investigation.
