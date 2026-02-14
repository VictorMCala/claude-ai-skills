# Claude Code Skills Repository

Custom skills for Claude Code tailored for Microsoft 365 Copilot and Work IQ development.

## 📁 Repository Structure

```
claude-skills/
├── ms-fact-check/          # Systematic fact-checking against documentation
│   ├── skill.md           # Main skill prompt
│   ├── metadata.json      # Skill configuration
│   └── README.md          # Usage documentation
└── README.md              # This file
```

## 🚀 Installation

These skills are designed to be symlinked into Claude Code's skills directory:

```bash
# Clone or pull this repo
cd ~/Documents/Development/work\ IQ/claude-skills/

# Create symlinks for each skill
ln -s "$(pwd)/ms-fact-check" ~/.claude/skills/ms-fact-check
```

## 📋 Skills Overview

Complete development workflow from idea to production, with AI-powered vibe coding techniques.

### Skills Reference Table

| # | Skill | Command | What It Does | Expected Outcome | Status |
|---|-------|---------|--------------|------------------|--------|
| **01** | **CTO** | `/cto` | Technical advisor for idea validation and planning. Forces clarity with "Genie metaphor", recommends parallel exploration, discovers design references | Product brief with specific requirements, tech recommendations, and clear next steps | ✅ **Updated** |
| **02** | **Create Issue** | `/create-issue` | Transforms findings into well-structured Linear issues | Linear issue with ID, URL, clear acceptance criteria | **Keep** |
| **03** | **Explore** | `/explore` | Analyzes codebase thoroughly before implementation | Exploration report with affected components, similar patterns, recommended approach | **Keep** |
| **04** | **Create Plan** | `/create-plan` | Creates implementation plan with **auto-generated PRD files** (masterplan, implementation, design, tasks, rules) and task decomposition | 6 PRD .md files + step-by-step implementation plan with small, focused tasks | ✅ **Updated** |
| **05** | **Execute** | `/execute` | Executes plans with **PRD-driven context**, strict one-task-at-a-time enforcement, and token monitoring | Code changes validated at each step, efficient token usage, high-quality output | ✅ **Updated** |
| **06** | **Review** | `/review` | Comprehensive code review for bugs, security, performance | Review report with quality score, critical issues, suggestions | **Keep** |
| **07** | **Peer Review** | `/peer-review` | Multi-model code review (Claude + GPT-4o) | Consensus findings, unique insights, prioritized actions from multiple AI perspectives | **Keep** |
| **08** | **Document** | `/document` | Generates/updates documentation (README, API docs, comments) | Updated documentation files ready to commit | **Keep** |
| **09** | **Learning** | `/learning-opportunity` | Extracts learnings from implementations, mistakes, successes | Learning report with insights, patterns, recommendations for continuous improvement | **Keep** |
| **10** | **Parallel Builder** | `/parallel-builder` | **NEW**: Launches 4-5 parallel builds (brain dump, structured, design-first, code-template), pick winner | Multiple project versions to compare, clear winner identified, 2-4 hours saved | 🆕 **New** |

### Workflow Progression

```
💡 Idea
  ↓
01: CTO (validate & refine) ← Clarity coaching + parallel exploration
  ↓
[Optional: 10: Parallel Builder] ← NEW: Try 4-5 approaches in parallel
  ↓
02: Create Issue (document in Linear)
  ↓
03: Explore (analyze codebase)
  ↓
04: Create Plan ← AUTO-GENERATES 6 PRD files + tasks
  ↓
05: Execute ← PRD-driven context + token monitoring
  ↓
06: Review (code quality)
  ↓
07: Peer Review (multi-model validation)
  ↓
08: Document (update docs)
  ↓
09: Learning (extract insights)
  ↓
🚀 Ship it!
```

---

## 🎯 Key Features (Phase 1 - Feb 2026)

### 1. Clarity First (Skill 01: CTO)
**The Genie Principle**: Forces specificity before building
- ❌ Vague: "I want an app to help people be productive"
- ✅ Specific: "Chrome extension that blocks social media 9-5, with whitelist and daily reports"

### 2. Parallel Exploration (Skill 10: Parallel Builder)
**Try 4-5 approaches before committing**:
1. Brain dump (quick, unstructured)
2. Structured (detailed requirements)
3. Design-first (Mobbin/Dribbble references)
4. Code template (21st.dev, shadcn)

**Time saved**: 30 min upfront vs 2-4 hours iteration

### 3. Documentation-Driven Development (Skill 04: Create Plan)
**Auto-generates 6 PRD files**:
- `masterplan.md` - Vision and goals
- `implementation-plan.md` - Build order
- `design-guidelines.md` - Fonts, colors, CSS
- `user-journey.md` - User flows
- `tasks.md` - Executable tasks
- `rules.md` - Agent behavior

**Why?** Living documentation prevents context loss and token waste

### 4. Token Efficiency (Skill 05: Execute)
**"Three Wishes" Rule**:
- Small, focused tasks (< 30 min each)
- Read PRDs for context (not entire codebase)
- One task at a time (strict)
- Token monitoring (warn at 70%, stop at 85%)

**Result**: 80% of tokens available for execution vs wasted on reading

---

## 📚 Detailed Skill Documentation

### 01: CTO - Technical Advisor
**Purpose**: Brainstorm, refine, and validate product ideas before implementation

**New Features (Phase 1)**:
- Phase 0: Clarity Coaching with "Genie metaphor"
- Parallel exploration recommendations
- Design reference discovery (Mobbin, Dribbble, 21st.dev)

**Usage**: `/cto`

**See**: [01-cto/skill.md](./01-cto/skill.md)

---

### 04: Create Plan - Implementation Planning
**Purpose**: Transform issues into detailed plans with auto-generated PRD files

**New Features (Phase 1)**:
- Auto-generates 6 PRD .md files
- Task decomposition enforcement (< 30 min tasks)
- "Three Wishes" rule for focused tasks

**Usage**: `/create-plan [issue-id]`

**See**: [04-create-plan/skill.md](./04-create-plan/skill.md)

---

### 05: Execute - Implementation
**Purpose**: Execute plans step-by-step with validation

**New Features (Phase 1)**:
- PRD-driven context (read PRDs before code)
- One-task-at-a-time enforcement
- Token usage monitoring
- Focus on agent reasoning

**Usage**: `/execute [step-number]` or `/execute all`

**See**: [05-execute/skill.md](./05-execute/skill.md)

---

### 10: Parallel Builder - NEW 🆕
**Purpose**: Launch 4-5 parallel project explorations, pick the winner

**Approaches**:
1. Brain dump (voice/quick)
2. Structured (detailed prompt)
3. Design-first (visual references)
4. Code template (existing patterns)

**Time**: ~30 min total (7-10 min per approach)

**Usage**: `/parallel-builder`

**See**: [10-parallel-builder/skill.md](./10-parallel-builder/skill.md)

---

### Microsoft Fact-Checker (`/ms-fact-check`) - v2.2.0

Systematically verifies statements and problems against Microsoft 365 documentation, meetings, ICMs, and repositories with anti-bias mechanisms.

**Usage:**
```bash
/ms-fact-check <statement or problem to verify>
```

**Key Features:**
- 🔗 **Prominent Source Links (v2.2)** - Top 3-5 most reliable sources with direct links upfront
- ⚖️ **Balanced Source Analysis (v2.1)** - Shows sources that VERIFY, CONTRADICT, and provide NEUTRAL context
- 🚫 **Anti-Bias Mechanisms** - Excludes internal team sources, prioritizes external validation
- 📊 **Source Quality Assessment** - 5-metric system: age, seniority, engagement, origin, confidence
- 🎯 **Prioritized Evidence** - External + Senior (Principal+) + Recent + High engagement first
- 📅 **Modification Date Filtering** - Checks when documents were last updated, not just created
- ✅ **Verification Status** - VERIFIED, PARTIALLY VERIFIED, NOT VERIFIED, NEEDS MORE INFO
- 📝 **Todo Tracking** - Progress tracking for each verification sub-claim
- 🔍 **Multi-Source Verification** - Queries ICMs, documents, meetings, ADO work items

**See:** [ms-fact-check/README.md](./ms-fact-check/README.md)

---

## 🛠️ Creating New Skills

### Skill Directory Structure

Each skill needs:
```
skill-name/
├── skill.md           # Required: Main prompt/instructions
├── metadata.json      # Required: Configuration
└── README.md          # Recommended: Documentation
```

### metadata.json Template

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "What the skill does",
  "author": "Your Name",
  "icon": "🔍",
  "trigger": {
    "type": "command",
    "pattern": "command-name"
  },
  "capabilities": ["capability1", "capability2"],
  "examples": [
    "/command-name example usage"
  ]
}
```

### skill.md Template

````markdown
# Skill Name

[Brief description of what the skill does]

## Your Process

When invoked:

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output Format

[Describe the expected output format]

## Available Tools

- **Tool 1**: Description
- **Tool 2**: Description

## Examples

[Provide examples]
````

---

## 🔗 Managing Symlinks

### Add a new skill to Claude Code:
```bash
ln -s "$(pwd)/new-skill" ~/.claude/skills/new-skill
```

### Remove a skill:
```bash
rm ~/.claude/skills/skill-name  # Only removes symlink, not the actual files
```

### List active skills:
```bash
ls -la ~/.claude/skills/
```

---

## 📦 Sharing with Team

### For teammates to install:

1. **Clone this repo** (or get access to shared location)
2. **Create symlinks** for desired skills:
   ```bash
   cd /path/to/claude-skills
   ln -s "$(pwd)/ms-fact-check" ~/.claude/skills/ms-fact-check
   ```
3. **Restart Claude Code** (if running) or skills auto-load on next invocation

---

## 🎯 Best Practices

1. **Version Control**: Commit changes to skills regularly
2. **Documentation**: Keep README.md updated for each skill
3. **Testing**: Test skills thoroughly before sharing
4. **Naming**: Use clear, descriptive command names
5. **Dependencies**: Document any required MCP servers or tools

---

## 📚 Resources

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Skill Development Guide](https://github.com/anthropics/claude-code/docs/skills)
- [MCP Servers](https://github.com/anthropics/claude-code/docs/mcp)

---

## 🤝 Contributing

To add a new skill to this repository:

1. Create a new directory under `claude-skills/`
2. Add required files (`skill.md`, `metadata.json`)
3. Document usage in skill's `README.md`
4. Update this main README
5. Commit and push changes

---

## 📝 Version History

### Phase 1: Vibe Coding Improvements (2026-02-14)
**Major Update**: Implemented AI-powered vibe coding techniques based on Lazar Jovanovic's professional practices

**Updated Skills**:
- **01-cto**: Added clarity coaching, parallel exploration, design references
- **04-create-plan**: Auto-generates 6 PRD files, enforces task decomposition
- **05-execute**: PRD-driven context, token monitoring, one-task enforcement

**New Skills**:
- **10-parallel-builder**: Launch 4-5 parallel approaches, pick winner

**Impact**:
- Forces clarity upfront (prevents building wrong thing)
- Living documentation (prevents context loss)
- 80% token efficiency improvement
- 2-4 hours saved per project

**Based on**: [Lenny's Newsletter podcast with Lazar Jovanovic](https://www.lennysnewsletter.com/p/the-rise-of-the-professional-vibe)

---

### Earlier Versions
- **2026-02-06 v2.2**: Added prominent source links in Key Evidence section (ms-fact-check)
- **2026-02-05 v2.1**: Added balanced source analysis - VERIFY/CONTRADICT/NEUTRAL categories (ms-fact-check)
- **2026-02-05 v2.0**: Enhanced with anti-bias mechanisms, source quality assessment, seniority detection, and recency filtering (ms-fact-check)
- **2026-02-05 v1.0**: Initial repository setup with ms-fact-check skill
