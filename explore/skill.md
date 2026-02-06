# Exploration Phase

Your task is NOT to implement yet, but to fully understand and prepare.

## Your Responsibilities

1. **Analyze and understand the existing codebase thoroughly**
   - Use Glob to find relevant files
   - Use Grep to search for similar patterns
   - Use Read to understand current implementations

2. **Determine exactly how this feature integrates**
   - Identify dependencies
   - Map out the current architecture
   - Consider edge cases (within reason, don't go overboard)
   - Note constraints and limitations

3. **Clearly identify anything unclear or ambiguous**
   - In the user's description
   - In the current implementation
   - List all questions that need clarification

## Your Process

1. **Problem Understanding**
   - Restate the problem in your own words
   - Identify the core requirement
   - List assumptions that need validation

2. **Codebase Exploration**
   - Find relevant files using Glob patterns
   - Trace execution paths using Read + Grep
   - Document current architecture
   - Identify similar implementations to reference

3. **Context Gathering**
   - Use WorkIQ for organizational context (meetings, discussions, decisions)
   - Check GitHub for related PRs and issues using gh CLI
   - Review existing documentation

4. **Analysis Output**
   - Refined problem statement
   - Affected components with file paths
   - Dependencies and constraints
   - Similar patterns found in codebase
   - 2-3 potential approaches with trade-offs
   - Recommended approach with clear rationale

## Available Tools

- **Glob**: Find files by pattern (e.g., "**/*.ts", "src/components/**")
- **Grep**: Search code content for keywords
- **Read**: Read files to understand implementation
- **WorkIQ (mcp__workiq-mcp__ask_work_iq)**: Organizational context
- **Bash(gh)**: GitHub issues and PRs
- **TodoWrite**: Track exploration progress

## Important Rules

- Do NOT implement anything yet - this is pure exploration
- Do NOT assume any requirements beyond what's explicitly described
- Ask clarifying questions before making assumptions
- Be thorough but not exhaustive - focus on what's needed for planning

## Output Format

Use this structure for your exploration results:

### Problem Statement
[Refined understanding of what needs to be solved]

### Affected Components
- `path/to/file1.ts` (lines X-Y) - [Role in the solution]
- `path/to/file2.ts` - [How it needs to change]

### Current Architecture
```
[Simple diagram or bullet points showing relevant structure]
```

### Similar Patterns Found
1. **Pattern in `path/to/example.ts`** (lines X-Y)
   - How it works: [brief explanation]
   - Why it's relevant: [connection to current task]
   - What we can reuse: [specific elements]

### Context from Organization
- **Meeting (Date)**: [Key decision or discussion from WorkIQ]
- **PR #123**: [Relevant implementation or approach]
- **Documentation**: [Relevant specs, ADRs, or guides]

### Potential Approaches

#### Option 1: [Descriptive Name]
**Description**: [What this approach entails]

**Pros**:
- [Benefit 1]
- [Benefit 2]

**Cons**:
- [Drawback 1]
- [Drawback 2]

**Effort**: [S/M/L/XL estimate]

#### Option 2: [Descriptive Name]
[Same structure]

#### Option 3: [Descriptive Name]
[Same structure]

### Recommended Approach

**Choice**: Option [X]

**Rationale**: [Why this is the best choice given the constraints, team patterns, and requirements]

### Open Questions
- [ ] Question 1?
- [ ] Question 2?

### Next Steps
Once questions are answered:
- `/create-plan` to generate implementation plan
