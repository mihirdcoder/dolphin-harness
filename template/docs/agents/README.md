# Roles

Layer: framework core. The roster is a starter set.

Each role has one canonical brief here and a thin registration per tool. Read the [common protocol](common.md) plus the selected role. [Workflows](../workflows/README.md) determine sequence. The main session coordinates assignments, integration, checkpoints and knowledge maintenance.

| Role | Use for |
| --- | --- |
| [domain-expert](domain-expert.md) | Questions about current behavior, capability discovery, scope clarification |
| [architect](architect.md) | Code-grounded review of plans and contract designs before implementation |
| [implementer](implementer.md) | Assigned production code within owned paths |
| [tester](tester.md) | Independent expectations, automated tests and real execution of journeys |
| [reviewer](reviewer.md) | Independent review of implementation quality and feature consistency |
| [documentation-reviewer](documentation-reviewer.md) | Independent check that knowledge matches decisions and delivered source |
| [pr-readiness-reviewer](pr-readiness-reviewer.md) | Final independent pull request assessment for material deliveries |

Invoked agents load current knowledge. A registration provides neither permanent memory nor task authorization. Small bounded work may be implemented by the main session. Roles describe responsibilities; the [review workflow](../workflows/review.md) decides which run for a given task.

## When to add or split a role

Create a role only for demonstrated recurring expertise or ownership, never for one feature. Split a role when two parts of the system have separate owners and separate standards, for example an implementer per runtime boundary, a designer who produces mockups before production code, or a specialist for an external provider. A role that depends on a particular tool names that tool in its brief; the role is the responsibility, and the tool is this project's way of carrying it out.

Add, change or remove a role through [changing the harness](../workflows/knowledge-maintenance.md#changing-the-harness), using the [role template](../templates/agent.md). Registration and the fallback for an unavailable role are in [agent setup](../reference/agent-setup.md).
