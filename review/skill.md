# Code Review

Perform comprehensive code review on recent changes, identifying bugs, issues, and improvements.

## Your Responsibilities

1. **Identify What Changed**
   - Read recent commits or modified files
   - Understand the scope of changes
   - Focus review on changed code

2. **Analyze Code Quality**
   - Check for bugs and logic errors
   - Verify error handling
   - Assess security issues
   - Review performance concerns
   - Check edge cases

3. **Provide Actionable Feedback**
   - Be specific about issues
   - Suggest concrete fixes
   - Prioritize critical vs nice-to-have
   - Explain the "why" behind feedback

4. **Rate and Summarize**
   - Overall quality score
   - Critical issues (must fix)
   - Suggestions (should fix)
   - Praise (what's good)

## Review Checklist

### 1. Correctness ✅
- [ ] Logic is correct
- [ ] Algorithm is appropriate
- [ ] No off-by-one errors
- [ ] Handles edge cases
- [ ] No race conditions

### 2. Error Handling 🛡️
- [ ] Errors are caught appropriately
- [ ] Error messages are clear
- [ ] Failure modes handled
- [ ] Resources cleaned up
- [ ] No silent failures

### 3. Security 🔒
- [ ] No SQL injection risks
- [ ] No XSS vulnerabilities
- [ ] Input validation present
- [ ] Authentication/authorization correct
- [ ] No hardcoded secrets
- [ ] No sensitive data in logs

### 4. Performance ⚡
- [ ] No obvious performance issues
- [ ] Efficient algorithms used
- [ ] No unnecessary loops
- [ ] Database queries optimized
- [ ] Memory usage reasonable

### 5. Code Quality 📝
- [ ] Code is readable
- [ ] Names are descriptive
- [ ] Functions are focused
- [ ] No code duplication
- [ ] Comments where needed
- [ ] Follows project conventions

### 6. Testing 🧪
- [ ] Tests are present
- [ ] Tests cover edge cases
- [ ] Test names are clear
- [ ] Mocks used appropriately
- [ ] Tests are maintainable

## Review Process

### Step 1: Understand Changes
```
1. Use git diff or git log to see what changed
2. Read the implementation plan if available
3. Identify affected files and components
4. Understand the intent of changes
```

### Step 2: Read Changed Code
```
1. Read each modified file completely
2. Focus on changed sections
3. Understand context around changes
4. Check how changes integrate with existing code
```

### Step 3: Analyze for Issues
```
1. Check against review checklist
2. Look for common anti-patterns
3. Verify edge cases handled
4. Check error handling paths
5. Assess security implications
```

### Step 4: Provide Feedback
```
1. Categorize issues (critical/important/nice-to-have)
2. Be specific with file paths and line numbers
3. Suggest concrete fixes
4. Explain reasoning
5. Acknowledge good practices
```

## Available Tools

- **Bash(git)**: See what changed (`git diff`, `git log`)
- **Read**: Read modified files
- **Grep**: Search for patterns (e.g., TODO, FIXME, security issues)
- **Glob**: Find all files of certain type

## Output Format

```markdown
# Code Review Report

## Summary
[Brief overview of changes and overall assessment]

**Quality Score**: X/10
**Critical Issues**: X
**Suggestions**: X
**Files Reviewed**: X

---

## 🔴 Critical Issues (Must Fix)

### 1. [Issue Title] - `file/path.ts:42`
**Severity**: Critical
**Category**: Security / Bug / Performance

**Problem**:
[Clear description of the issue]

**Impact**:
[What could go wrong]

**Fix**:
```language
// Suggested fix
```

**Why**:
[Explanation of why this is important]

---

### 2. [Next issue...]

---

## 🟡 Important Suggestions (Should Fix)

### 1. [Suggestion Title] - `file/path.ts:100`
**Severity**: Important
**Category**: Code Quality / Performance / Best Practice

**Current**:
```language
// Current code
```

**Suggested**:
```language
// Better approach
```

**Why**:
[Reasoning]

---

## 🟢 Nice-to-Have (Optional)

- Minor refactoring opportunities
- Style improvements
- Additional test cases

---

## ✅ Good Practices Found

- [List positive findings]
- What was done well
- Patterns to continue

---

## 📊 Detailed Analysis

### Correctness
[Analysis of logic correctness]

### Error Handling
[Analysis of error handling]

### Security
[Security assessment]

### Performance
[Performance considerations]

### Code Quality
[Readability and maintainability]

### Testing
[Test coverage and quality]

---

## 🎯 Recommended Actions

1. [Priority 1 action]
2. [Priority 2 action]
3. [Priority 3 action]

---

## Next Steps

- Fix critical issues
- Address important suggestions
- Run `/peer-review` for additional perspective
- Commit fixes
```

## Important Notes

- **Be constructive**: Focus on helping, not criticizing
- **Be specific**: Always include file paths and line numbers
- **Be actionable**: Provide concrete suggestions
- **Be balanced**: Acknowledge good practices too
- **Prioritize**: Not all issues are equal
- **Explain**: Help developer understand the "why"

## Common Issues to Check

### Security
- SQL injection (use parameterized queries)
- XSS (sanitize user input)
- CSRF (use tokens)
- Authentication bypass
- Authorization issues
- Secrets in code
- Insecure dependencies

### Bugs
- Null/undefined errors
- Off-by-one errors
- Race conditions
- Memory leaks
- Infinite loops
- Type mismatches
- Logic errors

### Performance
- N+1 query problems
- Unnecessary loops
- Large objects in memory
- Blocking operations
- Inefficient algorithms
- Missing indexes
- Excessive API calls

### Code Quality
- Long functions (>50 lines)
- Deep nesting (>3 levels)
- Magic numbers
- Code duplication
- Poor naming
- Missing error handling
- No input validation

## Example Review

```markdown
# Code Review Report

## Summary
Reviewed implementation of multi-language support for Hey Tito extension. Changes add language configuration and integrate with Azure Speech SDK. Overall solid implementation with a few suggestions for improvement.

**Quality Score**: 8/10
**Critical Issues**: 0
**Suggestions**: 2
**Files Reviewed**: 4

---

## 🔴 Critical Issues (Must Fix)

None found! 🎉

---

## 🟡 Important Suggestions (Should Fix)

### 1. Language Validation Missing - `src/extension.ts:222`
**Severity**: Important
**Category**: Error Handling

**Problem**:
Language code from user is not validated before being saved and used.

**Impact**:
Invalid language codes could cause Azure SDK to fail at runtime.

**Fix**:
```typescript
const SUPPORTED_LANGUAGES = ['en-US', 'es-ES', 'fr-FR', ...];

if (!SUPPORTED_LANGUAGES.includes(language)) {
  vscode.window.showErrorMessage('Unsupported language selected');
  return;
}
```

**Why**:
Fail fast with clear error message rather than cryptic Azure SDK error.

---

### 2. No Fallback for Missing Language Setting - `src/config.ts:25`
**Severity**: Important
**Category**: Best Practice

**Current**:
```typescript
static getLanguage(): string {
  const config = vscode.workspace.getConfiguration(this.CONFIG_SECTION);
  return config.get<string>('language', 'en-US');
}
```

**Suggested**:
Add explicit validation:
```typescript
static getLanguage(): string {
  const config = vscode.workspace.getConfiguration(this.CONFIG_SECTION);
  const language = config.get<string>('language', 'en-US');

  // Validate language code format (BCP-47)
  if (!/^[a-z]{2}-[A-Z]{2}$/.test(language)) {
    console.warn(`Invalid language code: ${language}, defaulting to en-US`);
    return 'en-US';
  }

  return language;
}
```

**Why**:
Protects against corrupted settings or manual editing errors.

---

## 🟢 Nice-to-Have (Optional)

- Add JSDoc comments to new methods
- Extract language options array to constant
- Add unit tests for config methods

---

## ✅ Good Practices Found

- ✅ Backward compatible (defaults to en-US)
- ✅ Follows existing code patterns
- ✅ User-friendly language labels
- ✅ Proper TypeScript types used
- ✅ Configuration properly persisted

---

## 📊 Detailed Analysis

### Correctness ✅
Logic is sound. Language parameter flows correctly through the system.

### Error Handling ⚠️
Missing validation for invalid language codes (see suggestions above).

### Security ✅
No security concerns. User input (language selection) is from controlled dropdown.

### Performance ✅
No performance issues. Configuration access is efficient.

### Code Quality ✅
Clean, readable code following project conventions.

### Testing ⚠️
No tests added. Consider adding tests for:
- Config get/set methods
- Language parameter flow through initialize()

---

## 🎯 Recommended Actions

1. Add language code validation in setup command
2. Add fallback validation in getLanguage()
3. (Optional) Add unit tests for config methods

---

## Next Steps

- Address the 2 suggestions above
- Run `/peer-review` for additional feedback
- Test with multiple languages
- Commit fixes
```

## Integration with Other Skills

- **After `/execute`**: Review what was implemented
- **Before committing**: Ensure quality
- **With `/peer-review`**: Get multi-model perspective
- **Before `/document`**: Fix issues first

## Tips for Good Reviews

1. **Read the whole diff**: Don't spot-check
2. **Understand intent**: Know what the code is trying to do
3. **Check edge cases**: What could go wrong?
4. **Be thorough but practical**: Don't nitpick
5. **Provide context**: Explain the "why"
6. **Balance criticism with praise**: Acknowledge good work
7. **Focus on impact**: Prioritize important issues

## Next Steps After Review

1. **Fix critical issues** immediately
2. **Address suggestions** when possible
3. **Run `/peer-review`** for additional perspective
4. **Update tests** based on feedback
5. **Document changes** with `/document`
6. **Commit** with descriptive message
