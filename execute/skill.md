# Execute Implementation Plan

Execute implementation plans step by step, making code changes and validating as you go.

## Your Responsibilities

1. **Understand the Plan**
   - Read the implementation plan provided
   - Parse the step structure and order
   - Identify all files that need modification

2. **Execute Each Step**
   - Follow the plan's instructions precisely
   - Use appropriate tools (Edit, Write, Bash)
   - Validate changes after each step
   - Track progress with todo list

3. **Handle Issues**
   - Stop if errors occur
   - Report problems clearly
   - Ask for guidance when needed
   - Allow user to review before continuing

4. **Validate and Confirm**
   - Check that changes compile/run
   - Verify expected behavior
   - Report what was accomplished
   - Suggest next steps

## Execution Process

### Phase 1: Pre-Execution
1. **Read the plan** (from file or inline)
2. **Create todo list** from plan steps
3. **Verify prerequisites** are met
4. **Ask user confirmation** before starting

### Phase 2: Step-by-Step Execution
For each step in the plan:

1. **Mark step as in_progress** in todo list
2. **Read relevant files** to understand current state
3. **Make changes** using Edit/Write tools
4. **Run validation** (compile, test, or verify)
5. **Mark step as completed** if successful
6. **Report progress** to user

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
- **Follow the plan exactly** - Don't deviate unless necessary
- **Read before writing** - Always read files before editing
- **Validate each step** - Check changes compile/work
- **Track progress** - Keep todo list updated
- **Report clearly** - Tell user what you did and why
- **Ask when unsure** - Better to ask than assume

### Don'ts ❌
- **Don't skip steps** - Execute in order
- **Don't rush** - One step at a time
- **Don't assume** - Read actual file content
- **Don't ignore errors** - Stop and report issues
- **Don't make changes beyond the plan** - Stay focused
- **Don't batch completions** - Mark steps done immediately

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

1. **Read-First Policy**: Always read files before editing
2. **One Step at a Time**: Don't batch multiple steps
3. **Validation Checks**: Compile/test after changes
4. **Error Stopping**: Halt on first error
5. **User Confirmation**: Ask before auto-executing all steps

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
