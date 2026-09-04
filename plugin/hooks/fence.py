# The write fence. Inert until .claude/done-is-a-lie/stage-2 exists in the
# repository — that file holds the one line naming the failure that earned it.
# Once on, two properties matter more than the logic:
#   1. it fails CLOSED  - unparseable input blocks, loudly
#   2. it is boring     - no network, no state, no cleverness
import json, os, sys
root = os.path.realpath(os.getcwd())
if not os.path.exists(os.path.join(root, ".claude", "done-is-a-lie", "stage-2")):
    sys.exit(0)                       # not turned on: allow everything, say nothing
try:
    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path")
except Exception:
    path = None
if not path:
    print("fence: cannot determine target path", file=sys.stderr)
    sys.exit(2)                       # exit 2 = block, stderr goes to the model
real = os.path.realpath(path)
if not real.startswith(root + os.sep):
    print(f"fence: {path} is outside the repository", file=sys.stderr)
    sys.exit(2)
sys.exit(0)                           # allow
