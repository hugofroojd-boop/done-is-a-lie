# template/ — stage 1, ready to copy

Copy the four files into the root of your repository. Or run `/done-is-a-lie:stage-1` and let the plugin do it.

**Change only these:**
- the one paragraph under *What this is* in `CLAUDE.md`
- the non-goals after the first two lines in `NON-GOALS.md` — those two hold for every project; the other three are defaults, not laws
- the four lines of `STATE.md`, from what is actually true today

**Do not change:**
- the prime directives — especially *the check must exercise the claim*
- the rhythm: read STATE first, update it last
- what each file is for: instructions in `CLAUDE.md`, never status; status in `STATE.md`, never lessons; lessons in `LESSONS.md`, each with a number

**Decide before you start, in one line each:**
1. What must the agent never touch, publish, deploy or pay for? → non-goals
2. Which dependencies need your approval? → a non-goal
3. What counts as verification here — which command proves "done"? → the prime directive, made concrete
4. Who says yes to a deploy? → a non-goal, with a name
5. Where does the repository end? → `cd` into it before `claude`; the fence in `later/` turns that into a gate, after the failure

`later/` holds stages 2–3. Do not copy them until the failure they answer has happened.
