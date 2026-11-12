# Dolphin Harness

A repository-level harness for building software with coding agents. It is a set of Markdown rules, templates and thin tool registrations that tell agents how to route a task, who does what, where knowledge is written and how it stays current as a project grows.

It was distilled from a production project where it evolved over several months of daily use with Claude Code and Codex working in the same repository. The project-specific content has been removed. What remains is the mechanism and the reasons behind it.

## What it gives a project

- **Task routing.** A chat holds many tasks. Each one is classified and given the smallest workflow that fits it.
- **One home for each kind of knowledge.** Requirements, technical standards, decisions, implementation references and delivery records are kept apart, and each rule has one owner.
- **Features that stay maintainable across iterations.** Current knowledge is separate from delivery history, so a second or tenth iteration never requires reading every old plan.
- **Roles that work in more than one tool.** One canonical brief per role, loaded by thin registrations for Claude Code and Codex.
- **Work that survives a session.** Every delivery has an on-disk checkpoint that a fresh session can verify and resume.
- **Self-maintenance.** A closeout gate and a reconciliation skill make updating the knowledge part of finishing the work.
- **A way to change the harness itself.** Workflows, roles and gates are added, changed and removed by a recorded decision.

## What it does not give

Nothing here is enforced by Git or CI. Every gate is an obligation the agent is asked to meet and an independent reviewer is asked to check. It works because the rules are short, routed and written once. It does not guarantee compliance.

## Layout

| Path | Purpose |
| --- | --- |
| [ADOPT.md](ADOPT.md) | Instructions for an agent adapting this harness to a project. Start here when adopting. |
| [PRINCIPLES.md](PRINCIPLES.md) | The ideas, each with its reason. Read this before changing anything. |
| [PLAYBOOK.md](PLAYBOOK.md) | Situation by situation: what to create, what points to it, what keeps it current. |
| [template/](template/) | The files that go into a project. |
| [Article](docs/agentic-development-without-scope-creep.md) | How the harness keeps delegated work in scope and gives agents current context. |
| [Workflow and task lifecycle](docs/workflow-and-task-lifecycle.md) | Stages, ownership, later iterations, and workflow maintenance. |

## Two layers

The template mixes two things, and every file says which it is.

- **Framework.** What a task, workflow, role, skill, capability, change and decision are; when each is created; how each is kept current. This is the part to keep.
- **Starter set.** Concrete workflows, gates and roles that worked in the originating project. They are examples of following the framework. A project should edit, replace or delete them.

## Using it

Open a session in the target project and tell it:

```text
Read <path-to-this-directory>/ADOPT.md and adapt the harness to this project.
```

The adopting agent reads the project first, asks the owner only the questions that are theirs, and writes a harness shaped to that project.
