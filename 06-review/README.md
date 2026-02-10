# 👀 Review Skill

Comprehensive code review that identifies bugs, security issues, performance problems, and improvement opportunities.

## Overview

The `/review` skill provides thorough code review by:
- Analyzing recent code changes
- Checking for bugs and logic errors
- Identifying security vulnerabilities
- Assessing performance implications
- Verifying error handling
- Rating code quality
- Providing actionable feedback

## Prerequisites

- **Recommended**: Code changes committed or staged
- **Optional**: Implementation plan for context

## Usage

### Basic Usage

```
/review
```

Reviews recent changes in the current repository.

### Review Specific File

```
/review src/auth.ts
```

### Review Specific Commit

```
/review HEAD~1
```

## What Gets Reviewed

### 1. Correctness ✅
- Logic errors
- Algorithm appropriateness
- Edge case handling
- Off-by-one errors
- Race conditions

### 2. Security 🔒
- SQL injection risks
- XSS vulnerabilities
- Authentication/authorization
- Input validation
- Hardcoded secrets
- OWASP Top 10

### 3. Performance ⚡
- Algorithm efficiency
- Database query optimization
- Memory usage
- Unnecessary computations
- Blocking operations

### 4. Error Handling 🛡️
- Proper error catching
- Clear error messages
- Resource cleanup
- Failure mode handling
- No silent failures

### 5. Code Quality 📝
- Readability
- Naming conventions
- Function size/complexity
- Code duplication
- Comments and documentation
- Project convention adherence

### 6. Testing 🧪
- Test coverage
- Edge case testing
- Test clarity
- Appropriate mocking
- Test maintainability

## Review Report Structure

```markdown
# Code Review Report

## Summary
Overall assessment and quality score

## 🔴 Critical Issues (Must Fix)
Security, bugs, blockers

## 🟡 Important Suggestions (Should Fix)
Best practices, performance, maintainability

## 🟢 Nice-to-Have (Optional)
Minor improvements, style

## ✅ Good Practices Found
Positive findings

## 📊 Detailed Analysis
Category-by-category breakdown

## 🎯 Recommended Actions
Prioritized action items
```

## Example Review

### Input
```
/review
```

### Output
```markdown
# Code Review Report

## Summary
Reviewed multi-language support implementation (4 files, 65 lines changed).
Solid implementation with minor suggestions for improvement.

**Quality Score**: 8/10
**Critical Issues**: 0
**Suggestions**: 2
**Files Reviewed**: 4

---

## 🔴 Critical Issues (Must Fix)

None found! 🎉

---

## 🟡 Important Suggestions (Should Fix)

### 1. Language Validation Missing - src/extension.ts:222
**Severity**: Important
**Category**: Error Handling

**Problem**: Language code from user not validated

**Fix**:
\`\`\`typescript
const SUPPORTED_LANGUAGES = ['en-US', 'es-ES', ...];
if (!SUPPORTED_LANGUAGES.includes(language)) {
  vscode.window.showErrorMessage('Unsupported language');
  return;
}
\`\`\`

**Why**: Prevent runtime errors from invalid codes

---

## ✅ Good Practices Found
- Backward compatible defaults
- Follows project conventions
- User-friendly interface
- Proper TypeScript types

---

## 🎯 Recommended Actions
1. Add language validation
2. Add unit tests for config methods
3. Run `/peer-review` for additional feedback
```

## Review Checklist

The skill checks:

- [ ] **Bugs**: Logic errors, edge cases, off-by-one
- [ ] **Security**: OWASP Top 10, injection, XSS, auth
- [ ] **Performance**: Algorithm efficiency, N+1 queries
- [ ] **Errors**: Proper handling, clear messages, cleanup
- [ ] **Quality**: Readability, naming, duplication
- [ ] **Tests**: Coverage, clarity, edge cases

## Tips for Better Reviews

### Do's ✅
- **Review full context**: Understand surrounding code
- **Check edge cases**: What breaks this code?
- **Be specific**: Include file paths and line numbers
- **Suggest fixes**: Provide concrete solutions
- **Explain why**: Help understand the reasoning
- **Acknowledge good work**: Balance criticism with praise

### Don'ts ❌
- **Don't nitpick**: Focus on important issues
- **Don't just criticize**: Offer solutions
- **Don't ignore positives**: Recognize good practices
- **Don't be vague**: "This looks bad" isn't helpful
- **Don't skip context**: Understand the intent first

## Workflow Integration

### Typical Flow

1. **Explore** → `/explore [feature]`
2. **Create Issue** → `/create-issue`
3. **Plan** → `/create-plan`
4. **Execute** → `/execute`
5. **Review** → `/review` ← **YOU ARE HERE**
6. **Peer Review** → `/peer-review` (optional)
7. **Document** → `/document`
8. **Commit** → `git commit`

## Common Issues Detected

### Security Issues
- SQL injection vulnerabilities
- XSS attack vectors
- Missing authentication checks
- Hardcoded credentials
- Insecure dependencies

### Bug Patterns
- Null pointer errors
- Off-by-one errors
- Race conditions
- Memory leaks
- Type mismatches

### Performance Problems
- N+1 query patterns
- Inefficient algorithms
- Memory bloat
- Blocking operations
- Missing database indexes

### Code Smells
- Functions >50 lines
- Nesting >3 levels
- Code duplication
- Magic numbers
- Poor naming

## Configuration

No configuration needed - works out of the box!

The skill automatically detects:
- Project language/framework
- Testing framework
- Code style conventions
- Security requirements

## Integration with Other Skills

### Before Review
- **`/execute`**: Implement the changes
- **`git diff`**: See what changed

### During Review
- **`Read`**: Read modified files
- **`Grep`**: Search for patterns
- **`Bash(git)`**: Check git history

### After Review
- **`/peer-review`**: Get multi-model feedback
- **`/document`**: Update documentation
- **`git commit`**: Commit fixes

## Example: Complete Review Workflow

```bash
# 1. Implement feature
/execute all

# 2. Review your work
/review

# 3. Fix issues found
[Make fixes based on review feedback]

# 4. Get additional perspective
/peer-review

# 5. Update documentation
/document

# 6. Commit
git add .
git commit -m "Add feature with review feedback addressed"
```

## Quality Scoring

**Score Breakdown:**
- **9-10**: Excellent - Production ready
- **7-8**: Good - Minor improvements needed
- **5-6**: Fair - Important issues to address
- **3-4**: Poor - Significant problems
- **1-2**: Critical - Major rework needed

## Related Skills

- **`/execute`**: What you review after implementation
- **`/peer-review`**: Multi-model review for additional perspective
- **`/document`**: Document after fixing review findings

## Version History

- **1.0.0** (2026-02-06): Initial release with comprehensive code review capabilities
