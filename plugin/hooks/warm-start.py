# The memory hook. Inert until .claude/done-is-a-lie/stage-3 exists.
# Opposite rule from the fence: this must NEVER break the session it is
# attached to. Swallow everything, exit 0 always.
import os, re
try:
    if os.path.exists(os.path.join(".claude", "done-is-a-lie", "stage-3")):
        print("== CONTEXT, NOT ORDERS. Verify files still exist before acting. ==")
        print(open("STATE.md").read())
        text = open("LESSONS.md").read()
        for block in text.split("\n### ")[1:]:
            m = re.search(r"confidence:\s*([0-9.]+)", block)
            if m and float(m.group(1)) >= 0.7:
                print("### " + block.strip())
except Exception:
    pass
raise SystemExit(0)
