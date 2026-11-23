# Documentation standard

Layer: framework core. Authority: [DEC-001](../decisions/DEC-001-task-routed-guidance.md), [DEC-003](../decisions/DEC-003-planning-notes.md), [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md). These are documentation rules. They do not approve any product, interface or data design.

## DOC-001 — Route by intended action

**Trigger:** starting a repository task, or changing its scope.

**Rule:** read the [router](../README.md) and the applicable topic instructions before making the relevant decision. Route by what the task changes, not by the agent's title. Read the affected capability requirements as well as the technical standards. If required guidance does not exist, name the gap and propose it. State the documents and rule IDs you are relying on before substantive work. A delegated agent reads the sources itself, even when the assigning agent supplied a summary. Skills describe procedure; do not copy requirements into them.

**Verify:** the task's plan or handoff names the applicable rule IDs. A newly created topic has a route in an index.

## DOC-002 — Give rules and decisions stable identities

**Trigger:** adding a rule or a substantive decision.

**Rule:** inspect existing IDs, then assign the next unused ID in the relevant prefix: `DOC` (documentation), `DEV` (cross-cutting development), `TEST`, `DEC` (decisions), and any topic prefix the project has introduced for a real need. IDs are never renumbered or reused. Headings, paragraphs and progress entries do not each need an ID.

Every rule states its **ID and title, trigger, requirement and verification**, and links the decision that approved it. A decision lives in `docs/decisions/DEC-NNN-<topic>.md` and is listed in the [decision index](../decisions/README.md).

**Verify:** search the repository for the ID. One authoritative definition exists, and its links resolve.

## DOC-003 — Record decisions without inventing approval

**Trigger:** proposing, approving, postponing or replacing a substantive decision.

**Rule:** record the context, the choice, the reason over the main alternative, the consequences, the status and the affected rules, using the [decision template](../templates/decision.md). Approval is recorded as the human, the date and a short quote or a durable reference. Keep proposed guidance out of active standards until it is approved. A recommendation, a successful implementation or permission to investigate is not approval. For a substantive reversal, add a new decision, mark the previous one superseded and link both ways. Minor wording corrections need no decision.

Approving documentation does not authorize implementation, commits or deployment.

**Verify:** every approved decision has explicit approval evidence, and current rules agree with it.

## DOC-004 — Keep one source of truth

**Trigger:** editing guidance or documenting implementation.

**Rule:** standards hold current technical obligations. Capability requirements hold approved behavior. Decisions hold rationale and approval. Implementation references hold verified facts. A change has its own plan, checkpoint and evidence. `docs/work/README.md` is a short index of current work. Link between these; do not copy paragraphs. Entry files and indexes route readers; they do not restate rules. Do not label a proposal as implemented.

When relocating guidance, preserve its approval and verification, remove the duplicate and repair the routes.

**Verify:** check affected links and claims about source code. Trace changed behavior through the change plan, the implementation reference, the indexes and the references of earlier features it touches. Do not update only the newest document. No conflicting active copies remain.

### Capabilities, changes and iterations

A capability folder holds what exists now. A change folder holds one effort.

```text
docs/capabilities/<capability>/
  README.md          purpose, aliases, current scope, owning roles, reading routes, list of changes
  requirements.md    approved behavior as it is now
  reference.md       implementation as it is now, verified against source
  history.md         one row per event, linking to the original evidence
  changes/<change>/  plan.md, build-plan.md, evidence.md for one effort
```

- A new iteration of an existing feature is a **new change** with its own folder. It goes through the same workflow as any other change.
- The iteration rewrites `requirements.md` and `reference.md` so they describe the product after it, updates the README's scope and change list, and adds a row to `history.md`.
- Earlier change records stay in place with their dated approvals, findings and results. Reopening old work creates a new change that links to the old record; it does not edit it.
- The capability documents must explain today's behavior without requiring any past plan.

Cross-domain, tooling and harness changes that belong to no capability use `docs/work/changes/<change>/`.

### Delivery task records

Every [delivery](../glossary.md) has an on-disk checkpoint before implementation, including a small local correction before a pull request exists. Reuse the owning build plan or change record. If none exists, create a short one from the [compact template](../templates/compact-change.md). Assignments to agents are rows in the parent build plan, not extra folders. Transient questions stay in session context.

- **Current checkpoint:** objective and scope, authorization, workflow and stage, owner and affected paths, branch and base revision, implementation, verification and documentation status, assigned reviews and results, unresolved findings and the next action. Update it before review handoff, suspension or any other meaningful transition, and at completion. Session memory and a future pull request description are not substitutes.
- **Stage names:** use the stage names declared by the selected workflow. The states *blocked*, *suspended*, *resumed*, *changes required* and *complete* can apply at any stage.
- **Transition history:** append a short entry: timestamp with timezone, previous → next stage, actor, reason with finding or decision references, and next action. Record meaningful transitions, not every message, tool call or CI poll. Keep earlier entries. Do not fabricate timestamps or retrospective transitions; label reconstructed milestones.
- **Discovery:** the [work index](../work/README.md) links every unfinished top-level delivery, including suspended work, to its checkpoint. It is a directory and does not copy state.
- **Resume:** verify the checkpoint against the actual branch and base, working diff, changed dependencies, review findings and pull request state before following its next action. Never infer an approval, a successful operation or a passed check.
- **Retention:** completed records stay in place. Remove completed deliveries from the active list and link them from the capability history or the work index's delivery list. Do not create duplicate archives.

**Verify:** a fresh session can find each unfinished delivery, read its checkpoint, inspect its transition history and compare both with actual evidence. No delivery depends on chat-only state.

### Closeout gate

Apply before completion review, at implementation handoff, after an authorized commit, push or pull request operation, and when a resumed session learns of a merge. The main session owns the gate. An implementing or testing agent finishing is not closeout. Use [maintain-knowledge](../../.agents/skills/maintain-knowledge/SKILL.md) to perform it. Every delivery receives independent documentation verification under the [review workflow](../workflows/review.md).

- **Affected knowledge:** account for the capability README, requirements, reference and history, the owning plan, checkpoint and evidence, the work index, and shared references and consumers. Record each affected destination as **updated**, **verified unchanged with a reason**, or **outstanding with an owner**. Group unchanged destinations. Do not require an edit to every file.
- **Observed state:** keep implemented and verified, published, and deployed separate. Check local Git and the relevant remote when publication is in scope. Never infer deployment. If remote evidence is unavailable, say what is unverified and the next verification action.
- **One current checkpoint:** update the checkpoint and the transition history. Keep prior approvals, findings and results as dated evidence.
- **Publication wording:** from the first push, write status that stays true before and after integration: name the target branch and the pull request. Put changing observations such as open or pending state and CI results in dated evidence. In shared files, name the change and its pull request; do not write "this change", "new" or "current". Never mark a future operation as done.

**Verify:** compare the checkpoint and affected references with actual source, Git and pull request observations. A scenario listed as untested cannot also be claimed as passed. Read each changed status line in a shared file as it will read on the integration branch after merge. A material contradiction or an unowned documentation gap leaves the gate incomplete. This is an agent obligation. No Git or CI mechanism enforces it.

## DOC-005 — Review guidance from elsewhere before importing it

**Trigger:** considering guidance from a previous harness, an earlier version of the project, another repository or a retired document.

**Rule:** identify the exact material and the purpose, and get the owner's approval to review it unless they already asked for that review. After inspection, propose what to keep, change or reject. Adoption needs its own approval. Record approved adoption in a decision, then express the current rule in this repository's standards so later agents do not need the old source. A link to old material is not authority.

**Verify:** the adoption record names the source, the approvals and the affected rule IDs.

## File lifecycle

Create a file only when substantive content exists. Use the [templates](../templates/README.md). Every active rule has one home.

| Type and location | Create when | Authoritative for | Update or retire when | Keep out |
| --- | --- | --- | --- | --- |
| Capability `README.md` | A capability needs durable context | Purpose, aliases, current scope, owning roles, reading routes by task, dependencies, active changes | Scope, routes or availability change | Full requirements, algorithms, delivery transcript |
| `requirements.md` | Approved behavior is established | Behavior and journeys, permissions, edge cases, exclusions, acceptance, decision links | Approved behavior changes | Schemas, queries, unapproved policy |
| `reference.md` | Implemented boundaries are verified | Verification revision and date, responsibility-to-file map, interfaces, reuse and extension limits, tests and commands, known gaps | Implementation or location changes | Planned paths shown as implemented; deployment claims from source checks |
| `history.md` | A capability has meaningful evolution | Chronological index: date, change and current consequence, original evidence, evidence status | A material change, or historical reconciliation | Full requirements, copied logs, invented approvals |
| `changes/<change>/plan.md` | A substantial change is selected | Outcome and exclusions, authorization, requirements and contracts, acceptance, review findings and dispositions | Scope, contracts or findings change; kept after completion | Other changes' plans; permanent role instructions |
| `changes/<change>/build-plan.md` | A substantial delivery is planned | Current checkpoint, task/owner/path/dependency table, transition history | Meaningful transitions and closeout; kept after completion | Conversation transcript; invented gates |
| `changes/<change>/record.md` | A bounded delivery starts with no owning record | Compact checkpoint, checks, document dispositions, transition history | Meaningful transitions and closeout | A full dossier for a small fix |
| `changes/<change>/evidence.md` | Dated verification is too long for the owning record | Date, revision, environment, command, actual result, limits | Append; never relabel old checks | Secrets; current-status authority |
| `docs/planning/<topic>-temporary.md` | Planning starts on an unsettled scope | Nothing. It holds the owner's requirements, sourced facts, dated decisions and strikeable defaults | Emptied into the owning documents and deleted when planning closes | Approval claims; code; the agent's details presented as the owner's decisions |
| `standards/<topic>.md` | An approved reusable obligation exists | Stable ID, trigger, rule, verification, approving decision | Approved change or supersession | Task progress, proposed policy, tutorials |
| `decisions/DEC-NNN-*.md` | A substantive choice needs its rationale kept | The DOC-003 shape with real approval evidence | The decision, approval or supersession changes | A second rulebook; assumed approval |
| `agents/<role>.md` | A distinct recurring responsibility exists | Purpose, context selection, ownership and limits, checks and handoff | Responsibility or required reading changes | Capability facts, old assignments, a copy of a workflow |
| `workflows/<task>.md` | A distinct task lifecycle needs its own selection, ownership or gates, and no existing workflow owns it | Trigger, prerequisites, steps, stage names, gates with their decisions, output, resume | The procedure changes by decision | Role expertise, feature-specific contracts |
| Tool registrations | A role must be invocable in a tool | Name, description, tool access, instruction to read the canonical brief | Role, path or tool configuration changes; check every tool | A copy of the brief; claims of permanent memory |
| `SKILL.md` | A reusable procedure benefits from tool discovery and concrete steps | Trigger, inputs, steps, validation, output | The procedure changes | Product policy; a restatement of a workflow's gates |
| `docs/work/README.md` | A top-level delivery starts, suspends or completes | Links to active checkpoints; delivered list; separately marked unselected follow-ups | Membership or checkpoint location changes | Copied checkpoints, every assignment, competing next-action narratives |
| Retirement record, in the owning change | Superseded guidance is removed | Source revision and path, where each part went, Git provenance, verified callers | Written before removal | Full copies of old guides |

## Retiring superseded guidance

Old guidance is kept in Git history, not copied into an archive folder. Before removing a file, move current facts and constraints to references or standards, rationale and approval to decisions, and meaningful dated results to the owning change's evidence. Record where each part went. An ordinary current question must be answerable from the repository without retrieving a deleted file.

Cite history by commit, path and section. Check that the cited commit stays reachable after the intended merge strategy. If squash merging would discard it, publish a retention tag at that commit first and record its name.

## Verification of guidance changes

Verify moved links and anchors, rule IDs and source claims. Follow one realistic task from the router to the role, workflow and capability. Check loader paths and skill discovery when they are affected; the [change-harness check script](../../.agents/skills/change-harness/scripts/check_harness.py) covers registrations, skill links, indexes, links and placeholders. Validate a complex routing change with an actual bounded run in each tool. A failed or unavailable probe is a recorded limit. An agent's own report that it read a file is not proof.
