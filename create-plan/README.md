# 📋 Create Plan Skill

Transform Linear issues or task descriptions into detailed, actionable implementation plans with step-by-step instructions.

## Overview

The `/create-plan` skill helps you create comprehensive implementation plans by:
- Breaking down complex tasks into manageable steps
- Identifying exact files and components to modify
- Ordering steps by dependencies
- Providing code structure guidance
- Including validation criteria and testing strategies
- Anticipating challenges and providing mitigations

## Prerequisites

- **Recommended**: Run `/explore` first to understand the codebase
- **Optional**: Have a Linear issue created with `/create-issue`
- **Optional**: Linear MCP server for fetching issue details
- **Optional**: WorkIQ MCP for organizational context

## Usage

### Basic Usage

```
/create-plan Add dark mode toggle to settings page
```

### From Linear Issue

```
/create-plan for Linear issue ENG-123
```

### With Exploration Reference

```
/explore How does theming work in this app?
[After exploration]
/create-plan Add dark mode based on exploration findings
```

## Plan Structure

Every plan includes:

1. **Overview**: Objective, approach, complexity estimate
2. **Prerequisites**: What needs to be done first
3. **Implementation Steps**: Detailed, ordered steps with:
   - Specific files to modify
   - What to change and why
   - Code structure examples
   - Validation criteria
4. **Testing Strategy**: Unit, integration, and manual tests
5. **Potential Challenges**: Risks and mitigations
6. **Rollback Plan**: How to undo if needed
7. **Next Steps**: How to proceed with `/execute`

## Complexity Estimates

- **S (Small)**: 1-2 files, <100 lines, simple changes
- **M (Medium)**: 3-5 files, 100-300 lines, moderate complexity
- **L (Large)**: 6-10 files, 300-800 lines, significant changes
- **XL (Extra Large)**: 10+ files, 800+ lines, major architecture changes

## Workflow Integration

### Typical Flow

1. **Explore** → `/explore [feature/area]`
2. **Create Issue** → `/create-issue [description]`
3. **Plan** → `/create-plan for issue ENG-123` ← **YOU ARE HERE**
4. **Execute** → `/execute Step 1` (implement the plan)
5. **Review** → `/review` and `/peer-review`
6. **Document** → `/document`

## Example Plan Output

### Input
```
/create-plan Add CSV export to user dashboard
```

### Output
```markdown
# Implementation Plan: Add CSV Export to User Dashboard

## 1. Overview
**Objective**: Enable users to export dashboard data as CSV
**Approach**: Add export button, create backend endpoint, generate CSV
**Estimated Complexity**: M (Medium)

## 2. Prerequisites
- [x] Exploration completed
- [ ] Export utility available (check src/utils/export.ts)
- [x] Acceptance criteria from ENG-456

## 3. Implementation Steps

### Step 1: Add Export Button to Dashboard
**Files to modify:**
- `src/components/Dashboard/DashboardHeader.tsx`
- `src/components/Dashboard/styles.module.css`

**What to do:**
1. Import ExportIcon
2. Add button with onClick handler
3. Add loading state
4. Style button consistently

**Code structure:**
\`\`\`typescript
const handleExport = async () => {
  setLoading(true);
  const data = await exportDashboard();
  downloadCSV(data);
  setLoading(false);
};
\`\`\`

**Validation:**
- [ ] Button appears correctly
- [ ] Loading state works
- [ ] Click triggers export

### Step 2: Create Export API Endpoint
[Additional steps...]

## 4. Testing Strategy
- Unit tests for CSV generation
- Integration tests for full flow
- Manual test: export and open CSV

## 5. Potential Challenges
1. **Challenge**: Large datasets may timeout
   - **Mitigation**: Add pagination or streaming

## 6. Rollback Plan
- Feature toggle to disable
- Monitor API endpoint errors

## 7. Next Steps
- [ ] Review plan
- [ ] `/execute Step 1` to begin implementation
- [ ] Continue with remaining steps
```

## Tips for Better Plans

- **Be specific**: Include exact file paths and line numbers
- **Show examples**: Provide code structure guidance
- **Explain why**: Don't just say what, explain reasoning
- **Order logically**: Dependencies first, integration last
- **Include validation**: How to verify each step works
- **Think ahead**: Anticipate problems and provide solutions

## Integration with Other Skills

### Before Planning
- **`/explore`**: Understand the codebase first
- **`/create-issue`**: Document what needs to be done

### After Planning
- **`/execute`**: Implement the plan step by step
- **`/review`**: Review implementation quality
- **`/peer-review`**: Get multi-model feedback
- **`/document`**: Update docs after completion

## Advanced Usage

### Planning from WorkIQ Context

```
/create-plan Implement the feature discussed in yesterday's team meeting
```

The skill will use WorkIQ MCP to find meeting context.

### Planning Complex Refactoring

```
/create-plan Refactor authentication system to use JWT instead of sessions
```

For complex tasks, the plan will include:
- Phased approach
- Backward compatibility considerations
- Migration strategy
- Risk mitigation

### Planning with Constraints

```
/create-plan Add search feature (must work offline, max 50ms response time)
```

The plan will consider and address the constraints explicitly.

## Troubleshooting

### Plan Too Vague
If the plan lacks detail:
- Run `/explore` first to gather more context
- Provide more specific requirements
- Reference similar existing features

### Steps Out of Order
If steps seem illogical:
- Skill considers dependencies automatically
- Trust the ordering or ask for clarification
- Dependencies explained in "Why this first" sections

### Missing Context
If plan needs more information:
- Skill will use AskUserQuestion to clarify
- Provide Linear issue number for automatic context
- Reference exploration results

## Configuration

No configuration needed - works out of the box!

Optional enhancements:
- Install Linear MCP for automatic issue fetching
- Install WorkIQ MCP for meeting context
- Run `/explore` before planning for better context

## Related Skills

- **`/explore`**: Understand before planning
- **`/create-issue`**: Document the task
- **`/execute`**: Implement the plan
- **`/review`**: Check the implementation
- **`/peer-review`**: Multi-model review

## Version History

- **1.0.0** (2026-02-06): Initial release with comprehensive planning capabilities
