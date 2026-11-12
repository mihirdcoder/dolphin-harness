# Shared agent protocol

Layer: framework core.

Read this with your role brief. Paths that begin with `docs/`, `.agents/` or a code root are relative to the repository root. Markdown links resolve from the file that contains them. Find the root with Git, or search upward for `AGENTS.md` and `docs/README.md`. Report a missing required source; do not skip it silently.

## Assignment and prerequisites

Read the selected workflow and the actual assigned sources yourself. A coordinator's summary is orientation and does not replace them. Every assignment states the outcome and authorized actions, the selected workflow and current gate, the owning plan, requirements and standards, owned files and responsibilities, dependencies and consumers, acceptance checks and the expected handoff. If any is missing, recover it from source and task context, and return material unresolved gaps before dependent work.

A question or review is read-only unless edits are authorized. An implementation assignment does not prove that the plan was approved, that design review happened or that contracts are settled. Verify the applicable prerequisites and report missing ones. Honor existing authorization without asking again. Required independent review cannot be self-certified; use the [setup fallback](../reference/agent-setup.md#when-a-role-is-unavailable) and report what actually ran.

Read the [development standard](../standards/development.md) for development work. Select other standards by what the task actually changes. Use the affected capability's requirements and reference and the selected change plan. Do not load every historical plan or decision. Inspect current code and tests before making implementation claims.

## Ownership and handoff

You are not alone in the codebase. Preserve others' changes. One owner per shared file or contract. Coordinate dependency and integration handoffs before parallel edits. Do not expand silently into another owner's paths or change approved behavior. Further delegation needs authorization. Do not commit, publish, deploy or reset data without authorization for that action.

Return findings or changed paths, the sources and rule IDs used, the checks actually run and their results, limitations and integration dependencies. Name the capability, reference and history documents your work affects and any documentation gap with no owner, even when another agent will edit them. The coordinator owns the [closeout gate](../standards/documentation.md#closeout-gate). A completed assignment is not a completed feature.

Report new durable constraints or conflicts to the coordinator. Keep no private rulebook. Resume from the current owning checkpoint and refresh changed sources. Use the owning [checkpoint and transition history](../standards/documentation.md#delivery-task-records) for meaningful handoffs; do not create an agent-private task list.
