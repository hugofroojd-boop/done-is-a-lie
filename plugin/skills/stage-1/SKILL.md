---
name: stage-1
description: Build stage 1 of done-is-a-lie in the current repository — CLAUDE.md, NON-GOALS.md, STATE.md, LESSONS.md — then stop. Use when the user says /done-is-a-lie:stage-1, "set up the four files", or hands you the document and says "build stage 1 only".
---

# stage-1 — the four files, then stop

Read STATE first, work, update STATE last. That habit is the user's. These four files are yours to create. Nothing else.

1. Confirm the current directory is a git repository and you were started inside it. If not, stop and say so — one repository is the workspace.
2. For each file below: if it already exists, **do not overwrite it**; show its first lines and ask. Otherwise write it exactly as given.
3. Run `ls -la CLAUDE.md NON-GOALS.md STATE.md LESSONS.md` and paste the output. Then stop. Do not build a gate, a hook, a skill, or a subagent workflow. Do not commit.

## CLAUDE.md

Replace the placeholder line with one paragraph about this project. Keep the rest verbatim.

```markdown
# CLAUDE.md
## What this is
<one paragraph: what the project is for — not how it works>
## Non-goals
See NON-GOALS.md. That file wins.
If a task touches one of them: stop and ask. Never change it quietly.
## Prime directives
1. No unverifiable claims. Every statement about state must be
   derivable from the filesystem, git, or the database.
2. Nothing is "done" until verification has run and its output
   is quoted — not summarised. The check must exercise the claim.
3. Report before any bulk delete, move or rename.
## Rhythm
Read STATE.md first. Update it last. Four lines are enough.
Lessons go in LESSONS.md, never here. Status never goes here.
```

## NON-GOALS.md

The first two lines hold for every project. Ask the user for up to three of their own; if they have none yet, keep the three examples.

```markdown
# NON-GOALS.md
Standing negative requirements. A goal is met and closed; a non-goal holds
until someone deletes the line. This file wins over anything CLAUDE.md says.

- Never write outside this repository.
- Nothing is published, deployed or paid for without me saying so.
- No new dependencies without asking.
- No background services.
- No more than three skills.
```

## STATE.md

Four lines, nothing else. Fill them from what is actually true right now — `git log -3` and `git status` are the source, not your guess.

```markdown
Last done:   <what the previous session finished>
In progress: <what is half-built right now>
Next:        <the one thing to do next>
Blocked:     <what is waiting on someone, or nothing>
```

## LESSONS.md

```markdown
# LESSONS.md
```

That is the whole stage. The gate (`/done-is-a-lie:stage-2`) and the memory hook (`/done-is-a-lie:stage-3`) exist, switched off. Do not turn them on. The user will, the day a rule is ignored or a project is re-explained twice.
