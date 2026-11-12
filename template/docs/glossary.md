# Glossary

Layer: framework core. Each term has one definition here. Other files link to it.

| Term | Meaning |
| --- | --- |
| Chat or session | One conversation with an agent. It can contain several tasks. It is not a unit of work. |
| Task | A unit of work with an objective, a domain, a selected workflow, a responsible agent, required sources, an authorization and a current stage. |
| Transient task | A question or short investigation. Its state stays in the session. Lasting conclusions move to the document that owns them. |
| Delivery | A task that changes the repository. It has an on-disk checkpoint before implementation starts, however small it is. |
| Assignment | A bounded piece of a delivery given to one agent. It is a row in the parent's build plan, with no folder of its own. An assignment finishing is not the delivery finishing. |
| Workflow | The lifecycle selected for a kind of task: trigger, context, steps and owners, stages, gates, output and resume. |
| Stage | A named position inside a workflow. Each workflow declares its own stage names. |
| Gate | Evidence that must exist before a delivery moves to the next stage. Every gate links the decision that added it. |
| Skill | A reusable procedure with concrete steps, discovered by the tool and called from workflows. |
| Role | A recurring responsibility with one canonical brief in `docs/agents/`. |
| Loader | A tool-specific registration that makes a role invocable and tells it to read its brief. |
| Main session | The session the user talks to. It routes, assigns, integrates and owns checkpoints and knowledge reconciliation. |
| Domain | An area of the project with its own expertise and entry point. |
| Capability | A durable area of product behavior, with current requirements and a current implementation reference. Often called a feature. |
| Change | One effort that alters a capability or the repository. It has its own record under `changes/<change>/`. A second iteration of a feature is a new change. |
| Checkpoint | The current state of a delivery, written in its build plan or compact record. |
| Transition history | The dated list of meaningful stage changes for a delivery. |
| Requirement | Approved behavior of a capability. |
| Standard | A reusable technical obligation with a stable ID, a trigger, a rule and a verification. |
| Decision | A record of a substantive choice, its reason and its actual approval. |
| Reference | A verified description of what the implementation does and where. |
| Closeout gate | The check, before completion, that every affected document is updated, verified unchanged with a reason, or outstanding with an owner. |
| Product owner | The person who decides product behavior. In this project: {{PRODUCT_OWNER}}. |
