# 💡 Learning Opportunity Skill

Extract and document learnings from implementations, mistakes, and successes to continuously improve your development practice.

## Overview

The `/learning-opportunity` skill helps you learn by:
- Analyzing recent implementations
- Identifying what worked and what didn't
- Extracting reusable patterns
- Documenting mistakes and fixes
- Creating actionable recommendations
- Building a personal knowledge base

## Prerequisites

- Recent work to reflect on (implementation, review, etc.)
- Willingness to be honest about challenges

## Usage

### Basic Usage
```
/learning-opportunity
```

Extracts learnings from recent work.

### Specific Feature
```
/learning-opportunity from the authentication refactor
```

### After Complex Work
```
/execute all
/review
/learning-opportunity
```

## What Gets Extracted

### 1. Technical Learnings 🔧
- Library/API discoveries
- Performance insights
- Architecture decisions
- Implementation patterns

### 2. Process Learnings 📋
- What planning helped
- What slowed us down
- Tool effectiveness
- Communication insights

### 3. Mistakes & Fixes 🐛
- What went wrong
- How it was fixed
- Prevention strategies
- Warning signs

### 4. Successes & Patterns ✅
- What worked well
- Why it worked
- When to replicate
- Reusable patterns

## Learning Report Structure

```markdown
# Learning Opportunity Report

## Context
Feature, duration, complexity, date

## 🎓 Key Learnings
Technical and process insights

## ✅ What Worked Well
Successes to replicate

## ❌ What Didn't Work
Mistakes and fixes

## 🔍 Patterns Discovered
Positive patterns and anti-patterns

## 💡 Recommendations
For future similar work

## 🎯 Action Items
Personal growth and team improvements
```

## Example Report

```markdown
# Learning Opportunity Report

## Context
**Feature**: Multi-language support
**Duration**: 2 hours
**Complexity**: S (Small)

---

## 🎓 Key Learnings

### Azure SDK Language Configuration
Must re-initialize when changing language, can't update property dynamically.

\`\`\`typescript
await speechService.initialize(apiKey, region, newLanguage);
\`\`\`

---

## ✅ What Worked Well

### Following Existing Patterns
Used same pattern as region config = consistent, predictable code.

---

## ❌ What Didn't Work

### Forgot Input Validation
Accepted any string without validation → potential runtime errors.

**Prevention**: Always ask "what could go wrong?"

---

## 💡 Recommendations

1. Start with configuration schema first
2. Add validation for all user inputs
3. Follow existing code patterns
4. Test with invalid inputs

### Questions for Next Time
- [ ] What user inputs could break this?
- [ ] Does this follow existing patterns?
- [ ] Is there fallback behavior?
```

## When to Extract Learnings

### Always Extract For:
- ✅ First implementations
- ✅ Unexpected challenges
- ✅ Mistakes made
- ✅ Elegant solutions
- ✅ Significant features

### Consider For:
- 🤔 Routine work with insights
- 🤔 Process improvements
- 🤔 Team collaboration learnings

### Skip For:
- ❌ Trivial changes
- ❌ Exact repeats
- ❌ No new insights

## Benefits

### Personal Growth
- Learn from mistakes
- Identify patterns
- Build expertise faster
- Avoid repeating errors

### Team Value
- Share insights
- Document best practices
- Build team playbooks
- Improve processes

### Future Efficiency
- Faster similar work
- Better decisions
- Fewer mistakes
- More confidence

## Workflow Integration

```bash
# Complete workflow
/explore             # Understand
/create-issue        # Document
/create-plan         # Plan
/execute             # Implement
/review              # Review
/peer-review         # Deep review
/document            # Document
/learning-opportunity # Learn ← YOU ARE HERE
git commit           # Commit with confidence
```

## Storage Recommendations

### Personal Learnings
```
~/Documents/learnings/
  2026-02-06-multi-language-support.md
  2026-02-10-auth-refactor.md
```

### Project Learnings
```
project-root/docs/learnings/
  YYYY-MM-DD-feature-name.md
```

### Team Playbook
```
team-docs/
  patterns/
    configuration-best-practices.md
  anti-patterns/
    common-mistakes.md
```

## Tips for Effective Learning

### Do's ✅
- Write while fresh (right after work)
- Be specific with examples
- Note context (why it mattered)
- Make it actionable
- Be honest about mistakes
- Focus on patterns

### Don'ts ❌
- Don't be vague
- Don't skip the "why"
- Don't only note negatives
- Don't forget successes
- Don't write novels

## Learning Categories

### Technical
- APIs and libraries
- Performance patterns
- Architecture decisions
- Implementation techniques

### Process
- Planning effectiveness
- Tool usage
- Communication
- Time management

### Patterns
- Reusable solutions
- Anti-patterns to avoid
- Decision frameworks
- Code structures

### Soft Skills
- Problem-solving approaches
- Debugging strategies
- Communication patterns
- Collaboration insights

## Example: Complete Workflow

```bash
# 1. Build feature
/execute all

# 2. Review quality
/review

# 3. Fix issues
[make fixes]

# 4. Deep review
/peer-review

# 5. Document
/document

# 6. Extract learnings
/learning-opportunity

# 7. Commit
git commit -m "Add feature with full learnings documented"
```

## Action Items

Learning reports should include:

### Personal Growth
- [ ] Skills to develop
- [ ] Topics to research
- [ ] Practices to adopt

### Team/Project
- [ ] Patterns to share
- [ ] Documentation updates
- [ ] Process improvements

## Periodic Review

Review past learnings:
- **Weekly**: Recent learnings
- **Monthly**: Patterns across projects
- **Quarterly**: Major insights and growth

## Related Skills

- **`/execute`**: Creates experiences to learn from
- **`/review`**: Provides feedback to extract
- **`/peer-review`**: Offers diverse perspectives
- **`/document`**: Captures institutional knowledge

## Version History

- **1.0.0** (2026-02-06): Initial release with comprehensive learning extraction
