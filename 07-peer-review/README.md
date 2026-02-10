# 👥 Peer Review Skill (Multi-Model)

Get comprehensive code review from multiple AI models (Claude Sonnet + GPT-4o) to identify issues, gain diverse perspectives, and increase confidence in code quality.

## Overview

The `/peer-review` skill provides multi-model code review by:
- Running reviews from 2+ AI models in parallel
- Identifying consensus findings (high confidence)
- Highlighting unique insights from each model
- Resolving contradictions intelligently
- Synthesizing into one actionable report

## Why Multi-Model?

### Single Model Limitations
- Blind spots and biases
- May miss certain issue types
- Single perspective

### Multi-Model Benefits
✅ **Diverse perspectives** - Different models catch different issues
✅ **Reduced bias** - No single model's blind spots
✅ **Higher confidence** - Consensus issues are real
✅ **Unique insights** - Each model has strengths
✅ **Comprehensive** - Better coverage

## Prerequisites

- **Required**: Python 3.8+ with litellm installed
- **Required**: API keys configured in shared/config/.env
- **Recommended**: Recent code changes to review

## Usage

### Basic Usage
```
/peer-review
```

Reviews recent changes with multiple models.

### Review Specific File
```
/peer-review src/auth.ts
```

### Review Git Diff
```
/peer-review --diff
```

## What You Get

### 1. 🤝 Consensus Findings
Issues identified by **multiple models** (high confidence).

### 2. 🔴 Critical Issues
**Any** model flags as critical → investigate.

### 3. 🟡 Important Suggestions
Best practices and improvements identified.

### 4. 💡 Unique Insights
Model-specific findings that others missed.

### 5. ✅ Strengths
What multiple models praised.

### 6. 📊 Agreement Analysis
Where models agreed/disagreed and why.

## Example Report

```markdown
# Peer Review Report (Multi-Model)

## 🤝 Consensus Findings

### SQL Injection Risk - src/auth.ts:42
**Agreed by**: Claude Sonnet, GPT-4o
**Severity**: Critical

Both models identified unsanitized user input.

**Fix**:
\`\`\`typescript
const email = sanitizeInput(req.body.email);
\`\`\`

---

## 💡 Unique Insights

### From Claude Sonnet:
- Suggests extracting validation to reusable module
- Notes error messages may expose system info

### From GPT-4o:
- Identifies potential race condition
- Recommends rate limiting on auth endpoint

---

## 📊 Model Agreement

**High Consensus**:
- SQL injection (both)
- Missing validation (both)

**Divergent Views**:
- Claude: Refactor recommended
- GPT-4o: Current approach acceptable
- **Synthesis**: Consider refactor if code grows

---

## 🎯 Actions

1. Fix SQL injection (Critical - consensus)
2. Add input validation (Important - consensus)
3. Review error messages (Important - Claude)
4. Consider race conditions (Important - GPT-4o)
```

## Model Strengths

| Model | Strengths |
|-------|-----------|
| **Claude Sonnet** | Architecture, security, best practices, code design |
| **GPT-4o** | Algorithms, performance, edge cases, concurrency |

## When to Use

### Use `/peer-review` for:
- ✅ Critical code (auth, payments, security)
- ✅ Architecture decisions
- ✅ Uncertain about approach
- ✅ High-stakes production code
- ✅ Learning opportunity

### Use `/review` instead for:
- 🚀 Quick reviews
- 🚀 Non-critical changes
- 🚀 Time-sensitive
- 🚀 Routine updates

## Interpreting Results

### High Consensus (Both Models Agree)
→ **Trust it**. High confidence, definitely investigate.

### One Model Only
→ **Consider it**. May be valid unique insight.

### Contradictory
→ **Use judgment**. Understand both perspectives.

## Architecture

```
┌─────────────────────────────────────────┐
│         /peer-review Skill              │
│                                         │
│  1. Identify code to review             │
│  2. Run orchestrator script             │
│  3. Present synthesized report          │
└─────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│    peer_review_orchestrator.py          │
│                                         │
│  ┌─────────────┐   ┌─────────────┐     │
│  │   Claude    │   │   GPT-4o    │     │
│  │   Review    │   │   Review    │     │
│  └─────────────┘   └─────────────┘     │
│         │                  │            │
│         └──────┬───────────┘            │
│                ▼                        │
│         Synthesis (Claude)              │
│                                         │
│  Output: Unified Report                 │
└─────────────────────────────────────────┘
```

## Configuration

Uses existing configuration from initial setup:
- `shared/config/.env` - API keys
- `shared/config/litellm_config.yaml` - Model configs
- `shared/venv/` - Python environment

No additional setup needed!

## Troubleshooting

### Script Not Found
```bash
# Verify path
ls shared/scripts/peer_review_orchestrator.py

# Make executable
chmod +x shared/scripts/peer_review_orchestrator.py
```

### Import Error: litellm
```bash
source shared/venv/bin/activate
pip install litellm
```

### API Key Missing
Check `shared/config/.env` has:
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`

### Only 1 Model Available
Need at least 2 models. Verify API keys configured.

## Workflow Integration

```bash
# Typical flow
/execute all           # Implement feature
/review               # Quick single review
/peer-review          # Deep multi-model review
/document             # Update docs
git commit            # Commit with confidence
```

## Performance

- **Speed**: 2-3x slower than `/review` (multiple API calls)
- **Cost**: 2x API usage
- **Value**: Higher confidence, better coverage
- **Recommended**: For critical code

## Best Practices

1. **Use strategically**: Not every change needs peer review
2. **Provide context**: Help models understand intent
3. **Act on consensus**: High-agreement issues are real
4. **Consider unique insights**: Even single-model valuable
5. **Balance with time**: Takes longer but worth it for critical code

## Example: Complete Workflow

```bash
# 1. Implement feature
/execute all

# 2. Quick review
/review

# 3. Fix obvious issues
[make fixes]

# 4. Deep peer review on critical parts
/peer-review src/auth.ts

# 5. Address all findings
[make final fixes]

# 6. Document
/document

# 7. Commit
git commit -m "Add auth with peer review feedback"
```

## Related Skills

- **`/review`**: Single-model review (faster)
- **`/execute`**: Implements before review
- **`/document`**: Documents after review

## Version History

- **1.0.0** (2026-02-06): Initial release with Claude + GPT-4o peer review
