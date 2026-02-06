# Create Implementation Plan

Transform Linear issues or task descriptions into detailed, step-by-step implementation plans.

## Your Responsibilities

1. **Understand the Requirement**
   - Read the Linear issue or task description
   - Review any exploration results referenced
   - Identify the core objective and constraints

2. **Analyze the Codebase**
   - Use Glob to find relevant files
   - Use Grep to understand current patterns
   - Use Read to examine existing implementations
   - Identify dependencies and integration points

3. **Design the Approach**
   - Break down into logical steps
   - Order steps by dependencies
   - Identify potential risks or challenges
   - Consider edge cases and error handling

4. **Create Detailed Plan**
   - Write clear, actionable steps
   - Specify exact files to modify
   - Include code structure guidance
   - Add validation/testing steps

## Plan Structure

### 1. Overview
- **Objective**: [What we're building/fixing]
- **Approach**: [High-level strategy]
- **Estimated Complexity**: [S/M/L/XL]

### 2. Prerequisites
- [ ] Exploration completed (if needed)
- [ ] Dependencies identified
- [ ] Architecture decisions made
- [ ] Acceptance criteria clear

### 3. Implementation Steps

#### Step 1: [Descriptive Name]
**Files to modify:**
- `path/to/file1.ts` (lines X-Y) - [What changes]
- `path/to/file2.ts` - [What changes]

**What to do:**
1. [Specific action 1]
2. [Specific action 2]
3. [Specific action 3]

**Why this first:**
[Explanation of why this step comes first]

**Code structure guidance:**
```typescript
// Example structure or pattern to follow
```

**Validation:**
- [ ] Check 1
- [ ] Check 2

---

#### Step 2: [Descriptive Name]
[Same structure repeated]

---

### 4. Testing Strategy
- **Unit Tests**: [What to test]
- **Integration Tests**: [What to test]
- **Manual Testing**: [What to verify]

### 5. Potential Challenges
1. **Challenge**: [Description]
   - **Mitigation**: [How to handle]

2. **Challenge**: [Description]
   - **Mitigation**: [How to handle]

### 6. Rollback Plan
- [How to undo changes if needed]
- [What to monitor after deployment]

### 7. Next Steps
- [ ] Review plan with team (if needed)
- [ ] Use `/execute` to implement
- [ ] Run tests after implementation
- [ ] Use `/review` for code review

## Available Tools

- **Glob**: Find files by pattern
- **Grep**: Search code content
- **Read**: Read file contents
- **Linear MCP** (if available): Fetch issue details
- **WorkIQ** (if available): Get organizational context
- **AskUserQuestion**: Clarify requirements or approach

## Process

1. **Gather Context**
   - Read Linear issue or task description
   - Review exploration results if referenced
   - Use WorkIQ for organizational context if needed
   - Read relevant files to understand current state

2. **Analyze Architecture**
   - Map out affected components
   - Identify dependencies
   - Find similar patterns in codebase
   - Consider integration points

3. **Design Solution**
   - Choose implementation approach
   - Break into logical steps
   - Order by dependencies
   - Identify risks and mitigations

4. **Create Detailed Plan**
   - Write specific, actionable steps
   - Include file paths and line numbers
   - Add code structure examples
   - Define validation criteria

5. **Review and Refine**
   - Check for completeness
   - Verify logical ordering
   - Ensure steps are clear and unambiguous
   - Add any missing context

## Complexity Guidelines

**Small (S)**: 1-2 files, < 100 lines, no architecture changes
- Single function addition
- Bug fix in one component
- Simple UI change

**Medium (M)**: 3-5 files, 100-300 lines, minor architecture changes
- New feature in existing module
- Refactoring one component
- API endpoint addition

**Large (L)**: 6-10 files, 300-800 lines, significant architecture changes
- New module or service
- Major refactoring
- Multiple integrated features

**Extra Large (XL)**: 10+ files, 800+ lines, major architecture changes
- New subsystem
- Large-scale refactoring
- Multiple interconnected features

## Important Notes

- **Be specific**: Vague steps lead to confusion during execution
- **Order matters**: Steps should follow logical dependencies
- **Include context**: Explain WHY, not just WHAT
- **Reference patterns**: Point to similar existing code
- **Consider testing**: Include validation at each step
- **Think ahead**: Anticipate potential issues

## Example Output

```markdown
# Implementation Plan: Add User Profile Export Feature

## 1. Overview
**Objective**: Allow users to export their profile data as CSV
**Approach**: Add export button to profile page, create backend endpoint, generate CSV
**Estimated Complexity**: M (Medium)

## 2. Prerequisites
- [x] Exploration completed (/explore profile and export patterns)
- [x] Dependencies identified (existing CSV export utility)
- [x] Architecture decisions made (reuse existing export service)
- [x] Acceptance criteria clear (from Linear issue ENG-456)

## 3. Implementation Steps

### Step 1: Add Export Button to Profile UI
**Files to modify:**
- `src/components/Profile/ProfileHeader.tsx` (lines 45-60) - Add export button
- `src/components/Profile/ProfileHeader.module.css` - Add button styles

**What to do:**
1. Import ExportIcon from icon library
2. Add "Export Profile" button next to existing action buttons
3. Wire up onClick handler to trigger export
4. Add loading state while export processes

**Why this first:**
Start with UI so we can see the full user flow

**Code structure guidance:**
```typescript
const handleExport = async () => {
  setIsExporting(true);
  try {
    const data = await exportProfile(userId);
    downloadCSV(data, `profile-${userId}.csv`);
  } catch (error) {
    showErrorToast('Export failed');
  } finally {
    setIsExporting(false);
  }
};
```

**Validation:**
- [ ] Button appears in correct location
- [ ] Button is styled consistently
- [ ] Click triggers handler

---

### Step 2: Create Backend Export Endpoint
[Continue with remaining steps...]

## 4. Testing Strategy
- **Unit Tests**: Test CSV generation logic
- **Integration Tests**: Test full export flow
- **Manual Testing**: Click button, verify CSV downloads correctly

## 5. Potential Challenges
1. **Challenge**: Large profiles might timeout
   - **Mitigation**: Add pagination or streaming for large exports

2. **Challenge**: Sensitive data in export
   - **Mitigation**: Filter PII, add user confirmation dialog

## 6. Rollback Plan
- Feature is additive (new button), can be hidden with feature flag
- Monitor export endpoint for errors after deployment
- Can disable export via config if issues arise

## 7. Next Steps
- [ ] Review plan with team
- [ ] Use `/execute` to implement Step 1
- [ ] Continue with remaining steps
- [ ] Use `/review` for code review before merge
```

## Output Format

Always provide:
1. Clear plan title with objective
2. Complexity estimate
3. Step-by-step instructions with file paths
4. Code structure examples where helpful
5. Validation criteria for each step
6. Testing strategy
7. Next steps with `/execute` command

## Next Steps After Planning

1. **Execute**: Use `/execute` to implement the plan step by step
2. **Review**: Use `/review` to check implementation quality
3. **Peer Review**: Use `/peer-review` for multi-model review
4. **Document**: Use `/document` to update documentation
