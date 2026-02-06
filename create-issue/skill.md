# Create Linear Issue

Transform exploration findings, bugs, or feature requests into well-structured Linear issues.

## Your Responsibilities

1. **Gather Information**
   - Understand the issue/feature being described
   - Reference any exploration results if provided
   - Identify the issue type (bug, feature, improvement, tech debt)

2. **Structure the Issue**
   - Write a clear, concise title (50-70 characters)
   - Create a comprehensive description with sections
   - Add relevant labels/tags
   - Set appropriate priority
   - Identify the team/project

3. **Create in Linear**
   - Use Linear MCP to create the issue
   - Return the issue URL and ID
   - Confirm successful creation

## Issue Structure

### Title Format
- **Bug**: "Fix: [Brief description of the problem]"
- **Feature**: "Add: [What is being added]"
- **Improvement**: "Improve: [What is being enhanced]"
- **Tech Debt**: "Refactor: [What needs refactoring]"

### Description Template

```markdown
## Problem Statement
[Clear description of the issue or need]

## Context
[Relevant background, exploration findings, or user impact]

## Current Behavior (for bugs)
[What happens now]

## Expected Behavior
[What should happen]

## Affected Components
- `path/to/file1.ts` - [Brief description]
- `path/to/file2.ts` - [Brief description]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Notes
[Implementation hints, constraints, or dependencies]

## Related
- Exploration: [Link if from /explore]
- PRs: [Related pull requests]
- Issues: [Related issues]
```

## Priority Guidelines

**Urgent** (P0):
- Production is broken
- Security vulnerability
- Data loss risk
- Complete blocker

**High** (P1):
- Major feature broken
- Significant user impact
- Blocking other work
- Time-sensitive

**Medium** (P2):
- Normal feature request
- Non-blocking bugs
- Planned improvements
- Standard tech debt

**Low** (P3):
- Nice-to-have
- Minor polish
- Future considerations
- Optional enhancements

## Available Tools

- **Linear MCP**: Create and manage issues
  - Note: User needs to have Linear MCP server installed and configured
  - If not available, provide the formatted issue for manual creation
- **Read**: Get exploration results from files
- **AskUserQuestion**: Clarify priority, team, or requirements

## Process

1. **Analyze Input**
   - Read any exploration results mentioned
   - Identify issue type
   - Gather all relevant context

2. **Ask Clarifying Questions** (if needed)
   - Which team/project?
   - What priority?
   - Any specific assignee?
   - Any additional context?

3. **Format Issue**
   - Create clear title
   - Structure description with all sections
   - Ensure acceptance criteria are specific and testable

4. **Create in Linear**
   - Use Linear MCP to create the issue
   - Handle any errors gracefully
   - Provide fallback formatted text if MCP unavailable

5. **Confirm Creation**
   - Return Linear issue URL
   - Return issue ID for reference
   - Summarize what was created

## Example Usage

**User**: "Create an issue for the authentication bug we found"

**Assistant Response**:
```
I'll create a Linear issue for the authentication bug. Let me gather some information first.

[Reads any exploration results if referenced]

Creating Linear issue...

✅ Issue Created: ENG-456

**Title**: Fix: Authentication token expires prematurely

**Priority**: P1 (High)
**Labels**: bug, authentication, backend

**URL**: https://linear.app/team/issue/ENG-456

**Description Summary**:
- Problem: Users getting logged out after 5 minutes
- Expected: Sessions should last 30 minutes
- Affected: src/auth/session.ts, src/middleware/auth.ts
- Acceptance Criteria: 3 testable conditions defined
- Technical notes: Check SESSION_TIMEOUT environment variable

Next step: Use /create-plan to plan the implementation
```

## Output Format

When creating an issue, always provide:

1. ✅ Confirmation message
2. Issue ID (e.g., ENG-456)
3. Issue title
4. Priority and labels
5. Linear URL (clickable link)
6. Brief summary of what was included
7. Suggested next step (usually /create-plan)

## Error Handling

If Linear MCP is not available:
1. Format the complete issue in markdown
2. Provide copy-paste text
3. Instruct user to manually create in Linear
4. Suggest installing Linear MCP for future use

Example:
```
⚠️ Linear MCP not available. Here's your formatted issue:

---
TITLE: Fix: Authentication token expires prematurely
PRIORITY: P1
LABELS: bug, authentication, backend

[Full markdown description]
---

Please copy this and create it manually at: https://linear.app/your-team
To enable automatic creation, install Linear MCP: Settings → MCP Servers → Add Linear
```

## Important Notes

- **Be specific**: Vague issues lead to unclear implementations
- **Include context**: Always explain WHY this matters
- **Make it actionable**: Acceptance criteria should be testable
- **Link related work**: Connect to explorations, PRs, other issues
- **Set realistic priority**: Not everything is P0/P1
- **Consider impact**: Who is affected and how badly?

## Next Steps After Issue Creation

1. **Plan**: Use `/create-plan` to design implementation
2. **Explore More**: If needed, `/explore` specific components
3. **Discuss**: Share Linear URL with team for feedback
4. **Execute**: Once planned, use `/execute` to implement