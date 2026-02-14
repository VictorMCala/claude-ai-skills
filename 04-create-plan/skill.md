# Create Implementation Plan

Transform Linear issues or task descriptions into detailed, step-by-step implementation plans with **PRD (Project Requirements Document) files** that serve as living documentation.

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

3. **Generate PRD Files** (NEW - Documentation-Driven Development)
   - Create `masterplan.md` - High-level vision and goals
   - Create `implementation-plan.md` - Build order and sequence
   - Create `design-guidelines.md` - Visual design specs (CSS, fonts, spacing, colors)
   - Create `user-journey.md` - User flows and navigation
   - Create `tasks.md` - Executable task list
   - Create `rules.md` - Agent behavior rules

4. **Design the Approach**
   - Break down into logical steps
   - Order steps by dependencies
   - Identify potential risks or challenges
   - Consider edge cases and error handling
   - **Enforce task decomposition** (one focused task at a time)

5. **Create Detailed Plan**
   - Write clear, actionable steps
   - Specify exact files to modify
   - Include code structure guidance
   - Add validation/testing steps
   - **Break large tasks into small, focused chunks** (3 wishes rule)

## PRD Files Structure (Generate These First)

### 1. masterplan.md
```markdown
# Master Plan: [Project Name]

## Vision (One Sentence)
[Clear, specific description of what we're building]

## Why This Matters
[Core problem being solved]

## Who This Is For
[Specific target users, not vague "everyone"]

## Success Looks Like
[Measurable outcomes]

## Key Decisions
- [Decision 1 and why]
- [Decision 2 and why]

## References
- Design Guidelines: See design-guidelines.md
- Implementation Sequence: See implementation-plan.md
- User Flows: See user-journey.md
- Tasks: See tasks.md
```

### 2. implementation-plan.md
```markdown
# Implementation Plan: [Project Name]

## Build Order
1. **Phase 1: [Name]** - [Why first]
   - Component A
   - Component B

2. **Phase 2: [Name]** - [Why second]
   - Component C
   - Component D

## Dependencies
- [X must be built before Y because...]

## Integration Points
- [How this connects to existing code]

## Risks
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]
```

### 3. design-guidelines.md
```markdown
# Design Guidelines: [Project Name]

## Visual Style
**Fonts:**
- Primary: [Font family, size, weight]
- Secondary: [Font family, size, weight]

**Colors:**
- Primary: [Hex code]
- Secondary: [Hex code]
- Background: [Hex code]
- Text: [Hex code]

**Spacing:**
- Base unit: [e.g., 8px]
- Component padding: [e.g., 16px]
- Section margins: [e.g., 32px]

## Component Patterns
[Reference to existing patterns or design system]

## CSS Guidelines
```css
/* Key styles */
.primary-button {
  /* Specific styles */
}
```

## References
- Mobbin/Dribbble links: [URLs]
- Component library: [e.g., shadcn/ui]
```

### 4. user-journey.md
```markdown
# User Journey: [Project Name]

## Entry Points
- User lands on [page/screen]
- User action: [First action]

## Main Flow
1. User [action 1]
2. System [response 1]
3. User [action 2]
4. System [response 2]
5. Success state: [What user sees]

## Alternative Flows
- If [condition]: [Alternative path]
- Error state: [What user sees]

## Exit Points
- Success: [Where user ends up]
- Cancel: [What happens]
```

### 5. tasks.md
```markdown
# Tasks: [Project Name]

## Task Breakdown (Small, Focused Chunks)

### Task 1: [Specific Action]
- **File:** path/to/file.ts
- **Action:** [Exactly what to do]
- **Validation:** [How to verify]
- **Status:** [ ] Pending / [x] Done

### Task 2: [Specific Action]
[Same structure]

## Notes
- Each task should take < 30 minutes
- One focused change per task
- Read masterplan.md and design-guidelines.md before starting
```

### 6. rules.md
```markdown
# Agent Rules: [Project Name]

## Behavior Instructions
- Always read masterplan.md before making changes
- Always read tasks.md to see current task
- After completing task, mark it done in tasks.md
- One task at a time - no batching
- Report what was done and how to test it

## File Reading Priority
1. masterplan.md (vision)
2. design-guidelines.md (how it should look)
3. tasks.md (what to do next)
4. implementation-plan.md (context)

## Context Management
- If context window is > 70% full, suggest creating documentation
- Reference files by path, not full content
- Focus on current task only
```

---

## Implementation Plan Structure (After PRDs)

### 1. Overview
- **Objective**: [What we're building/fixing]
- **Approach**: [High-level strategy]
- **Estimated Complexity**: [S/M/L/XL]
- **PRD Files Generated**: ✅ All 6 files created

### 2. Prerequisites
- [ ] Exploration completed (if needed)
- [ ] Dependencies identified
- [ ] Architecture decisions made
- [ ] Acceptance criteria clear
- [x] PRD files generated (masterplan, implementation, design, journey, tasks, rules)

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

## Process (Documentation-Driven Approach)

### Step 1: Gather Context
   - Read Linear issue or task description
   - Review exploration results if referenced
   - Use WorkIQ for organizational context if needed
   - Read relevant files to understand current state

### Step 2: Generate PRD Files (CRITICAL)

**Why PRDs First?**
> "Context is more valuable than code. Documentation prevents token waste."

Generate all 6 PRD files:

1. **masterplan.md** - Ask ChatGPT or use your understanding to create high-level vision
2. **implementation-plan.md** - Based on exploration, outline build order
3. **design-guidelines.md** - Extract from design references (Mobbin/Dribbble links) or defaults
4. **user-journey.md** - Map out user flows from requirements
5. **tasks.md** - Break implementation into small, focused tasks (< 30 min each)
6. **rules.md** - Set agent behavior rules for this project

**Output these files in markdown code blocks** so they can be copy-pasted into project.

### Step 3: Analyze Architecture
   - Map out affected components
   - Identify dependencies
   - Find similar patterns in codebase
   - Consider integration points

### Step 4: Design Solution with Task Decomposition
   - Choose implementation approach
   - **Break into small, focused tasks** (3 wishes rule: each task should be focused enough that AI doesn't waste tokens)
   - Order by dependencies
   - Identify risks and mitigations
   - **Each task should be < 30 minutes of work**

### Step 5: Create Detailed Plan
   - Write specific, actionable steps
   - Include file paths and line numbers
   - Add code structure examples
   - Define validation criteria
   - **Ensure tasks reference PRD files for context**

### Step 6: Review and Refine
   - Check for completeness
   - Verify logical ordering
   - Ensure steps are clear and unambiguous
   - **Verify tasks are small enough** (no task should do > 3 things)
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

- **PRDs are mandatory**: Always generate all 6 PRD files - they prevent context loss
- **Be specific**: Vague steps lead to confusion during execution
- **Order matters**: Steps should follow logical dependencies
- **Task decomposition**: Break tasks into < 30 min focused chunks (3 wishes rule)
- **Include context**: Explain WHY, not just WHAT
- **Reference patterns**: Point to similar existing code
- **Reference PRDs**: Tasks should tell agent to read masterplan.md and design-guidelines.md
- **Consider testing**: Include validation at each step
- **Think ahead**: Anticipate potential issues

## The "Three Wishes" Rule (Task Decomposition)

**Analogy**: Like Aladdin's Genie, AI has limited "wishes" (token window) per request.

**Problem**: Large, vague tasks waste tokens:
- Agent reads entire codebase (80% of tokens)
- Little room left for thinking and executing (20% of tokens)
- Result: Poor quality output, needs rework

**Solution**: Small, focused tasks with context in PRDs:
- Agent reads ONLY relevant PRD files (20% of tokens)
- Most tokens available for execution (80% of tokens)
- Result: High quality output, first try

**How to decompose:**
- ❌ Bad: "Add authentication to the app" (too vague, too large)
- ✅ Good: "Add login form component to src/components/Auth/LoginForm.tsx following design-guidelines.md"

**Rule of thumb**: If a task would take > 30 minutes or touches > 3 files, break it down.

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
