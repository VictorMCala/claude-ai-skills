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

### 1. Fact-Checker (`/ms-fact-check`)

Systematically verifies statements and problems against Microsoft 365 documentation, meetings, ICMs, and repositories.

**Usage:**
```bash
/ms-fact-check <statement or problem to verify>
```

**Features:**
- ✅ Queries WorkIQ for evidence (ICMs, docs, meetings, ADO)
- ✅ Tracks verification progress with todos
- ✅ Classifies results: VERIFIED, PARTIALLY VERIFIED, NOT VERIFIED
- ✅ Provides sources and documentation links
- ✅ Generates architectural recommendations

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

- **2026-02-05**: Initial repository setup with ms-fact-check skill
- **2026-02-05 v2.0**: Enhanced with anti-bias mechanisms, source quality assessment, seniority detection, and recency filtering
