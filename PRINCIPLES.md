# Principles

Each principle is stated with its reason. The files in [template/](template/) are one way to follow them. When a project changes a file, the principle is the test of whether the change is sound.

## 1. Route the task, not the chat

A chat contains several tasks: a question, then a small fix, then planning a feature. Each needs a different amount of process. The agent classifies each task when it starts and again when it materially changes, and picks the smallest workflow that fits.

*Why:* one process for everything is either too heavy for a question or too light for a feature. Routing per task means a question never turns into a repair, and a typo never drags in a feature team.

A side question does not end the task underneath it. After answering, the agent returns to the parent task.

## 2. Each kind of knowledge has one home

| Kind | Holds | Changes when |
| --- | --- | --- |
| Requirements | Approved behavior of a capability | The owner approves different behavior |
| Standards | Reusable technical obligations with stable IDs | An approved rule changes |
| Decisions | Why a choice was made, and who approved it | A choice is made, postponed or replaced |
| References | What the code does today, verified against source | The implementation changes |
| Delivery records | The plan, state and evidence of one effort | That effort moves forward |

Entry files and indexes route readers to these. They never restate the rules.

*Why:* a rule written in two places drifts. An agent that finds two versions cannot tell which is current.

## 3. Current knowledge and history are different things

A capability's README, requirements and reference describe what exists now. Each change has its own dated record of how it got there. A second iteration is a new change with its own record. It rewrites the current documents and leaves the old records untouched. A thin history index links them in order.

*Why:* an agent starting a task should be able to learn today's behavior from a few current pages, and should not need to replay every past plan. The past still matters for rationale, so it is kept and linked, never rewritten.

## 4. A workflow exists because a kind of task has its own lifecycle

A workflow states the trigger, required context, steps and owners, gates, failure handling, output and how to resume. Create one only when a distinct lifecycle needs its own selection, ownership or gate rules. Extend an existing workflow before adding another.

*Why:* workflows multiply easily. A frontend copy and a backend copy of the same lifecycle diverge within weeks. A small set that is selected by intent stays understood.

## 5. A role exists because a responsibility recurs

Create a role for demonstrated recurring expertise or ownership. Do not create one per feature. A role has one canonical brief. Each tool gets a thin registration that only says "read the brief". The brief names what the role reads, owns, checks and hands back. It does not contain product facts.

*Why:* copying a role's instructions into each tool's format creates two roles that drift apart. One body with thin loaders is what lets Claude Code and Codex behave the same in one repository.

## 6. A skill is a procedure, a workflow is a lifecycle

A workflow says which kind of task this is, who owns each step and what must be true before moving on. A skill says how to carry out one procedure step by step. Workflows call skills. Do not wrap a workflow in a skill only to repeat its gates.

## 7. The main session coordinates, and every agent reads for itself

The main session routes the task, assigns bounded work, integrates the results and owns the checkpoint and the knowledge. Each assignment states the outcome, authorized actions, sources, owned paths, acceptance checks and expected handoff. The receiving agent reads the sources itself. A summary from the sender is orientation only.

*Why:* summaries lose the detail that matters. An agent that works from a summary builds what the summary said.

## 8. Independence cannot be self-certified

The author of a change cannot be its independent reviewer. If a required independent check cannot run, it is recorded as incomplete. It is never replaced silently by self-review, and a human accepting the risk does not turn it into a pass.

## 9. Planning separates the owner's decisions from the agent's details

Before a plan exists, an unsettled scope is worked out in a scratch file that has no authority. Only product decisions go to the product owner: what the product does, for whom, what it costs, what widens or narrows scope. Everything else the agent's own proposal raises gets a default that the owner can strike. When planning closes, the decided parts move to their permanent homes and the scratch file is deleted.

*Why:* an agent that asks the owner about every detail hides the three decisions that matter among thirty that do not.

## 10. Delivery state lives on disk

Every delivery has a checkpoint before implementation starts: objective, authorization, workflow and stage, owner, branch, status, findings and next action. Meaningful transitions are appended with a timestamp, actor and reason. A fresh session resumes by reading the checkpoint and then verifying it against the actual branch, diff and review state before acting.

*Why:* chat memory ends with the session. A stale "next action" followed blindly repeats an operation that already happened.

## 11. Finishing includes reconciling the knowledge

Before completion, each affected document is marked updated, verified unchanged with a reason, or outstanding with an owner. An independent reviewer checks that list. This is what keeps the current documents true as the code changes.

## 12. A convention that lives only in memory is not part of the harness

When a working habit proves useful, it is promoted into the repository as a workflow, a file-lifecycle entry and a decision.

*From the originating project:* the planning scratch file began as a convention held in one agent's private memory. Other agents could not follow it, and nothing stopped the agent from presenting its own details as the owner's decisions. It became a workflow only after that failure.

## 13. The harness changes by decision, and gates are earned

A workflow, role, gate or standard is added when evidence shows the need: a recurring task, recurring expertise, or a failure the process missed. A decision records the reason and the approval. Then the index, router and registrations are updated, and one real task is run through the change. The most common evidence is work just finished that the owner wants to repeat: it is captured under a name while the run is fresh, and the owner's words for asking become the trigger that is tested.

*From the originating project:* feature delivery had one architecture review, of the plan. During one release an extra review of the written API contracts, run only because the owner asked, found nine new problems. Seven came from the contract document written after the plan review, so the first review could not have caught them. A second gate was added by decision, with that evidence attached. A project without written contracts would not need it.

## 14. Proportion

A small correction gets a compact record and one independent reviewer. A new feature gets a plan, design review, independent tests and separate reviewers. Roles and reviews are selected by actual impact, never from a fixed roster.

## 15. Say only what was observed

Implemented, verified, published and deployed are separate states, and none is inferred from another. A proposal is never labelled as implemented. A check that did not run is never reported as passed. Approval is recorded with the human's actual words or a durable reference.

## Framework and starter set

| Framework: keep | Starter set: edit, replace or delete |
| --- | --- |
| Session protocol and task routing | The seven steps of feature delivery |
| The four knowledge homes and the file lifecycle table | The two architecture review gates |
| Capability and change structure, history index | The planning conversation rules |
| Delivery checkpoints and transition history | The design and operations workflows |
| Closeout gate and the maintain-knowledge skill | The seven starter roles |
| The change-harness skill and its check script | |
| Canonical role body with thin loaders | The example development and testing rules |
| The procedure for changing the harness | The design-review decision (DEC-005), which a project may supersede |
| The framework decisions (DEC-001 to DEC-004 and DEC-006) | |
| The rule that every gate has a recorded reason | |
