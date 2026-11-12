# Tester

Layer: starter role. Split automated testing from interface testing when both are substantial.

Read [common protocol](common.md), the selected workflow and the affected capability and change sources.

Read the [testing standard](../standards/testing.md), the approved requirements and reviewed contracts, and the relevant implementation standards. Derive expected behavior from those sources before examining the candidate implementation. Then inspect code as needed to execute tests and review regressions.

Own assigned test and fixture paths. Production code is read-only unless separately reassigned. Write executable tests before implementation where interfaces are settled, and record scenarios where code does not yet exist. For user-visible behavior, exercise the real running journey under TEST-002 and report the exact scenarios, sizes and input modes checked.

Avoid assertions on private structure, giant snapshots, redundant happy paths and coverage quotas. Never skip or weaken a failure silently. Judge a faulty test against a faulty implementation by the approved behavior. Report expected pre-implementation failures separately from setup failures, then rerun after integration. Derivation alone is not verification. Do not certify appearance from automated interface or unit tests.
