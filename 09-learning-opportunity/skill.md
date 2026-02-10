# Learning Opportunity Extractor

Extract and document learnings from implementations, mistakes, and successes for continuous improvement.

## Your Responsibilities

1. **Analyze Recent Work**
   - Review what was implemented
   - Identify challenges faced
   - Note solutions found
   - Recognize patterns

2. **Extract Learnings**
   - What worked well?
   - What didn't work?
   - What would you do differently?
   - What patterns emerged?

3. **Document Insights**
   - Technical learnings
   - Process improvements
   - Anti-patterns to avoid
   - Best practices discovered

4. **Make Actionable**
   - Specific recommendations
   - Patterns to reuse
   - Pitfalls to avoid
   - Questions to ask next time

## Learning Categories

### 1. Technical Learnings 🔧
- Library/framework insights
- API discoveries
- Performance patterns
- Architecture decisions

### 2. Process Learnings 📋
- What planning helped?
- What slowed us down?
- Communication gaps
- Tool effectiveness

### 3. Mistakes & Fixes 🐛
- What went wrong?
- How was it fixed?
- How to prevent next time?
- Warning signs to watch for

### 4. Successes & Patterns ✅
- What worked well?
- Why did it work?
- How to replicate?
- When to use this pattern?

## Extraction Process

### Step 1: Review the Journey
```
1. Read git log / commit history
2. Review implementation plan
3. Check review feedback
4. Recall challenges faced
```

### Step 2: Identify Key Moments
```
1. Where did we struggle?
2. What surprised us?
3. What took longer than expected?
4. What was easier than expected?
```

### Step 3: Extract Insights
```
1. Technical: What did we learn about the tech?
2. Process: What would we do differently?
3. Patterns: What patterns emerged?
4. Anti-patterns: What should we avoid?
```

### Step 4: Make Actionable
```
1. Specific recommendations
2. Reusable patterns
3. Checklists for next time
4. Questions to ask upfront
```

## Available Tools

- **Bash(git)**: Review commit history
- **Read**: Read implementation plans, reviews
- **Grep**: Search for patterns in code
- **Write**: Create learning documents

## Output Format

```markdown
# Learning Opportunity Report

## Context
**Feature**: [What was implemented]
**Duration**: [How long it took]
**Complexity**: [S/M/L/XL]
**Date**: [When]

---

## 🎓 Key Learnings

### Technical Insights

#### 1. [Learning Title]
**Discovery**: [What we learned]

**Context**: [When/how we learned it]

**Impact**: [Why this matters]

**Application**: [When to use this knowledge]

**Example**:
```language
// Code example demonstrating the learning
```

---

### Process Insights

#### 1. [Process Learning]
**What Happened**: [Description]

**Why It Mattered**: [Impact]

**Next Time**: [What to do differently]

---

## ✅ What Worked Well

### 1. [Success]
**What**: [Description]

**Why It Worked**: [Reasons for success]

**When to Replicate**: [Similar scenarios]

---

## ❌ What Didn't Work

### 1. [Challenge or Mistake]
**What Happened**: [Description]

**Impact**: [How it affected the work]

**Root Cause**: [Why it happened]

**Fix**: [How we resolved it]

**Prevention**: [How to avoid next time]

---

## 🔍 Patterns Discovered

### Positive Patterns (Use These)
1. **[Pattern Name]**
   - When: [Context for using]
   - Why: [Benefits]
   - Example: [Code/process example]

### Anti-Patterns (Avoid These)
1. **[Anti-pattern Name]**
   - Problem: [What goes wrong]
   - Instead: [Better approach]
   - Warning Signs: [How to detect early]

---

## 💡 Recommendations

### For Similar Future Work
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

### Questions to Ask Next Time
- [ ] [Question 1]
- [ ] [Question 2]
- [ ] [Question 3]

### Checklist for Next Implementation
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

---

## 📚 Resources Found Helpful
- [Resource 1] - [Why it helped]
- [Resource 2] - [Why it helped]

---

## 🎯 Action Items

### Personal Growth
- [ ] Learn more about [topic]
- [ ] Practice [skill]
- [ ] Read [resource]

### Team/Project
- [ ] Update documentation with [learning]
- [ ] Add to team playbook: [pattern]
- [ ] Share with team: [insight]

---

## 📝 Notes for Future Self

[Any additional thoughts, context, or advice for future similar work]
```

## Example Learning Report

```markdown
# Learning Opportunity Report

## Context
**Feature**: Multi-language support for Hey Tito
**Duration**: 2 hours
**Complexity**: S (Small)
**Date**: 2026-02-06

---

## 🎓 Key Learnings

### Technical Insights

#### 1. Azure Speech SDK Language Configuration
**Discovery**: The Azure Speech SDK accepts BCP-47 language codes and the parameter must be set during initialization.

**Context**: Initially tried to change language dynamically but found it requires re-initialization.

**Impact**: Need to re-initialize the speech service when language changes, not just update a property.

**Application**: Any feature that changes Azure SDK configuration at runtime.

**Example**:
\`\`\`typescript
// Must re-initialize, can't just update property
await speechService.initialize(apiKey, region, newLanguage);
\`\`\`

#### 2. VS Code Configuration Persistence
**Discovery**: vscode.workspace.getConfiguration() automatically handles persistence to settings.json when using ConfigurationTarget.Global.

**Context**: Was planning to manually write to settings file, but the API handles it.

**Impact**: Simpler code, less error-prone.

**Application**: Any VS Code extension configuration.

---

### Process Insights

#### 1. Start with Schema, Then Implementation
**What Happened**: Added configuration schema to package.json first, then implemented the code.

**Why It Mattered**: This ensured VS Code settings UI was available immediately and helped catch naming issues early.

**Next Time**: Always start with schema/types/interfaces before implementation.

---

## ✅ What Worked Well

### 1. Following Existing Patterns
**What**: Used the same pattern as region configuration for language configuration.

**Why It Worked**: Consistency made code predictable and easy to review.

**When to Replicate**: Any time adding configuration to an existing system.

---

## ❌ What Didn't Work

### 1. Forgot Language Validation
**What Happened**: Initial implementation accepted any string as language code without validation.

**Impact**: Could cause runtime errors with invalid language codes.

**Root Cause**: Focused on happy path, didn't think about edge cases.

**Fix**: Added validation in config getter and setup command.

**Prevention**: Always ask "what could go wrong?" during implementation.

---

## 🔍 Patterns Discovered

### Positive Patterns (Use These)
1. **Configuration Getters with Defaults**
   - When: Reading configuration values
   - Why: Prevents undefined errors, provides fallback
   - Example: `config.get<string>('language', 'en-US')`

### Anti-Patterns (Avoid These)
1. **Accepting User Input Without Validation**
   - Problem: Runtime errors, confusing failures
   - Instead: Validate at entry point with clear errors
   - Warning Signs: Any user-provided string used in API calls

---

## 💡 Recommendations

### For Similar Future Work
1. Start with configuration schema in package.json
2. Add validation for all user inputs
3. Follow existing code patterns for consistency
4. Test with invalid inputs, not just happy path

### Questions to Ask Next Time
- [ ] What could the user enter that would break this?
- [ ] Does this follow existing patterns in the codebase?
- [ ] Is there fallback behavior for errors?

### Checklist for Next Configuration Feature
- [ ] Add to package.json schema first
- [ ] Implement getter with default value
- [ ] Implement setter with validation
- [ ] Update setup command to include new config
- [ ] Test with invalid inputs
- [ ] Update documentation

---

## 📚 Resources Found Helpful
- Azure Speech SDK docs - Clear BCP-47 language code examples
- VS Code extension API docs - Configuration Target explained well

---

## 🎯 Action Items

### Personal Growth
- [ ] Learn more about BCP-47 language codes and i18n standards
- [x] Practice defensive programming (validation at boundaries)

### Team/Project
- [ ] Add language validation pattern to team coding guidelines
- [ ] Document the "schema first" approach in CONTRIBUTING.md

---

## 📝 Notes for Future Self

Small features like this are great for following existing patterns exactly. Don't reinvent - look for similar code and follow the same approach. The 5 minutes spent finding the pattern saves 30 minutes of debugging and review feedback.

Always validate user input, even from controlled sources like dropdowns (settings can be manually edited!).
```

## Integration with Other Skills

- **After `/execute`**: Extract learnings from implementation
- **After `/review`**: Learn from review feedback
- **After `/peer-review`**: Learn from model insights
- **Periodically**: Review past learnings to improve

## When to Extract Learnings

### Always Extract For:
- ✅ First time implementing something
- ✅ Unexpected challenges
- ✅ Mistakes made
- ✅ Elegant solutions found
- ✅ Significant features

### Consider Extracting For:
- 🤔 Routine work with new insights
- 🤔 Process improvements discovered
- 🤔 Team collaboration learnings

### Don't Need For:
- ❌ Trivial changes (typos, formatting)
- ❌ Exact repeat of previous work
- ❌ No new insights

## Best Practices

### Do's ✅
- Be specific and concrete
- Include code examples
- Note context (why it mattered)
- Make it actionable
- Be honest about mistakes
- Focus on patterns, not just facts

### Don'ts ❌
- Don't be vague ("it was hard")
- Don't skip the "why"
- Don't only note negatives
- Don't forget successes
- Don't write novels (be concise)

## Tips for Effective Learning Extraction

1. **Do It While Fresh**: Extract right after work, not days later
2. **Be Honest**: Mistakes are learning opportunities
3. **Think Forward**: How will this help next time?
4. **Share Insights**: Some learnings help the whole team
5. **Review Periodically**: Past learnings improve future work
6. **Update as You Learn**: Revise if you learn more later

## Storage

Save learning reports in:
```
project-root/
  docs/
    learnings/
      2026-02-06-multi-language-support.md
      2026-02-10-authentication-refactor.md
```

Or in your personal notes for cross-project learnings.

## Next Steps After Extraction

1. **Share relevant learnings** with team
2. **Update documentation** with discovered patterns
3. **Add to team playbook** if applicable
4. **Create follow-up tasks** for action items
5. **Review before similar work** in future

## Related Skills

- **`/execute`**: Generates experiences to learn from
- **`/review`**: Provides feedback to learn from
- **`/peer-review`**: Offers multiple perspectives
- **`/document`**: Captures learnings in docs
