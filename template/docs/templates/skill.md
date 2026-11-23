# <Skill title>

Copy to `.agents/skills/<name>/SKILL.md` and put this frontmatter at the very top:

```text
---
name: <equal to the folder name>
description: <What it does. Use when <the words people actually use to ask for it>. Not for <the job of the nearest other skill>.>
---
```

Layer and authority: the decision that approved this skill, and the workflow step that calls it.
Inputs (what the caller gives, how arguments are read when it is called by name, what is recovered from the repository):
Procedure (numbered steps; link the workflow and standards, never copy their rules or gates):
Validation (the checks that show the procedure worked):
Output and limits (what it returns and records; what it does not authorize):

Detail needed only for some cases goes in `references/<case>.md`, read only for that case. A deterministic check that has been repeated by hand goes in `scripts/`, using only what every project machine has. Claude Code finds the skill through a relative symlink at `.claude/skills/<name>`; see `docs/reference/agent-setup.md`.
