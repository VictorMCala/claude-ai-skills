# Snapshot

> Preserve your Claude session context before the memory runs out

## Overview

`/snapshot` generates a structured summary of your current Claude session and saves it to disk + auto-memory. Invoke it when Claude warns about context compression so you can seamlessly pick up where you left off in a new chat.

## Features

- **Structured summary** — What was done, current state, next steps, key findings
- **Saves to disk** — Timestamped `.md` file in `~/.claude/sessions/`
- **Updates MEMORY.md** — Auto-loaded in your next session with a link to the full snapshot
- **30-second resume** — New chat reads the snapshot and you're back in context immediately

## Usage

```bash
/snapshot
```

No arguments needed. Invoke it any time, but especially when you see Claude's context compression warning.

## Output

The skill produces:

- **Session file**: `~/.claude/sessions/YYYY-MM-DD-HHMM-session.md`
- **MEMORY.md entry**: Compact one-liner linking to the full file
- **4 structured sections**:
  - `## What Was Done` — completed work, files modified
  - `## Current State` — where things stand right now
  - `## Next Steps` — ordered list of what to do next
  - `## Key Findings & Decisions` — gotchas, decisions, discoveries

## How to Resume in a New Chat

After `/snapshot` runs, start your next Claude session with:

> "I'm continuing a previous session. Here's my context: [paste snapshot content]"

Or simply open Claude Code — the MEMORY.md entry will auto-load and Claude will know a session file exists.

## Installation

```bash
cd /Users/victorcalauhia/Documents/Development/claude-skills
ln -s "$(pwd)/11-snapshot" ~/.claude/skills/snapshot
```

## Version History

- **v1.0.0** (2026-02-27): Initial release

## License

MIT License - See [LICENSE](../LICENSE) file for details.
