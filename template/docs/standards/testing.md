# Testing standard

Layer: starter set. The two rules below carry the harness's independence principle into testing. Add the project's own commands, environments and conventions.

## TEST-001 — Independent expectations

**Trigger:** a delivery introduces or materially changes behavior.

**Rule:** expected behavior is derived from approved requirements and reviewed contracts by someone other than the implementer, before the implementation is examined, and where executable boundaries exist before it is written. The implementer does not weaken or rewrite those expectations to obtain a pass. A coordinator rerunning an existing suite for a small bounded change is not a new independent expectation and does not need a separate tester.

**Verify:** the record names who derived the tests, when they ran and the actual results. Derivation alone is not verification. Expected missing-behavior failures are reported separately from broken setup. Skipped checks are named.

## TEST-002 — Real execution for user-visible behavior

**Trigger:** a delivery changes what a user sees or does.

**Rule:** the affected journey is exercised in the real running system, connected to its real dependencies in the stated environment, by someone other than the implementer. Automated unit or interface tests do not certify appearance or interaction. Reviewing code is not execution.

**Verify:** the record states the environment, the exact scenarios and sizes or input modes checked, the results and what was not checked. A tool being unavailable is an incomplete check.
