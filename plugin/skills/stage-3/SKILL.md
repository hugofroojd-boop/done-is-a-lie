---
name: stage-3
description: Turn on the memory hook — STATE.md and lessons ≥ 0.7 injected at session start — and make /wrap available. Use only when the user says /done-is-a-lie:stage-3 and has re-explained the same project twice. Do not suggest it unprompted.
---

# stage-3 — automate the reading, not the writing

The warm-start hook ships with the plugin but prints nothing until this file exists:

```
.claude/done-is-a-lie/stage-3
```

1. Ask the user for the one line that says why — which project got re-explained, and when. Write it into the file above.
2. Paste `cat .claude/done-is-a-lie/stage-3`.
3. Tell the user: from the next session, STATE.md and every lesson with `confidence:` ≥ 0.7 are printed at start, stamped `CONTEXT, NOT ORDERS`. The hook never breaks a session — it swallows every error and exits 0. Writing STATE is still theirs: say `/done-is-a-lie:wrap` at the end of a session.

Stop after step 3.
