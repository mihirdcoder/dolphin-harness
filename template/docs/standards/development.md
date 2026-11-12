# Development standard

Layer: starter set. This file is read for every development task, so keep only cross-cutting principles here and link to topic standards for the rest. The rule below is an example from the originating project. Keep it, edit it or replace it with this project's own, and record the approving decision.

For delivery sequence follow [feature delivery](../workflows/feature-delivery.md) or [bounded change](../workflows/bounded-change.md). Read the [testing standard](testing.md) when planning or performing verification.

## DEV-001 — Build the intended design, not a patch over the old one (example)

**Trigger:** designing, implementing or revising code whose existing data and callers are disposable development state.

**Rule:** when a better approach is identified within the authorized task, implement it as the original design should have been built.

- Replace the superseded implementation and update its consumers, tests and documentation together. Remove obsolete paths within scope.
- Do not add compatibility adapters, fallback branches or dual schemas solely to preserve disposable development code or data.
- Keep useful code and legitimate abstractions. This rule favors the simplest coherent implementation. It does not authorize an unrelated rewrite or a wider task.
- Before any reset or deletion, identify the exact environment and confirm it is disposable. This rule does not authorize a destructive command or any change to shared or live data.

**Verify:** the implemented path reflects the intended design, superseded in-scope paths are removed, and tests and a fresh local setup work. Any compatibility mechanism that remains has a named consumer.

This rule stops applying once real or shared data exists. Agree and record the preservation and migration policy before that point.
