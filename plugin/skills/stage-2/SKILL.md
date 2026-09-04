---
name: stage-2
description: Turn on the write fence — the one gate in done-is-a-lie. Use only when the user says /done-is-a-lie:stage-2 and names a failure that happened (a rule in CLAUDE.md was ignored at least once). Do not suggest it unprompted.
---

# stage-2 — one gate, after the failure

A rule in a prompt is a request; a rule in a hook is a boundary. The fence ships with the plugin but does nothing until this file exists in the repository:

```
.claude/done-is-a-lie/stage-2
```

1. Ask the user to name the incident in one line. Write that line into the file above (create the directory). The line is the reason the gate exists; without it, do not create the file.
2. Paste `cat .claude/done-is-a-lie/stage-2`.
3. Verify the mechanism, not the intention: ask the user to run one write outside the repository with the fence on and confirm it is blocked (`fence: … is outside the repository`, exit 2). Then delete the marker, repeat, confirm it succeeds, and put the marker back. If the failure never occurs with the gate off, the gate is decoration — say so.

What the fence protects: the file-writing tools — Edit, Write, MultiEdit. What it does not: shell commands, subprocesses, scripts that write files. It is a repository write fence, not a security sandbox. Pair it with `git status` before and after a job.

Stop after step 3. Do not turn on stage 3.
