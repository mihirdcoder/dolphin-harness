# Plan with the product owner

Layer: starter set. Authority: [DEC-003](../decisions/DEC-003-planning-notes.md). Keep this workflow when someone other than the agent decides product behavior.

Stages: notes open, points settled one at a time, closed on the owner's authorization.

**Trigger and selection.** The product owner says "let's plan this", or a request arrives whose scope is not settled: what the product should do and for whom, what it costs, what touches legal or privacy, how wide the first release is. Select this before [feature delivery](feature-delivery.md), which starts from a settled scope. A settled request goes straight to feature delivery or [bounded change](bounded-change.md). An ordinary question uses [question](question.md). Planning applies to an existing capability as well as a new one, and can end in a feature, a bounded change or an answer.

**Inputs and authorization.** The owner's requirements in their own words, and facts about the current product read from capability knowledge and code. When a domain expert is needed, say so, run it, and bring back a short reading labelled as that expert's view. Planning authorizes reading and writing the planning notes. It never authorizes code, mockups, commits, pushes or pull requests.

**Steps.** The main session runs planning with the owner.

1. Open `docs/planning/<topic>-temporary.md` using the [planning notes template](../templates/planning-notes.md): the owner's requirements first, then facts with their sources, then decisions as they are made, then defaults and proposals.
2. Discuss one point at a time, in prose and plain words. Bring only the facts that point needs, give a short view, let the owner decide, and write the decision down with its date and the owner's words. No option menus, no bundled conclusions, no code names.
3. Put to the owner only product decisions: what the product does for a user, what it costs, what touches legal or privacy, what widens or narrows scope. Everything else your own proposal raises gets a default that you set and record as strikeable. It is never a question. When unsure whether a point is the owner's, it is not: set the default and show it.
4. Settle a point before recording it as a decision. A point the owner has not decided stays a proposal.
5. When no product decision is pending, say so. The owner authorizes the close.

**Gate.** Planning is closed when the notes hold every decision dated in the owner's words, no question is pending, and every remaining detail has a strikeable default.

**Failure handling.** Proposal details raised as decisions: withdraw them and set defaults. A missing fact: read the source or consult the domain expert; do not guess. A decision the owner declines to make now: record it as postponed with what it blocks, and continue only with the parts it does not block.

**Output.** On the owner's authorization, close through [knowledge maintenance](knowledge-maintenance.md): approved behavior into the owning capability's requirements, creating the capability when it is new; rationale and approval into a decision record; scope, exclusions, acceptance checks and proposals into `changes/<change>/plan.md`, or into a bounded change. Then delete the temporary file. Development needs its own go-ahead afterwards.

**Resume.** The notes file is the checkpoint. On resume, inspect the branch and the file, state the [session](session.md) entry block and continue from the first unsettled point. Nothing in the notes is a requirement until it has moved.
