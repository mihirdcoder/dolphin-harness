# Adopting the harness in a project

These instructions are for an agent session opened in a target project and pointed at this directory. Your job is to adapt the harness to that project. Copying it unchanged is a failure: the template contains a starter set that belongs to another project's history.

Do not commit, push, delete existing guidance or change code unless the owner has authorized that action.

## 1. Read before writing

1. Read [PRINCIPLES.md](PRINCIPLES.md) and [PLAYBOOK.md](PLAYBOOK.md) in full.
2. Read the template in this order: `template/AGENTS.md`, `template/docs/README.md`, `template/docs/glossary.md`, `template/docs/workflows/README.md` and `session.md`, `template/docs/standards/documentation.md`, `template/docs/agents/README.md` and `common.md`, `template/.agents/skills/maintain-knowledge/SKILL.md`. Read the remaining workflows and roles as you decide whether to keep them.

## 2. Inspect the target project

Establish these from the repository, not from assumption:

- Existing agent guidance: `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.codex/`, `.agents/`, `.cursor/`, any `docs/` conventions, contribution guides.
- Code roots, languages, test and build commands, and whether there is a user interface, a database, external providers or deployable infrastructure.
- Branch model: the integration branch, the production branch and how changes are merged.
- CI and what it enforces.
- The durable areas of the product that already exist in code. These are candidate capabilities.
- Which coding tools the team uses: Claude Code, Codex or both.

Existing guidance is not overwritten. Treat it under DOC-005 in `template/docs/standards/documentation.md`: inventory it, propose what to keep, change or drop, and get the owner's approval before retiring anything.

## 3. Ask the owner only what is theirs

Put these to the owner, one at a time, in plain words. Decide everything else yourself and show it as a default they can strike.

1. Who decides product behavior? This person is the product owner in the planning workflow.
2. What are the project's domains? A domain is an area with its own expertise and entry point, such as product, infrastructure, data pipeline or a core library.
3. Which starter workflows and gates should the project keep? Recommend a set sized to the project (section 5) and say why.
4. Which tools need registrations?

## 4. Fill the placeholders

| Placeholder | Meaning |
| --- | --- |
| `{{PROJECT}}` | Project name |
| `{{PRODUCT_OWNER}}` | The person or role who decides product behavior |
| `{{INTEGRATION_BRANCH}}` | Branch that feature work targets |
| `{{PRODUCTION_BRANCH}}` | Branch that is released |
| `{{CODE_ROOTS}}` | Top-level directories that hold runtime code |

Search the copied files for `{{` when you finish. None may remain.

## 5. Choose what to keep

Every template file states its layer on its first lines.

**Framework core. Keep in every project:**

- `AGENTS.md`, `CLAUDE.md`, `docs/README.md`, `docs/glossary.md`
- `docs/workflows/`: `README.md`, `session.md`, `question.md`, `investigation.md`, `bounded-change.md`, `review.md`, `knowledge-maintenance.md`
- `docs/standards/documentation.md`
- `docs/agents/README.md`, `common.md`
- `docs/templates/`, `docs/decisions/README.md`, `docs/capabilities/README.md`, `docs/work/README.md`, `docs/reference/agent-setup.md`
- `.agents/skills/maintain-knowledge/`

**Starter set. Keep, edit or delete by evidence:**

| File | Keep when |
| --- | --- |
| `workflows/planning.md` | Someone other than the agent decides product behavior |
| `workflows/feature-delivery.md` | The project builds features larger than a bounded change. Edit its gates to fit. |
| `workflows/design.md` | There is a user interface designed before it is built |
| `workflows/verification.md` | Existing behavior is tested on request, apart from delivery |
| `workflows/operations.md` | The project deploys or operates external systems |
| `standards/development.md`, `standards/testing.md` | Replace the example rules with the project's own |
| Roles in `docs/agents/` | Section 6 |

Suggested sizes:

- **Solo or small tool:** core plus `feature-delivery.md` reduced to scope, build, independent review and closeout. Roles: implementer and reviewer.
- **Product with one team:** core plus planning, feature delivery with one design review, verification. Roles: domain expert, architect, implementer, tester, reviewer, documentation reviewer.
- **Product with several boundaries and providers:** the full starter set, with the implementer and reviewer split along real ownership boundaries.

When you remove a workflow or gate, remove every link to it from the entry file, the router, the workflow index, the review selection table, the role briefs and the templates. When you remove a role, put a role the project kept (or "main session") in every owner slot that named it: the third column of the router and of the review selection table. Coverage rows stay; only who carries them changes.

### The solo setup, worked through

This is what the smallest setup looks like when it is consistent. Use it as the check for any reduced setup.

| File | What it says after adoption |
| --- | --- |
| `AGENTS.md` | No planning line if `planning.md` is dropped. Feature work points to the reduced `feature-delivery.md`. |
| `docs/README.md` | Owner column: main session for product behavior, feature delivery and knowledge; reviewer for review. No verification row if `verification.md` is dropped. |
| `workflows/feature-delivery.md` | Four steps: scope, build, independent review, closeout. No design-review gates. |
| `workflows/review.md` | The two starter-gate rows are removed. Every other row stays, with the reviewer in the third column. The documentation and final-assessment paragraphs name a fresh-context run of the reviewer. |
| `docs/agents/README.md` | Two rows: implementer and reviewer. Five briefs and their loaders are deleted. |
| `docs/decisions/` | DEC-001 to DEC-004 unchanged. DEC-005 marked superseded by DEC-006 (section 7). |

A solo project still gets independence: the reviewer runs in a fresh context and is never the session that wrote the change. If that cannot happen, the check is recorded as incomplete.

## 6. Shape the roster

Start with the smallest roster that covers the project's real boundaries. Rename roles to the project's words. Split a role only where ownership is truly separate, for example frontend and backend with different standards. For each role you keep:

1. Edit `docs/agents/<role>.md`: what it reads, owns, checks and returns. Name the project's tools in the brief where a role depends on one.
2. Keep one loader per tool: `.claude/agents/<role>.md` and `.codex/agents/<role>.toml`. A loader holds the name, a one-line description, the tool list and the instruction to read the brief. Never copy the brief into it.
3. Add the role to `docs/agents/README.md`.

Delete the loaders and briefs of roles you drop. If the team uses one tool, delete the other tool's registrations and say so in `docs/reference/agent-setup.md`.

## 7. Carry the inherited decisions

`template/docs/decisions/` holds five decisions that explain why the harness is shaped this way. They were taken in the project the harness came from and arrive **Approved**. Copy them as they are. Do not ask the owner to approve them again.

What the project accepts by adopting:

| Decision | Accepted | Notes |
| --- | --- | --- |
| DEC-001 to DEC-004 | Always | They are the framework. A project that rejects one is not adopting this harness. |
| DEC-005 (two design-review gates) | Only if the project keeps both gates unchanged | Any setup with one gate or none supersedes it during adoption. |

A project changes a decision the way any decision is changed: record a new decision that supersedes it, with the reason and the owner's approval, mark the old one superseded, and update the rule or gate it authorized.

**If the setup chosen in section 5 drops or changes a design-review gate, write the superseding decision now.** Do not leave DEC-005 Approved beside a workflow that contradicts it. Record `DEC-006` from the decision template: what the project does instead, why (project size, no written contracts, a single author), and the owner's answer to question 3 in their words as the approval. Set DEC-005's status to "Superseded by DEC-006", update the decision index, and remove the starter-gate rows from the review selection table. The same applies to any other starter gate removed later.

New project decisions continue the same numbering.

## 8. Seed the knowledge

Create content only where it exists. Do not generate empty folders.

- **Capabilities:** list the real ones in `docs/capabilities/README.md` with aliases and owners. For each one you document now, write the README, and write `reference.md` only from code you have actually read, with the revision and date you verified against.
- **Requirements:** write only behavior the owner confirms. Behavior you inferred from code is recorded in the reference as observed, not in requirements as approved.
- **History:** if you reconstruct it from Git, label it reconstructed and state what evidence is missing. Never invent a past plan, review or approval.
- **Standards:** move the project's real technical rules into topic files with stable IDs. Delete the example rules you do not adopt.
- **Domains:** add one router row per domain, with its entry document and owning role.

## 9. Prove it

1. **Links:** every relative link and anchor in the copied files resolves.
2. **Placeholders:** no `{{` remains.
3. **Registrations:** each role is discoverable in each tool the team uses, and the skill symlink in `.claude/skills/` resolves.
4. **Routes:** run three real probes in a fresh session of each tool and record what happened:
   - a question about existing behavior, answered from the capability documents and code;
   - a small bounded change, ending with a compact record and a closeout disposition;
   - a resume: a new session finds the unfinished work from the work index and verifies the checkpoint against Git before acting.

A probe that fails or cannot run is recorded as a limit. Do not report that agents will comply.

## 10. Record the adoption

The adoption is the project's first delivery. Record it in `docs/work/changes/harness-adoption/record.md` using the compact template: what was adopted, what was dropped and why, the owner's decisions in their words, probe results, and what remains. Link it from `docs/work/README.md`.

Report to the owner: files created, starter items kept and dropped, inherited decisions superseded, probe results and limits.
