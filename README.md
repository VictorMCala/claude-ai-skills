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

## 📋 Available Skills

### 1. Microsoft Fact-Checker (`/ms-fact-check`) - v2.2.0

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

- **2026-02-06 v2.2**: Added prominent source links in Key Evidence section (ms-fact-check)
- **2026-02-05 v2.1**: Added balanced source analysis - VERIFY/CONTRADICT/NEUTRAL categories (ms-fact-check)
- **2026-02-05 v2.0**: Enhanced with anti-bias mechanisms, source quality assessment, seniority detection, and recency filtering (ms-fact-check)
- **2026-02-05 v1.0**: Initial repository setup with ms-fact-check skill
