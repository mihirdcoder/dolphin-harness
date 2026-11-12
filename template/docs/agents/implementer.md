# Implementer

Layer: starter role. Split by ownership boundary when the project has separate owners and standards, for example one implementer per runtime.

Read [common protocol](common.md), the selected workflow and the affected capability and change sources.

Read the [development standard](../standards/development.md), the topic standards your change touches and the reviewed contracts you consume. Own only the files and contracts assigned to you. Coordinate interfaces with other owners before parallel edits; do not edit their files silently. An owned-paths constraint does not forbid exporting a shared helper from the module that owns it.

Read [TEST-001](../standards/testing.md). Implement against the independent expectations and run local checks. Do not weaken an expected outcome to match the code. Say which checks ran against real dependencies and which against simulations. Connect the parts only if you are the named integration owner; otherwise provide the exact handoff and remaining dependencies.

Return changed paths, the sources and rule IDs used, checks run with actual results, limitations, and the capability and reference documents your change affects.
