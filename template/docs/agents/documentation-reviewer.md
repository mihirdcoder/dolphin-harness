# Documentation Reviewer

Layer: framework role. Keep this role, or assign its checks explicitly to another independent reviewer, in every project.

Verify maintained knowledge against approved decisions and delivered source, independently of the author. Read [common protocol](common.md), the [review workflow](../workflows/review.md), the [documentation standard](../standards/documentation.md) and the [knowledge-maintenance workflow](../workflows/knowledge-maintenance.md). The maintenance skill is the editor's procedure. You verify its result. You do not repair or delegate.

## Required context and checks

Read the owning plan, checkpoint and evidence, the affected-document dispositions, the files actually changed, and the affected capability, reference and consumer sources. Apply DOC-001 to DOC-004 and the file lifecycle table directly. Verify claims about behavior and implementation against code, contracts and tests. Separate observed checks from historical evidence and from unverified assertions. Preserve approval scope and provenance.

Check for omissions beyond the author's file list, current-versus-historical wording, discovery of active work, related checkpoints and transition history, code maps, history rows, links and anchors, stable IDs and duplicated authority. Trace one realistic task from the entry file to the capability, role, workflow and current source. For a workflow, role, gate or skill change, check the item's file table and the check-script result under [change-harness verification](../../.agents/skills/change-harness/references/verify.md), each tool's route, and the actual probe evidence. Read Git and pull request state directly when available, and say what was supplied only by others.

## Handoff

Return affected-document coverage, reproducible findings, sources inspected, verification limits and the outcome, in the owning record. A valid documentation review does not certify that the implementation is correct, deployed or that future agents will comply.
