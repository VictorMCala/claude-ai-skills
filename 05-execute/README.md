# 🚀 Execute Skill

Execute implementation plans step by step, making code changes, validating as you go, and tracking progress.

## Overview

The `/execute` skill brings plans to life by:
- Executing implementation plans from `/create-plan`
- Making precise file modifications
- Running validation checks after each step
- Tracking progress with real-time updates
- Handling errors gracefully
- Providing detailed feedback

## Prerequisites

- **Required**: Have an implementation plan (from `/create-plan`)
- **Recommended**: Files and dependencies ready
- **Optional**: Tests in place for validation

## Usage

### Basic Usage

#### Execute Specific Step
```
/execute step 1
```

#### Execute All Steps
```
/execute all
```

#### Dry Run (Preview)
```
/execute --dry-run
```

## Execution Modes

### 1. Step-by-Step Mode (Recommended)
Execute one step at a time with user review between steps.

**Best for:**
- Complex changes
- Learning the codebase
- When you want control
- Critical production code

**Example:**
```
/execute step 1
[Review changes]
/execute step 2
[Review changes]
...
```

### 2. Auto-Execute Mode
Execute all steps automatically with validation between steps.

**Best for:**
- Simple, well-understood changes
- Following trusted plans
- Saving time on routine tasks

**Example:**
```
/execute all

⚠️ This will execute all 4 steps automatically.
   Changes will be made to 3 files.

Continue? [Yes/No]
```

### 3. Dry Run Mode
Preview what would be executed without making any changes.

**Best for:**
- Understanding the scope
- Checking file paths
- Verifying the plan

**Example:**
```
/execute --dry-run

🔍 Dry Run Mode - No changes will be made

Step 1: Would modify package.json
Step 2: Would modify src/config.ts
...
```

## Workflow Integration

### Typical Flow

1. **Explore** → `/explore [feature]`
2. **Create Issue** → `/create-issue [description]`
3. **Plan** → `/create-plan`
4. **Execute** → `/execute all` ← **YOU ARE HERE**
5. **Review** → `/review`
6. **Commit** → `git commit`

## What Happens During Execution

### Step Execution Process

For each step:

1. **📋 Read Files**
   - Reads current file content
   - Understands existing code structure

2. **✏️ Make Changes**
   - Uses Edit tool for modifications
   - Uses Write tool for new files
   - Preserves code style and indentation

3. **✅ Validate**
   - Checks syntax (compilation)
   - Runs type checking if applicable
   - Executes tests if available

4. **📊 Report Progress**
   - Updates todo list
   - Shows what changed
   - Confirms success or reports errors

5. **➡️ Continue or Stop**
   - Moves to next step if successful
   - Stops and reports if error occurs

## Example Execution

### Input
```
/execute step 1
```

### Output
```
📋 Reading implementation plan...

**Plan**: Add multi-language support to Hey Tito
**Step 1/4**: Add Language Configuration Schema

📂 Reading: package.json

✏️ Editing: package.json (lines 43-62)
   Adding heyClaude.language configuration setting

   Changes:
   + "heyClaude.language": {
   +   "type": "string",
   +   "default": "en-US",
   +   "description": "Speech recognition language"
   + }

✅ Step 1 Complete

**Files Modified**:
- package.json (added 5 lines)

**Validation**:
- ✅ JSON syntax valid
- ✅ Schema well-formed

**Progress**: 1/4 steps complete (25%)

**Next**: Run `/execute step 2` to continue
```

## Safety Features

### 1. Read-First Policy
Always reads files before modifying them to ensure accuracy.

### 2. Validation Checks
Compiles/tests after each step to catch errors early.

### 3. Progress Tracking
Keeps todo list updated so you always know where you are.

### 4. Error Handling
Stops immediately on errors and reports clearly.

### 5. User Confirmation
Asks before auto-executing multiple steps.

## Error Handling

When errors occur, the skill will:

1. **Stop immediately** (doesn't continue)
2. **Mark step as failed** in todo list
3. **Show error details** with context
4. **Suggest fixes** when possible
5. **Wait for your decision**:
   - Fix the issue and retry
   - Skip the problematic step
   - Abort execution

### Example Error

```
❌ Step 2 Failed: Add Language Methods

**Error**: File not found: src/config.ts

**Possible Causes**:
- Working directory is incorrect
- File path in plan is wrong
- File was moved/deleted

**Suggestions**:
1. Check current directory with `pwd`
2. Verify file exists with `ls src/`
3. Update plan with correct path

**Next**: Fix the issue and run `/execute step 2` again
```

## Validation Strategy

After each step, validates using:

| Check Type | Description | When |
|------------|-------------|------|
| **Syntax** | Code parses correctly | Always |
| **Type Check** | TypeScript/types valid | For TS files |
| **Linting** | Code style compliance | If linter present |
| **Tests** | Unit tests pass | For testable changes |
| **Build** | Project compiles | For compiled projects |

## Progress Tracking

The skill maintains a todo list showing:

- ✅ Completed steps (green)
- 🔄 Current step (yellow)
- ⏳ Pending steps (gray)
- ❌ Failed steps (red)

### Example Progress

```
📊 Execution Progress:

✅ Step 1: Add Language Configuration Schema
✅ Step 2: Add Language Methods to Config Class
🔄 Step 3: Update Setup Command (in progress)
⏳ Step 4: Use Language in Speech Service

Progress: 50% (2/4 complete)
```

## Tips for Best Results

### Do's ✅
- **Read the plan first** - Understand what will happen
- **Use dry-run** - Preview before committing
- **Execute step-by-step** - For complex changes
- **Review each step** - Check changes make sense
- **Run tests** - Validate as you go
- **Commit often** - After successful steps

### Don'ts ❌
- **Don't skip validation** - Always check changes compile
- **Don't ignore errors** - Fix issues before continuing
- **Don't rush** - Take time to review
- **Don't edit the plan mid-execution** - Complete or restart
- **Don't manually edit files during execution** - Let skill handle it

## Configuration

No configuration needed - works out of the box!

The skill automatically detects:
- Project type (TypeScript, Python, etc.)
- Build commands (npm, tsc, pytest, etc.)
- Test commands
- Linting tools

## Troubleshooting

### Issue: "Cannot find plan"
**Solution**: Provide the plan inline or reference a plan file

### Issue: "Edit failed - string not found"
**Solution**: The file may have changed. Re-run `/explore` and `/create-plan`

### Issue: "Validation failed"
**Solution**: Check compilation errors, fix syntax issues, ensure imports are correct

### Issue: "Step keeps failing"
**Solution**: Use `/review` to check the code, or manually fix and skip the step

## Advanced Usage

### Execute from Plan File

```
/execute from plan-file.md
```

### Execute with Custom Validation

```
/execute step 1 --validate="npm test"
```

### Skip Validation (Use Carefully)

```
/execute step 1 --no-validate
```

## Integration with Other Skills

### Before Execution
- **`/explore`**: Understand the codebase first
- **`/create-plan`**: Generate detailed implementation plan

### During Execution
- **`Read`**: Understands current file state
- **`Edit`**: Makes precise modifications
- **`Write`**: Creates new files
- **`Bash`**: Runs validation commands
- **`TodoWrite`**: Tracks progress

### After Execution
- **`/review`**: Check code quality
- **`/peer-review`**: Get multi-model feedback
- **`/document`**: Update documentation
- **`git commit`**: Commit the changes

## Example: Complete Workflow

```bash
# 1. Explore the feature area
/explore How does authentication work?

# 2. Create an issue
/create-issue Add 2FA support to authentication

# 3. Create a plan
/create-plan for Linear issue ENG-123

# 4. Execute the plan (YOU ARE HERE)
/execute --dry-run          # Preview first
/execute step 1             # Execute carefully
/execute step 2
/execute step 3

# 5. Review the changes
/review

# 6. Commit
git add .
git commit -m "Add 2FA support"
```

## Performance

- **Speed**: Typically 30-60 seconds per step
- **Accuracy**: High (reads files, validates syntax)
- **Safety**: Very safe (stops on errors, validates)

## Related Skills

- **`/create-plan`**: Creates the plan to execute
- **`/review`**: Reviews the executed code
- **`/peer-review`**: Multi-model code review
- **`/explore`**: Understand before executing

## Version History

- **1.0.0** (2026-02-06): Initial release with step-by-step execution, validation, and progress tracking
