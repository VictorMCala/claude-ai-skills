# claude-ai-skills

Personal and workplace-specific Claude Code skills. These are context-specific utilities that complement the core development pipeline.

For the full AI-assisted development pipeline, see: **[claude-dev-pipeline-for-PMs](https://github.com/VictorMCala/claude-dev-pipeline-for-PMs)**

---

## Skills

### `/advisor`
Personal advisor skill integrated with WorkIQ for automatic M365 context queries. Useful for workplace intelligence — emails, meetings, documents, Teams messages, and organizational context.

### `/ms-fact-check`
Microsoft-specific fact-checking skill. Systematically verifies statements against Microsoft 365 documentation, meetings, ICMs, and repositories. Includes anti-bias mechanisms, source quality assessment, and balanced VERIFY/CONTRADICT/NEUTRAL analysis.

### `shared/`
Shared scripts and utilities used across skills (e.g., peer review orchestrator).

---

## Installation

```bash
# Clone this repo
git clone git@github.com:VictorMCala/claude-ai-skills.git

# Copy skills into Claude Code skills directory
cp -r claude-ai-skills/advisor ~/.claude/skills/
cp -r claude-ai-skills/ms-fact-check ~/.claude/skills/
```

---

## Related

- **[claude-dev-pipeline-for-PMs](https://github.com/VictorMCala/claude-dev-pipeline-for-PMs)** — The full development pipeline:
  `ceo-thinker → cto → parallel-builder → design → create-issue → explore → create-plan → execute → review → peer-review → document → learning-opportunity`
