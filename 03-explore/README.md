# Explore Skill 🔍

**Deep exploration and analysis before implementation**

## Purpose

The `/explore` skill helps you thoroughly understand a problem and codebase before writing any code. It's the "think before you build" checkpoint in your development workflow.

## When to Use

- Starting work on a new feature
- Investigating a bug or performance issue
- Understanding how an existing system works
- Before planning implementation (feeds into `/create-plan`)

## What It Does

1. **Analyzes the codebase** - Finds relevant files and traces execution paths
2. **Gathers context** - Pulls in organizational knowledge from WorkIQ, GitHub, docs
3. **Identifies patterns** - Finds similar implementations to reference
4. **Recommends approaches** - Presents 2-3 options with trade-offs
5. **Asks clarifying questions** - Identifies ambiguities that need resolution

## Usage

### Basic Usage
```
/explore How does the authentication system work?
```

### With Linear Issue
```
/explore LINEAR-123
```

### With Specific Focus
```
/explore Performance issue in data processing pipeline
```

## Output

The skill produces a comprehensive exploration report including:

- **Problem Statement** - Refined understanding
- **Affected Components** - Files and their roles
- **Architecture Overview** - Current system structure
- **Similar Patterns** - Existing code to reference
- **Recommended Approach** - Best path forward with rationale
- **Open Questions** - What needs clarification

## Tools Used

- `Glob` - Find files by pattern
- `Grep` - Search code content
- `Read` - Understand implementations
- `WorkIQ` - Organizational context (meetings, emails, discussions)
- `gh` - GitHub issues and PRs

## Example Workflow

```
1. /explore Authentication bug in GCC environments
   → Produces exploration report

2. Review findings, answer any questions

3. /create-plan
   → Uses exploration to build implementation plan

4. /execute
   → Implements based on plan
```

## Tips

- **Be specific** - "Fix login bug" vs "Authentication timeout in restricted clouds"
- **Reference existing issues** - Include Linear/GitHub issue numbers when available
- **Don't rush** - Good exploration saves implementation time
- **Ask follow-ups** - If the exploration raises questions, clarify before planning

## Configuration

No configuration needed - works out of the box with Claude Code.

## Dependencies

- Claude Code (required)
- WorkIQ MCP (optional - for organizational context)
- GitHub CLI (optional - for GitHub integration)

## Version

1.0.0 - Initial release

## Author

Victor Calauhia
