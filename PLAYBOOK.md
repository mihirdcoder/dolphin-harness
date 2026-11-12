# Playbook

What to do in each situation a project meets. Each entry gives the rule, what is created or updated, what must point to it, what keeps it current, and how the originating project did it. Paths are inside the adopted project and match [template/](template/).

The authoritative rules are in `docs/standards/documentation.md` (when each file exists) and `docs/workflows/` (the sequences). This playbook only routes to them.

## Starting a project with nothing

- **Create:** `AGENTS.md`, `CLAUDE.md`, `docs/README.md` (router), the workflows, the documentation standard, the role briefs and loaders, the maintain-knowledge skill, an empty capability index and work index.
- **Do not create:** capability folders, standards or roles that have no content yet. Empty scaffolding reads as a rule that does not exist.
- **Keeps it current:** the adoption itself is recorded as the first change.
- **See:** [ADOPT.md](ADOPT.md).

## Adding the first feature, or any new capability

- **Rule:** a capability is a durable area of the product. Create its folder when it has real content.
- **Create:** `docs/capabilities/<capability>/README.md` and `requirements.md` once behavior is approved, then `changes/<change>/plan.md` and `build-plan.md` for the delivery. `reference.md` is written when code exists and has been verified.
- **Points to it:** the capability index, with search aliases and owning roles. The work index links the unfinished delivery.
- **Keeps it current:** the closeout gate at the end of the delivery.
- **Originating example:** each capability README carried a short "read this for that task" table, so an agent could go from a request to the three files it needed.

## Iterating on an existing feature

- **Rule:** a new iteration is a new change. It never edits the old plan.
- **Create:** `changes/<new-change>/` with its own plan and checkpoint.
- **Update:** `requirements.md` and `reference.md` are rewritten to describe the product after the iteration. The README lists the new change. `history.md` gains one row linking to the evidence, and the superseded row says what remains true.
- **Leave alone:** earlier change records, with their dated approvals and results.
- **Keeps it current:** the closeout gate requires a disposition for the README, requirements, reference and history.
- **Originating example:** a results page was delivered, then replaced five days later by a redesigned presentation. Both change folders remain. The history row for the first reads "initial presentation superseded; readiness requirements remain current."

## Scope is not settled yet

- **Rule:** use the planning workflow before any plan exists.
- **Create:** `docs/planning/<topic>-temporary.md` with the owner's requirements in their words, then sourced facts, then dated decisions, then the agent's strikeable defaults.
- **End:** approved behavior moves to requirements, rationale to a decision, scope and acceptance to the change plan. The temporary file is deleted.
- **Rule inside it:** only product decisions are put to the owner.

## A small fix

- **Rule:** use the bounded-change workflow when impact is understood and approved behavior and contracts do not change.
- **Create:** a compact record, or a new entry in the existing change record. No feature dossier.
- **Review:** one qualified independent reviewer may cover the correction, the existing test evidence and the documentation.

## A kind of task keeps recurring

- **Ask:** does it have its own lifecycle, with different triggers, owners or gates from every existing workflow?
- **If no:** add a variant or a paragraph to the workflow that already owns that lifecycle.
- **If yes:** follow "Changing the harness" in `docs/workflows/knowledge-maintenance.md`: evidence, check for extension, decision, write from the template, connect the index, prove with a real task.

## A kind of expertise keeps recurring

- **Ask:** is there a distinct responsibility or ownership boundary that has shown up more than once?
- **If yes:** write one canonical brief in `docs/agents/`, add a thin loader for each tool, add a row to the role index, and say in the review or delivery workflow when the role is selected.
- **Do not:** create a role for a single feature, or copy the brief into the loaders.
- **Originating example:** a design role produced interactive mockups with a specific review tool. The role (owns journeys and mockups before production code) is the reusable part. The tool is that project's implementation, named in the brief.

## A review found something the process missed

- **Rule:** trace where each finding came from. If an existing gate could not have caught it, the process has a gap.
- **Create:** a decision with the evidence, then a new step or gate in the owning workflow, annotated with that decision.
- **Originating example:** the second architecture gate, described in [PRINCIPLES.md](PRINCIPLES.md#13-the-harness-changes-by-decision-and-gates-are-earned).

## A gate or role is no longer earning its cost

- **Rule:** remove it the same way it was added: a decision with the reason, then update the workflow, index and registrations. Keep the old decision and mark it superseded.

## A useful habit exists only in chat or agent memory

- **Rule:** promote it. Write the procedure into the owning workflow, add the file's lifecycle row if it creates a file, and record the decision. Then remove the private copy.

## Guidance has been replaced

- **Rule:** before deleting, move current facts to references, rationale to decisions and dated results to the owning change's evidence. Record where each part went. Old text stays in Git history, cited by commit, and is not copied into an archive folder.
- **Create:** a retirement record inside the change that did the replacing.

## Resuming work in a new session

- **Read:** the work index, then the owning checkpoint and its transition history.
- **Verify first:** compare the checkpoint with the actual branch, diff, dependencies, review findings and pull request state. Reconcile any disagreement before following the recorded next action.

## Integrating a newer base branch

- **Rule:** a clean merge does not prove the guidance still agrees. Check for colliding decision or rule IDs and for workflow prerequisites that changed, then refresh the affected sources and review coverage.
- **Originating example:** two branches each created a decision with the same number. The published one kept its number and the local one was renumbered, with a note recording why.

## Publishing or merging

- **Rule:** from the first push, write status so it stays true before and after the merge: name the branch and pull request, and avoid "this change", "new" and "current" in shared files. Changing observations such as CI results go in dated evidence.
- **Why:** a record that needs editing after every merge creates an endless loop of status-only commits.
