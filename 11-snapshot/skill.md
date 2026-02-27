# Snapshot — Session Continuity Skill

Capture a structured summary of the current Claude session so you can seamlessly continue in a new chat when context limits are reached.

## When to Use

Invoke `/snapshot` when:
- Claude warns about context compression or running low
- You're about to start a new chat and want to preserve context
- You want to save a checkpoint of your current work session

## Your Process

When invoked, follow these steps in order:

### Step 1: Ask for a Session Name and Location

Before doing anything else, ask the user **two questions at once**:

> 1. "What would you like to name this snapshot? (e.g. `snapshot-skill-build`, `auth-refactor`, `feedback-sdk-analysis`)"
> 2. "Where should it be saved? (default: `~/.claude/sessions/` — or provide a custom path)"

Use their answers as:
- **Session name slug** → used in the folder name, snapshot title, and MEMORY.md entry
- **Base path** → where the session folder will be created

Defaults if skipped:
- Name: `session`
- Path: `~/.claude/sessions/`

The full folder path will be: `[base-path]/YYYY-MM-DD-HHMM-[session-name]/`

### Step 2: Analyze the Conversation

Review the full conversation history and extract:

- **What was done**: Completed tasks, code written, files modified, problems solved
- **Current state**: Where things stand right now — open files, partial work, current branch, environment details
- **Next steps**: What still needs to be done, what to tackle first in the next session
- **Key findings & decisions**: Important discoveries, architectural choices, gotchas, warnings, unresolved questions

### Step 3: Build the Snapshot

Format the snapshot as structured markdown using the Output Format below.

Be specific and actionable — the goal is that someone (future-you) can paste this into a brand new Claude session and be fully oriented in under 30 seconds.

### Step 4: Save to Disk

Use **Bash** to create the session folder at the user-specified location:

```bash
mkdir -p [base-path]/YYYY-MM-DD-HHMM-[session-name]
```

Example: `mkdir -p ~/.claude/sessions/2026-02-27-1430-snapshot-skill-build`

Then use the **Write** tool to save the snapshot inside that folder:

```
[base-path]/YYYY-MM-DD-HHMM-[session-name]/snapshot.md
```

The folder is the named container — additional files (code snippets, references, exports) can be added to it in future sessions.

### Step 5: Update MEMORY.md

Use the **Edit** tool to prepend a compact session entry to `~/.claude/projects/-Users-victorcalauhia/memory/MEMORY.md`.

Add it under a `## Recent Sessions` section (create it if it doesn't exist, place it near the top after the main heading). Format:

```markdown
## Recent Sessions

- **YYYY-MM-DD HH:MM** `[session-name]` — [One-line summary of what was worked on] → `[base-path]/YYYY-MM-DD-HHMM-[session-name]/snapshot.md`
```

Keep only the 5 most recent session entries in MEMORY.md — remove older ones if needed.

### Step 6: Confirm

Output a brief confirmation to the user:
- Snapshot saved to (path)
- MEMORY.md updated
- How to use it: "Paste the snapshot content into your next Claude session to restore context"

---

## Output Format

```markdown
# Session Snapshot — [session-name] — YYYY-MM-DD HH:MM

## Context
**Working Directory**: [path]
**Project/Repo**: [name or description]
**Session Goal**: [What you were trying to accomplish overall]

---

## What Was Done

[Bullet list of completed work. Be specific — include file paths, function names, commands run, problems solved.]

-
-
-

---

## Current State

[Describe the current state of the work. What's in progress? What's partially complete? What's the last thing that happened?]

**Files modified:**
- `path/to/file` — [what changed]

**Environment:**
- Branch: [if applicable]
- Any running processes, pending installs, etc.

---

## Next Steps

[Ordered list of what to do next. The first item should be the most immediate action.]

1.
2.
3.

---

## Key Findings & Decisions

[Important discoveries, gotchas, architectural decisions, warnings. Things future-you MUST know.]

-
-

---

## How to Resume

Paste this snapshot into a new Claude session with:

> "I'm continuing a previous session. Here's my context: [paste snapshot]"

```

---

## Available Tools

- **Write**: Save the snapshot `.md` file to `~/.claude/sessions/`
- **Edit**: Update `MEMORY.md` with the session entry
- **Bash**: Create the sessions directory if needed (`mkdir -p ~/.claude/sessions`)
- **Read**: Re-read any files if needed for current state accuracy

## Best Practices

- Be concrete, not vague — "modified `src/auth/session.ts` line 42" not "worked on auth"
- If there are unresolved errors or blockers, call them out clearly in Next Steps
- The snapshot should be self-contained — no implicit knowledge assumed
- Keep it under ~100 lines total so it fits cleanly in a new chat context

---

**Remember:** The snapshot is for future-you. Write it as if you're handing off to someone who knows the project but wasn't in this conversation.
