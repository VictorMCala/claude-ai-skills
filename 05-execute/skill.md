# Execute Implementation Plan

Execute implementation plans step by step, making code changes and validating as you go.

## Your Responsibilities

1. **Read PRD Files for Context** (NEW - Critical for Token Efficiency)
   - **BEFORE each step**: Read relevant PRD files
   - `masterplan.md` - Understand vision and goals
   - `design-guidelines.md` - Know visual requirements
   - `tasks.md` - See current task in context
   - `rules.md` - Follow project-specific behavior rules
   - **Why?** Prevents wasting 80% of tokens reading entire codebase

2. **Understand the Plan**
   - Read the implementation plan provided
   - Parse the step structure and order
   - Identify all files that need modification
   - **Check tasks.md for task breakdown**

3. **Execute ONE Task at a Time** (STRICT - No Batching)
   - Follow the plan's instructions precisely for CURRENT task only
   - Use appropriate tools (Edit, Write, Bash)
   - Validate changes after each step
   - Track progress with todo list
   - **ONE focused task - never combine multiple tasks**
   - Mark task complete in tasks.md when done

4. **Monitor Token Usage** (NEW - Prevent Context Overflow)
   - Track how many files you've read
   - If context feels "heavy" (>10 file reads), warn user
   - Suggest creating/updating PRD files if context is full
   - Reference files by path, not full content dumps

5. **Handle Issues**
   - Stop if errors occur
   - Report problems clearly
   - Ask for guidance when needed
   - Allow user to review before continuing

6. **Validate and Confirm**
   - Check that changes compile/run
   - Verify expected behavior
   - Report what was accomplished
   - **Report how to test** (from agent output, not code)
   - Suggest next steps

## Execution Process

### Phase 1: Pre-Execution (With PRD Context)
1. **Check for PRD files** (if they exist, read them first)
   - Look for: `masterplan.md`, `design-guidelines.md`, `tasks.md`, `rules.md`
   - Read these BEFORE reading any code
   - **Why?** These files contain compressed context that saves tokens

2. **Read the plan** (from file or inline)
   - If `tasks.md` exists, use that as task source
   - Otherwise, parse implementation plan

3. **Check token budget** (estimate)
   - Count files that need to be read
   - If >10 files, warn user about context usage
   - Suggest task breakdown if tasks seem too large

4. **Create todo list** from plan steps
   - **Ensure ONE task at a time** (don't batch)
   - Each task should be focused (<30 min work)

5. **Verify prerequisites** are met

6. **Ask user confirmation** before starting

### Phase 2: Step-by-Step Execution (PRD-Driven)

**CRITICAL**: Execute ONE task at a time. No exceptions.

For each step in the plan:

1. **Read PRD files** (if not already read)
   - `masterplan.md` - Vision and context
   - `design-guidelines.md` - Visual specs (fonts, colors, spacing)
   - `tasks.md` - Find current task
   - `rules.md` - Behavior instructions for this project

2. **Mark step as in_progress** in todo list AND tasks.md

3. **Read ONLY relevant files** for THIS task
   - Reference specific files mentioned in task
   - Don't read entire codebase "just in case"
   - Use PRDs for context, not code exploration

4. **Make changes** using Edit/Write tools
   - Follow design-guidelines.md for visual elements
   - Follow masterplan.md for architectural decisions
   - ONE focused change only

5. **Read agent output** (not just code)
   - Focus on reasoning and explanations
   - Trust AI for syntax (don't micromanage code)
   - Verify agent understands the task correctly

6. **Run validation** (compile, test, or verify)

7. **Mark step as completed** if successful
   - Update tasks.md to mark task done
   - Update todo list

8. **Report progress** to user
   - What was done
   - How to test (from agent reasoning)
   - Token usage status (if high)

9. **Token check** (after each task)
   - If >70% of context used, warn user
   - Suggest updating PRDs with new decisions
   - Consider stopping for context cleanup

### Phase 3: Post-Execution
1. **Summarize what was done**
2. **Run any final checks** (tests, build)
3. **Suggest next steps** (/review, commit, etc.)

## Available Tools

- **Read**: Read files to understand current state
- **Edit**: Modify existing files with precise string replacement
- **Write**: Create new files
- **Bash**: Run commands (compile, test, build)
- **TodoWrite**: Track execution progress
- **AskUserQuestion**: Clarify ambiguities or get approval

## Important Rules

### Do's ✅
- **Read PRD files FIRST** - masterplan.md, design-guidelines.md, tasks.md, rules.md
- **Follow the plan exactly** - Don't deviate unless necessary
- **Read before writing** - Always read files before editing (but only relevant files)
- **ONE task at a time** - NEVER batch multiple tasks (strict rule)
- **Read agent output** - Focus on reasoning, not just code
- **Validate each step** - Check changes compile/work
- **Track progress** - Keep todo list AND tasks.md updated
- **Monitor token usage** - Warn if context >70% full
- **Report clearly** - Tell user what you did and why
- **Ask when unsure** - Better to ask than assume

### Don'ts ❌
- **Don't skip PRD files** - Always read masterplan.md and design-guidelines.md first
- **Don't read entire codebase** - Only read files needed for current task
- **Don't batch tasks** - ONE focused task at a time (critical for token efficiency)
- **Don't skip steps** - Execute in order
- **Don't rush** - One step at a time, validate before moving on
- **Don't assume** - Read actual file content (but selectively)
- **Don't ignore errors** - Stop and report issues
- **Don't make changes beyond the plan** - Stay focused on current task
- **Don't batch completions** - Mark steps done immediately
- **Don't waste tokens** - Reference files by path, not content dumps

### The "Three Wishes" Rule (Critical)

**Analogy**: Like Aladdin's Genie has limited wishes, AI has limited token window per request.

**Problem with vague, large tasks**:
- Agent reads 50 files (80% of tokens spent)
- Little room for thinking/executing (20% of tokens left)
- Result: Poor output, needs rework

**Solution with focused tasks + PRDs**:
- Agent reads 3 PRD files + 2 relevant code files (20% of tokens)
- Most tokens available for execution (80% of tokens)
- Result: High quality output, first try

**Your job**: Enforce ONE small, focused task at a time. Reference PRDs for context.

## Execution Modes

### Mode 1: Step-by-Step (Recommended)
Execute one step at a time, wait for user confirmation

**Usage**: `/execute step 1`

### Mode 2: Auto-Execute
Execute all steps automatically with validation checks

**Usage**: `/execute all` or `/execute auto`

### Mode 3: Dry Run
Parse and show what would be done without making changes

**Usage**: `/execute --dry-run`

## Error Handling

When errors occur:

1. **Stop immediately** - Don't continue
2. **Mark step as failed** in todo
3. **Report the error** with context
4. **Suggest fixes** if possible
5. **Wait for user decision**:
   - Fix and retry
   - Skip step
   - Abort execution

## Validation Strategy

After each step, validate using:

1. **Syntax check**: Ensure code compiles/parses
2. **Type check**: Run TypeScript/linter if applicable
3. **Test run**: Execute relevant tests
4. **Manual verification**: Check expected files exist/modified

## Example Usage

### Example 1: Execute Specific Step

**User**: `/execute step 1`

**Assistant**:
```
📋 Reading implementation plan...

**Plan**: Add multi-language support to Hey Tito

**Total Steps**: 4

**Executing Step 1**: Add Language Configuration Schema

📂 Reading: package.json

✏️ Editing: package.json (lines 43-62)
   Adding heyClaude.language setting

✅ Step 1 Complete

**Changes Made**:
- Added language setting to configuration schema
- Default value: "en-US"
- Description includes language code examples

**Validation**:
- ✅ JSON syntax valid
- ✅ Setting schema well-formed

**Next**: Execute Step 2 with `/execute step 2`
```

---

### Example 2: Auto-Execute All Steps

**User**: `/execute all`

**Assistant**:
```
📋 Reading implementation plan...

**Plan**: Add multi-language support to Hey Tito
**Total Steps**: 4

⚠️ This will execute all 4 steps automatically.
   Changes will be made to 3 files.

Continue? [Yes/No]

[User confirms]

▶️ Executing Step 1: Add Language Configuration Schema
   ✅ Complete (package.json modified)

▶️ Executing Step 2: Add Language Methods to Config Class
   ✅ Complete (src/config.ts modified)

▶️ Executing Step 3: Update Setup Command
   ✅ Complete (src/extension.ts modified)

▶️ Executing Step 4: Use Language in Speech Service
   ✅ Complete (src/azureSpeech.ts and src/extension.ts modified)

🎉 **All Steps Complete!**

**Summary**:
- ✅ 4/4 steps executed successfully
- 📝 4 files modified
- ✏️ ~65 lines changed

**Files Changed**:
1. package.json - Added language setting
2. src/config.ts - Added get/set methods
3. src/extension.ts - Updated setup and initialization
4. src/azureSpeech.ts - Updated initialize method

**Next Steps**:
- Run `/review` to check code quality
- Test the changes manually
- Commit with `git commit`
```

---

### Example 3: Dry Run

**User**: `/execute --dry-run`

**Assistant**:
```
🔍 Dry Run Mode - No changes will be made

**Plan**: Add multi-language support to Hey Tito
**Total Steps**: 4

**Step 1: Add Language Configuration Schema**
  📝 Would modify: package.json (lines 43-62)
  ➕ Would add: language setting to schema

**Step 2: Add Language Methods to Config Class**
  📝 Would modify: src/config.ts
  ➕ Would add: getLanguage() and setLanguage() methods

**Step 3: Update Setup Command**
  📝 Would modify: src/extension.ts (lines 189-241)
  ➕ Would add: language selector quickpick

**Step 4: Use Language in Speech Service**
  📝 Would modify: src/azureSpeech.ts (line 20-30)
  📝 Would modify: src/extension.ts (lines 51-71, 231-236)
  ➕ Would add: language parameter and usage

**Summary**:
- 4 steps to execute
- 4 files to modify
- ~65 lines to change
- Estimated time: 5-10 minutes

Ready to execute for real? Use `/execute step 1` or `/execute all`
```

## Implementation Guidelines

### Reading Files
Always read files before editing:
```
1. Use Read tool to get current content
2. Identify exact location to change
3. Extract old_string precisely (with correct indentation)
4. Prepare new_string with same indentation
```

### Making Edits
Use Edit tool with exact string matching:
```
- Match indentation exactly from Read output
- Don't include line numbers in old_string/new_string
- Make minimal changes (don't refactor unnecessarily)
- Preserve existing code style
```

### Creating Files
Use Write tool for new files:
```
- Follow project conventions
- Include appropriate headers/imports
- Match existing file structure patterns
```

### Running Commands
Use Bash tool for validation:
```
- Compile: npm run compile, tsc, etc.
- Test: npm test, pytest, etc.
- Lint: eslint, flake8, etc.
- Build: npm run build, make, etc.
```

## Progress Tracking

Use TodoWrite to track execution:

```javascript
[
  {
    "content": "Step 1: Add Language Configuration Schema",
    "status": "completed",
    "activeForm": "Adding language configuration"
  },
  {
    "content": "Step 2: Add Language Methods",
    "status": "in_progress",
    "activeForm": "Adding language methods"
  },
  {
    "content": "Step 3: Update Setup Command",
    "status": "pending",
    "activeForm": "Updating setup command"
  }
]
```

## Safety Features

1. **PRD-First Policy** (NEW): Read masterplan.md and design-guidelines.md before reading code
2. **Read-First Policy**: Always read files before editing
3. **One Task at a Time** (STRICT): Never batch multiple tasks - this is CRITICAL for token efficiency
4. **Token Monitoring** (NEW): Track context usage, warn at 70%, suggest PRD updates
5. **Agent Output Focus** (NEW): Read agent reasoning, not just code changes
6. **Validation Checks**: Compile/test after changes
7. **Error Stopping**: Halt on first error
8. **User Confirmation**: Ask before auto-executing all steps

## Token Usage Monitoring

### Signs Context Window is Getting Full:
- 🟡 **Yellow (50-70%)**: You've read 5-10 files - still okay
- 🟠 **Orange (70-85%)**: You've read 10-15 files - warn user
- 🔴 **Red (85%+)**: You've read 15+ files - STOP and suggest:
  - Update PRDs with recent decisions
  - Break current task into smaller pieces
  - Continue in new execution context

### What to Say When Token Budget is High:
```
⚠️ Context Window Alert (70% full)

I've read multiple files and the context window is filling up.

Options:
1. Complete current task and stop (recommended)
2. Update tasks.md with recent decisions to compress context
3. Continue carefully (risk of poor output quality)

What would you like to do?
```

## Output Format

After each step:

```
✅ Step N Complete: [Step Title]

**Changes Made**:
- [List of changes]

**Files Modified**:
- path/to/file1.ts (lines X-Y)
- path/to/file2.ts (lines A-B)

**Validation**:
- ✅ Syntax check passed
- ✅ Type check passed
- ✅ [Other validations]

**Next**: [Suggestion for next action]
```

## Integration with Other Skills

### Before Executing
- `/explore` - Understand codebase
- `/create-plan` - Generate detailed plan

### During Execution
- `AskUserQuestion` - Clarify ambiguities
- `Read` - Understand current state

### After Executing
- `/review` - Check code quality
- `/peer-review` - Get multi-model feedback
- `/document` - Update documentation
- `git commit` - Commit changes

## Common Patterns

### Pattern 1: Add New Configuration
1. Update schema (package.json, config files)
2. Add getter/setter methods
3. Use configuration in code
4. Test configuration persistence

### Pattern 2: Add New Feature
1. Add UI components
2. Add business logic
3. Add tests
4. Update documentation

### Pattern 3: Refactor Code
1. Extract common patterns
2. Update all usage sites
3. Remove old code
4. Run full test suite

## Troubleshooting

### "File not found" Error
- Check working directory
- Verify file paths are absolute
- Read plan again for correct path

### "Edit failed - string not unique" Error
- Read file to see actual content
- Provide more context in old_string
- Or use replace_all if intentional

### "Validation failed" Error
- Check compilation errors
- Fix syntax issues
- Ensure imports are correct
- Ask user for guidance

## Best Practices

1. **Communicate clearly**: Tell user what you're doing
2. **Be precise**: Use exact file paths and line numbers
3. **Validate often**: Check after each change
4. **Handle errors gracefully**: Don't panic, report clearly
5. **Follow the plan**: Trust the planning phase
6. **Ask when stuck**: User can provide context
7. **Track progress**: Keep todos updated
8. **One thing at a time**: Don't rush

## Next Steps After Execution

1. **Review**: Use `/review` to check code quality
2. **Test**: Run manual tests to verify functionality
3. **Commit**: Commit changes with descriptive message
4. **Document**: Use `/document` to update docs
5. **Deploy**: If applicable, deploy changes
