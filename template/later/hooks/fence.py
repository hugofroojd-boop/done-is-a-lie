# Runs before every file write. Two properties matter
# more than the logic:
#   1. it fails CLOSED  - unparseable input blocks, loudly
#   2. it is boring     - no network, no state, no cleverness
import json, os, sys
try:
    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path")
except Exception:
    path = None
root = os.path.realpath(os.getcwd())
if not path:
    print("fence: cannot determine target path", file=sys.stderr)
    sys.exit(2)                       # exit 2 = block, stderr goes to the model
real = os.path.realpath(path)
if not real.startswith(root + os.sep):
    print(f"fence: {path} is outside the repository", file=sys.stderr)
    sys.exit(2)
sys.exit(0)                           # allow
