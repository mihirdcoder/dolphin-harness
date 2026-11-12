---
name: maintain-knowledge
description: Reconcile approved decisions, implementation knowledge, workflows, role reading routes and delivery records. Use for durable guidance changes, documentation migrations, meaningful delivery transitions, review handoff or completion, after publication or a reported merge, and when adding, changing or removing a workflow, role, gate or standard. Does not approve product policy.
---

# Maintain repository knowledge

Read the [documentation standard](../../../docs/standards/documentation.md) and the affected capability or work record. Use the [router](../../../docs/README.md) to locate the authority. Do not load every domain or historical plan. The standard owns file lifecycle and formats. This skill owns the reconciliation procedure. Templates are in [docs/templates](../../../docs/templates/README.md).

## Inputs

Establish what changed or was learned, the actual approval and status evidence, the scope (shared, one domain, one capability or one change), what it replaces or extends, and the affected implementation and consumers. Recover these from the authorized task and from source evidence. Ask only when a substantive decision is missing. An idea that was discussed is not an approved rule.

## Procedure

1. **Search first.** Look for existing IDs, requirements, code references and callers. Choose one authoritative destination from the [file lifecycle table](../../../docs/standards/documentation.md#file-lifecycle) before writing. For delivery work, locate or create its on-disk owner under [delivery task records](../../../docs/standards/documentation.md#delivery-task-records). Prefer updating an existing topic over adding an overlapping file.
2. **Classify.** Approved behavior goes to capability requirements. A reusable technical obligation goes to a standard. Rationale and approval go to a decision. Verified code or configuration facts go to a reference. One effort's scope, state and results go to its plan, build plan and evidence. Discovery goes to the router or a role brief. Procedure goes to a workflow or skill. Split a mixed discussion by responsibility and link the parts.
3. **Respect status.** Record proposals as proposed decisions or plans, never as active requirements. For an approval, keep the evidence and scope, update the owning rule and add supersession links. A pure relocation keeps its IDs and approval and creates no new decision.
4. **Verify implementation claims.** Check actual sources, update code maps, interfaces and tests listed in the reference, and separate local source verification from live deployment. Record adoption that is still outstanding across consumers.
5. **Repair routes.** Fix inbound links, anchors and affected reading routes. Update a role brief only when its responsibilities or required reading change. Update every tool's registration and skill discovery when a path or registration changes. Do not copy shared rules into prompts. One editor owns a shared file during parallel work.
6. **Apply the closeout gate.** Before completion review and at handoff, inspect the actual changed files and the references that consume them. Record a disposition for each affected document: updated, verified unchanged with a reason, or outstanding with an owner. Include shared indexes and the capability's history index, not only the files edited for the feature. Rewrite the capability's current documents so they describe the product as it now is; leave earlier change records untouched. Keep current status short and move long results to `evidence.md`.
7. **Retire carefully.** Before removing a file, inventory its facts, rationale, approvals, results and unresolved gaps against the documents that will own them. Extract what is missing without copying the whole narrative. Record the Git revision, path and section, verify current callers, and confirm the commit will stay reachable after the intended merge.
8. **Update the delivery record.** At a meaningful transition, update the checkpoint, append the transition, and maintain the work index entry. On resume, verify Git, the diff, dependencies, findings and remote state before following the next action. After an authorized publication, record the observed result. Keep implementation, verification, publication and deployment separate.
9. **Verify.** Check relative links and anchors, stable IDs, agreement between approval and status, and source claims. Follow one realistic task route. Check registrations and symlinks after a role or skill change. A complex workflow change needs an actual bounded run; never claim reading or delegation from final prose alone.

## Changing the harness

For a workflow, role, gate, skill or standard, follow the six steps in [changing the harness](../../../docs/workflows/knowledge-maintenance.md#changing-the-harness): evidence, check for extension, decision, write from the template, connect, prove. The same steps apply to a removal.

## Example: an approved interface rule

The owner approves a rule for how animations behave. Update the interface standard with the scope, verification and decision link. Update the shared-component reference with the tokens and components that actually implement it. If existing screens are unchanged, link the outstanding adoption. The roles that build and test the interface already read that standard, so their briefs change only if this introduces a new required reading route.

## Output and limits

Return the authoritative documents changed or verified unchanged, routing and role changes, superseded records, the observed delivery state, outstanding adoption and gaps with owners, the checks run and the exact next action. Hand the document dispositions and state evidence to the reviewer assigned documentation coverage under the [review workflow](../../../docs/workflows/review.md). A no-change result is valid with a stated reason; the checkpoint and transition history are still required.

This skill cannot authorize implementation, publication, destructive operations or changes to external systems. Follow DOC-005 before importing guidance from elsewhere. Keep secrets, user data and private rulebooks out of guidance. Add a supporting script only for repeated deterministic work that has actually been demonstrated.
