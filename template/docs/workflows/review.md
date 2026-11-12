# Review

Layer: framework core. The rows of the selection table are project slots. Authority: [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

Stages: coverage selected, assigned, findings returned, findings closed, final assessment.

This workflow owns coverage selection, independent closure of findings and the final pull request assessment. Standards own the quality obligations themselves.

## Trigger and selection

The main session coordinates review per task and assesses the combined effect of a pull request before calling it ready. An explicit, bounded review request covers only its requested scope and authorizes no repairs; do not report it as approval of a whole delivery. Questions and investigations do not trigger delivery reviews merely because files were read.

**Early coverage.** During planning, identify the applicable design-review gates, who derives independent test expectations, interface scenarios, documentation destinations and anticipated reviewers. Late completion review cannot replace an early gate.

**Completion selection.** Once implementation, developer checks and documentation reconciliation are ready, inspect the actual diff, the approved intent, affected consumers (including unchanged files), existing verification and its limits. Record the required coverage in the build plan or compact record. Select by impact, not by filenames or a fixed roster. The main session makes this assessment itself. Assigned reviewers also look for omitted consumers.

Minimum responsibilities. Add rows for the project's own boundaries, and add coverage when evidence warrants it:

| Impact or gate | Required coverage | Who (project slot; starter roster shown) |
| --- | --- | --- |
| New or materially changed product behavior | Feature consistency and completeness against approved requirements | [Reviewer](../agents/reviewer.md) |
| Implementation code | Code quality and affected consumers | Reviewer |
| New independent expectations, or material feature verification | Expectations derived before implementation where practical, executed after integration | [Tester](../agents/tester.md) |
| User-visible interface behavior | Independent execution of the real journey; unchanged interface files do not waive this | Tester |
| Every delivered change's knowledge reconciliation | Independent documentation verification under the [closeout gate](../standards/documentation.md#closeout-gate) | Any independent reviewer; see [proportionality](#proportional-executions-and-independence) |
| An actual pull request | Complete assessment under the [final gate](#final-pull-request-readiness) | Main session; see the final gate |
| *Starter gate:* new feature or material architecture or scope change | Review of the plan against current code before implementation, under [feature delivery](feature-delivery.md) and [DEC-005](../decisions/DEC-005-design-review-gates.md) | [Architect](../agents/architect.md) |
| *Starter gate:* written contract design, or a material deviation from it | Review before tests and schemas derive from it, under DEC-005 | Architect |

The first two columns of the unmarked rows are the framework. The third column names whoever on this project's roster carries the coverage. On a small roster one role fills several rows; the only fixed rule is that the person or agent is not the author of what they check. The two starter-gate rows exist because of DEC-005. A project that supersedes that decision removes or edits them; no other row is removed without a decision.

Record a scope-based reason for relevant coverage that does not apply. Do not fill a roster of unrelated roles for every task. The coordinator cannot drop an applicable requirement. A tool or agent being unavailable is not inapplicability: use the [setup fallback](../reference/agent-setup.md#when-a-role-is-unavailable), otherwise report the check as incomplete. An explicit human decision may accept a risk; record it, and keep the unperformed check incomplete. It is never relabelled as passed.

### Proportional executions and independence

For a small [bounded change](bounded-change.md), the main session may implement and run existing checks. One qualified independent reviewer may cover the intended correction, code quality, existing test evidence and documentation. Record why those checks cover the risk.

Material feature delivery, and substantial documentation, migration or harness changes, need documentation verification by a reviewer separate from the one who reviewed the code. In the starter roster this is the [Documentation Reviewer](../agents/documentation-reviewer.md); on a smaller roster it is a second fresh-context run of the reviewer role. A verified-unchanged documentation disposition still needs independent checking.

The author of an implementation cannot provide its independent verification. A reviewer who implements a fix cannot independently certify that fix. Reviewing test code does not substitute for running a required test. Reuse an earlier result only with evidence that its scope and freshness still hold.

Testing stays proportional: identify meaningful checks, and record when no executable test is warranted. Do not manufacture redundant tests for a reversible text correction.

## Assign and run

1. Establish the approved requirements, workflow and gate, and the candidate and base. For uncommitted work, identify the base and the changed and untracked files. A branch name alone does not identify reviewed content.
2. Assign selected reviewers bounded responsibilities, source links, affected consumers, prior findings and the expected handoff under the [common protocol](../agents/common.md). Say which roles were actually invoked. Domain reviews and applicable tests may run at the same time when their inputs are ready. The final pull request assessment is last.
3. Reviewers read requirements, standards, current source, tests and evidence themselves, including consumers beyond the assigned file list. Review approved behavior; do not convert preferences into requirements. Review is read-only unless a separate assignment authorizes edits.
4. Owners repair findings within authorization. The main session reconciles affected knowledge and returns the change to the reviewer assigned that coverage.

## Findings, outcomes and freshness

Record in the existing plan, build plan, evidence or compact record: reviewer identity, scope, candidate and base, sources and checks inspected, limitations, findings and dispositions, and the outcome.

A material finding has a local ID, a source location, the requirement or authority it rests on, a concrete consequence, a proposed correction and an independent closure check. Separate failures of an established rule from missing decisions and from optional improvements. The author's response is fixed, disputed or needs decision. "Fixed" waits for the reviewer to verify it. Keep the original finding and its disposition.

Outcomes: **pass**, **changes required**, **incomplete**, or **not applicable with reason**. A pass can carry non-blocking notes. It cannot hide an unavailable required check or an unresolved blocker.

After edits or a changed base, assess the difference and its consumer dependencies. Recheck only the affected reviews, tests and documentation. Carry an unaffected result forward with its original reviewed identity and a short justification. An old approval is not approval of unreviewed changes.

## Final pull request readiness

Every pull request gets a complete assessment by the main session: the whole diff against its target base, and the interaction of its tasks, shared files, contracts and carried reviews. Individually passing task records are not sufficient.

A separate reviewer who took no part in the delivery (in the starter roster, the [PR Readiness Reviewer](../agents/pr-readiness-reviewer.md); on a smaller roster, a fresh-context run of the reviewer role) performs the final independent assessment for a new feature or other material delivery, for material interaction risk between tasks, or on explicit request. A small qualifying delivery uses the main session's assessment.

A ready verdict requires that applicable prior reviews and verification passed or truly do not apply, blocking findings were independently closed, and documentation was reconciled and verified. Refresh the actual target, base and head, the full diff, required CI checks, review feedback and mergeability. Pending, failed, unavailable or absent checks are not passing checks. Readiness is not authorization to merge or deploy.

**Verify.** Early prerequisites and final selection agree; independent assignments and findings are evidenced; fixes were independently checked; documentation has a named verifier. These are agent obligations. Nothing dispatches or enforces them automatically.
