# Peer Review (Multi-Model)

Get code review feedback from multiple AI models (Claude + GPT-4o) for diverse perspectives and comprehensive analysis.

## Your Responsibilities

1. **Identify Code to Review**
   - Determine what changed recently
   - Get file paths or diff
   - Understand the context

2. **Run Multi-Model Review**
   - Execute peer_review_orchestrator.py
   - Collect reviews from multiple models
   - Synthesize findings

3. **Present Unified Report**
   - Show consensus findings
   - Highlight unique insights
   - Resolve contradictions
   - Prioritize actions

## Why Multi-Model Review?

### Benefits
- **Diverse Perspectives**: Different models catch different issues
- **Reduced Bias**: No single model's blind spots
- **Increased Confidence**: Consensus on critical issues
- **Unique Insights**: Each model has strengths
- **Comprehensive Coverage**: More thorough than single review

### Model Strengths
- **Claude Sonnet**: Architecture, security, best practices
- **GPT-4o**: Performance, algorithms, edge cases

## Available Tools

- **Bash**: Run peer_review_orchestrator.py script
- **Read**: Read files to provide context
- **Bash(git)**: Get git diff for review

## Process

### Step 1: Prepare for Review
```
1. Identify what to review (files or diff)
2. Gather context (what changed, why)
3. Verify orchestrator script is ready
```

### Step 2: Run Multi-Model Review
```
1. Execute peer_review_orchestrator.py
2. Pass file path or --diff flag
3. Include context if needed
4. Collect output
```

### Step 3: Present Results
```
1. Parse synthesized report
2. Format for readability
3. Highlight key findings
4. Provide action items
```

## Usage Patterns

### Pattern 1: Review Recent Changes
```
1. Get git diff: git diff HEAD
2. Run orchestrator on diff
3. Present synthesized report
```

### Pattern 2: Review Specific File
```
1. Read file path from user
2. Run orchestrator on file
3. Present synthesized report
```

### Pattern 3: Review with Context
```
1. Get implementation plan or Linear issue
2. Run orchestrator with context
3. Present synthesized report
```

## Orchestrator Script

**Location**: `shared/scripts/peer_review_orchestrator.py`

**Usage**:
```bash
# Review specific file
python3 peer_review_orchestrator.py path/to/file.ts

# Review git diff
python3 peer_review_orchestrator.py HEAD --diff

# Review with context
python3 peer_review_orchestrator.py file.ts --context "Added auth feature"

# Save to file
python3 peer_review_orchestrator.py file.ts --output review.md
```

**Requirements**:
- Python 3.8+
- litellm package
- Environment variables configured (AZURE_OPENAI_API_KEY, etc.)

## Output Format

```markdown
# Peer Review Report (Multi-Model)

## 🤝 Consensus Findings
[Issues identified by multiple models]

### Security Issue: SQL Injection Risk
**Agreed by**: Claude, GPT-4o
**File**: src/auth.ts:42
**Severity**: Critical

Both models identified unsanitized user input in SQL query.

---

## 🔴 Critical Issues

### 1. [Issue from any model marked critical]
**Identified by**: GPT-4o
**File**: path/to/file:line

[Description and fix]

---

## 🟡 Important Suggestions

### 1. [Important findings]
**Identified by**: Claude

[Description]

---

## 💡 Unique Insights

### From Claude Sonnet:
- Architecture pattern suggestion
- Security best practice recommendation

### From GPT-4o:
- Performance optimization opportunity
- Edge case handling improvement

---

## ✅ Strengths Identified

Multiple models praised:
- Clean code structure
- Proper error handling
- Good test coverage

---

## 📊 Model Agreement Analysis

**High Consensus** (both models agree):
- Critical security issue in auth.ts
- Performance concern in query.ts

**Divergent Views**:
- Claude suggests refactoring, GPT-4o says current approach fine
- Analysis: [Synthesis of perspectives]

---

## 🎯 Prioritized Actions

1. Fix SQL injection (Critical - both models)
2. Add input validation (Important - both models)
3. Consider refactoring (Optional - Claude only)
```

## Example Usage

### User Input
```
/peer-review
```

### Skill Response
```
🔍 Analyzing recent changes...

Found changes in:
- src/auth.ts (45 lines added)
- src/config.ts (12 lines modified)

👥 Running multi-model peer review...
  📝 Getting review from Claude Sonnet...
  📝 Getting review from GPT-4o (Azure)...

🔄 Synthesizing feedback...

---

# Peer Review Report (Multi-Model)

## 🤝 Consensus Findings

Both Claude and GPT-4o identified:

### 1. Missing Input Validation - src/auth.ts:42
**Severity**: Critical
**Category**: Security

User-provided email not validated before use in database query.

**Recommended Fix**:
```typescript
if (!isValidEmail(email)) {
  throw new Error('Invalid email format');
}
```

---

## 💡 Unique Insights

### From Claude Sonnet:
- Suggests extracting validation logic to separate module for reusability
- Notes that error messages could expose system information

### From GPT-4o:
- Identifies potential race condition in concurrent requests
- Suggests adding rate limiting for auth endpoint

---

## 🎯 Prioritized Actions

1. **Critical**: Add email validation (both models)
2. **Important**: Review error message content (Claude)
3. **Important**: Consider race condition handling (GPT-4o)
4. **Nice-to-have**: Extract validation module (Claude)

---

**Next Steps**:
- Fix critical issues immediately
- Run `/review` again after fixes
- Consider unique insights for future improvements
```

## When to Use Peer Review

Use `/peer-review` when:
- **Critical changes**: Security, authentication, payments
- **Architecture decisions**: Want multiple perspectives
- **Uncertain about approach**: Need validation
- **Learning opportunity**: See different AI perspectives
- **High-stakes code**: Production systems, public APIs

Use `/review` (single model) when:
- Quick review needed
- Non-critical changes
- Time is limited
- Routine code changes

## Interpreting Results

### High Consensus
When both models agree, **trust it**. High confidence in finding.

### Divergent Views
When models disagree:
- **Critical issues**: If either model flags critical, investigate
- **Suggestions**: Consider both perspectives, use judgment
- **Style/preference**: Your call

### Unique Insights
Pay attention to unique findings:
- May reveal model-specific strengths
- Could be valuable alternative perspectives
- Worth investigating even if not consensus

## Configuration

The orchestrator uses configuration from:
```
shared/config/.env
shared/config/litellm_config.yaml
```

Ensure these are set up (should be from initial setup).

## Troubleshooting

### "litellm not installed"
```bash
source venv/bin/activate
pip install litellm
```

### "Azure API key not found"
Check `.env` file has `AZURE_OPENAI_API_KEY`

### "Only 1 model available"
At least 2 models needed. Check API key configuration.

### Script execution fails
```bash
# Make executable
chmod +x shared/scripts/peer_review_orchestrator.py

# Test directly
python3 shared/scripts/peer_review_orchestrator.py --help
```

## Integration with Other Skills

- **After `/execute`**: Get multi-perspective review
- **After `/review`**: Get second opinion on complex changes
- **Before committing**: Final validation on critical code
- **Before `/document`**: Ensure quality first

## Best Practices

1. **Use for important code**: Not needed for every change
2. **Provide context**: Help models understand intent
3. **Act on consensus**: High-agreement issues are real
4. **Consider unique insights**: Even single-model findings valuable
5. **Balance with time**: Peer review takes longer than single review

## Performance

- **Speed**: ~2-3x slower than single `/review` (parallel API calls)
- **Cost**: 2x API usage (two models)
- **Value**: Higher confidence, better coverage

## Next Steps After Peer Review

1. **Address consensus issues**: High priority
2. **Evaluate unique insights**: Consider carefully
3. **Run `/document`**: Update docs
4. **Commit changes**: With confidence
5. **Learn**: Note patterns for future

## Related Skills

- **`/review`**: Single-model review (faster)
- **`/execute`**: What you review after implementation
- **`/document`**: Document after review
