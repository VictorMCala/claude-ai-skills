# 📋 Create Issue Skill

Transform exploration findings, bugs, or feature requests into well-structured Linear issues with proper formatting, priority, and acceptance criteria.

## Overview

The `/create-issue` skill helps you create comprehensive, actionable Linear issues by:
- Structuring information with consistent templates
- Setting appropriate priorities based on impact
- Generating clear acceptance criteria
- Integrating context from exploration results
- Creating issues directly in Linear via MCP

## Prerequisites

- **Linear MCP Server**: Must be installed and configured
  - Install: `claude mcp add linear` (in Claude Code UI)
  - Configure: Add Linear API key to MCP settings
  - Verify: Run `/create-issue --check` to test connection

## Usage

### Basic Usage

```
/create-issue Fix authentication timeout after 5 minutes of inactivity
```

### With Exploration Context

```
/explore How does session management work?
[After exploration completes]
/create-issue Fix session timeout based on exploration findings
```

### With Details

```
/create-issue Add dark mode support
Priority: P2
Team: Frontend
Project: UI Improvements
```

## Issue Types

The skill automatically formats issues based on type:

- **Bug**: `Fix: [problem description]`
- **Feature**: `Add: [what is being added]`
- **Improvement**: `Improve: [what is being enhanced]`
- **Tech Debt**: `Refactor: [what needs refactoring]`

## Priority Levels

- **P0 (Urgent)**: Production broken, security issue, data loss
- **P1 (High)**: Major feature broken, blocking work
- **P2 (Medium)**: Normal features, non-blocking bugs
- **P3 (Low)**: Nice-to-have, minor polish

## Issue Template

Every issue includes:

1. **Problem Statement**: Clear description of the need
2. **Context**: Background and exploration findings
3. **Current/Expected Behavior**: For bugs
4. **Affected Components**: Files and areas of code
5. **Acceptance Criteria**: Testable checkboxes
6. **Technical Notes**: Implementation hints
7. **Related**: Links to explorations, PRs, issues

## Workflow Integration

### Typical Flow

1. **Explore** → `/explore [feature/bug]`
2. **Create Issue** → `/create-issue [based on exploration]`
3. **Plan** → `/create-plan` (references the Linear issue)
4. **Execute** → `/execute` (implements the plan)
5. **Review** → `/review` and `/peer-review`

## Examples

### Example 1: Bug Report

**Input**:
```
/create-issue Users getting logged out after 5 minutes, should be 30 minutes
```

**Output**:
```
✅ Created Linear Issue: ENG-123

Title: Fix: Session timeout occurring at 5 minutes instead of 30 minutes

Priority: P1 (High)
Team: Backend
Labels: bug, authentication

URL: https://linear.app/team/issue/ENG-123

Description includes:
- Problem statement
- Current vs expected behavior
- Affected components (session management)
- Acceptance criteria (session lasts 30min, logout warning, etc.)
- Technical notes (check SESSION_TIMEOUT config)
```

### Example 2: Feature Request

**Input**:
```
/create-issue Add ability to export data as CSV from dashboard
```

**Output**:
```
✅ Created Linear Issue: ENG-124

Title: Add: CSV export functionality for dashboard data

Priority: P2 (Medium)
Team: Frontend
Labels: feature, dashboard, export

URL: https://linear.app/team/issue/ENG-124

Description includes:
- Feature requirements
- User impact and value
- Affected components (dashboard, data service)
- Acceptance criteria (export button, CSV format, date range filter)
- Technical notes (use existing export service pattern)
```

## Configuration

If Linear MCP is not available, the skill will:
1. Format the issue with proper structure
2. Provide markdown copy-paste text
3. Guide you to create it manually in Linear

## Tips

- **Be specific**: Include context, impact, and expected behavior
- **Reference explorations**: Mention if this came from `/explore`
- **Set priority**: Help the skill by indicating urgency
- **Add team info**: Specify which team owns this if known
- **Link related work**: Mention related PRs, issues, or explorations

## Related Skills

- **`/explore`**: Investigate before creating issues
- **`/create-plan`**: Plan implementation after issue is created
- **`/review`**: Review code related to the issue

## Troubleshooting

### Linear MCP Not Connected
```
Error: Linear MCP server not found
```
**Solution**: Install Linear MCP in Claude Code settings → MCP Servers

### Missing API Key
```
Error: Linear API key not configured
```
**Solution**: Add your Linear API key to MCP configuration

### Can't Determine Priority
```
What priority should this be? (P0/P1/P2/P3)
```
**Solution**: The skill will ask clarifying questions to determine priority

## Version History

- **1.0.0** (2026-02-06): Initial release with Linear MCP integration
