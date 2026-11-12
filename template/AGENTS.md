# {{PROJECT}} task entry

Before substantive work, read [the task router](docs/README.md) and [session protocol](docs/workflows/session.md). Route each task; do not assign one workflow to the whole chat, and keep ongoing work alive across side questions. Identify intent, domain or capability, workflow, responsible agent, required sources, authorization and current gate. A question or a planning request is not authorization to implement. An implementation request still follows its prerequisites.

- Questions about product behavior: the [question workflow](docs/workflows/question.md) and the [capability index](docs/capabilities/README.md).
- Settling with {{PRODUCT_OWNER}} what a feature or change is, before a plan exists: [planning workflow](docs/workflows/planning.md).
- Durable decisions, documentation, role or workflow changes, and delivery reconciliation: [maintain-knowledge](.agents/skills/maintain-knowledge/SKILL.md).

For development, read the [development standard](docs/standards/development.md) and the standards the task actually touches. New features and material changes follow [feature delivery](docs/workflows/feature-delivery.md). Small corrections follow [bounded change](docs/workflows/bounded-change.md). Use the [review workflow](docs/workflows/review.md) to select reviewers. Agents check prerequisites themselves. A missing required independent review is incomplete; it is never replaced silently by self-review.

Canonical role briefs live in `docs/agents/`. Tool registrations load those same files; see [agent setup](docs/reference/agent-setup.md). The main session owns integration, on-disk delivery checkpoints and knowledge reconciliation. Every agent reads its assigned sources itself.

Runtime code lives in {{CODE_ROOTS}}. Feature branches target `{{INTEGRATION_BRANCH}}`; `{{PRODUCTION_BRANCH}}` is production. Preserve unrelated changes. Commit, push, merge, destructive resets and external operations each require task authorization.
