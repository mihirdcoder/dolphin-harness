# Verify existing functionality

Layer: starter set. Authority: [DEC-004](../decisions/DEC-004-routing-review-and-delivery-state.md).

Stages: scope stated, checks run, results reported.

**Trigger.** A request to test existing behavior without changing it. Verification inside a delivery stays part of that delivery. This standalone route creates no feature plan and no completion-review roster.

1. Establish the question, approved behavior, candidate revision, environment, permitted fixtures and scenarios. Read the affected capability requirements and reference and the [testing standard](../standards/testing.md). A request to verify does not authorize production repairs, provider changes or destructive setup.
2. Select the [Tester](../agents/tester.md). Choose relevant boundary and failure cases and representative consumers, not every suite without purpose.
3. Run the checks against the stated environment and candidate. Separate mocks, local integration, hosted behavior and checks that were not performed. A tool being unavailable is an incomplete check, never a pass.
4. Report scenarios, commands and environment, actual results, reproducible failures and limits. Attach evidence to an existing owning record when there is one.

**Outcome.** A successful verification closes the bounded request. It does not establish whole-feature, pull request or deployed readiness outside the inspected scope. A failure may lead to [investigation](investigation.md) or an authorized [bounded change](bounded-change.md) or [feature delivery](feature-delivery.md). Do not repair silently inside verification.
