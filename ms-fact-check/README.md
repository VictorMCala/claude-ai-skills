# Fact-Checker Skill

A systematic fact-checking skill for Claude Code that verifies statements and problems against real documentation, meetings, ICMs, and repositories.

## Installation

This skill is already installed at: `~/.claude/skills/fact-checker/`

## Usage

### Basic Command

```bash
/fact-check <statement or problem to verify>
```

### Examples

```bash
# Verify a single claim
/fact-check The deployment pipeline is broken in GCC

# Verify multiple related claims
/fact-check Web grounding fails in GCC and there's no commercial fallback

# Verify technical specifications
/fact-check BizChat uses GPT-5 in all clouds

# Verify architectural claims
/fact-check The evaluation pipelines are not available in restricted clouds
```

## How It Works

1. **Breaks down claims** into verifiable components
2. **Creates a todo list** to track verification progress
3. **Queries WorkIQ** for evidence from:
   - ICM incidents
   - SharePoint documents
   - Meeting recordings
   - ADO work items
   - Architecture docs
   - Compliance specifications
4. **Compiles evidence** with sources
5. **Classifies results**:
   - ✅ VERIFIED
   - ⚠️ PARTIALLY VERIFIED
   - ❌ NOT VERIFIED
   - 🔍 NEEDS MORE INFO

## Output Format

For each claim verified, you'll get:
- Verification status
- Supporting evidence with sources
- Key findings summary
- Links to documentation
- Recommendations (if applicable)

## Customization

### Modify the Prompt

Edit [`skill.md`](./skill.md) to customize:
- Verification process steps
- Output format
- Classification criteria
- Focus areas (e.g., security, performance, compliance)

### Add New Capabilities

Edit [`metadata.json`](./metadata.json) to:
- Change the command trigger
- Update description
- Add new capabilities
- Modify examples

## Tips for Best Results

1. **Be specific** - Include context like cloud (GCC, Commercial), component names, or time periods
2. **One topic at a time** - Focus on related claims rather than mixing unrelated topics
3. **Use technical terms** - Reference specific systems (BizChat, Catalyst, Heron, etc.)
4. **Include constraints** - Mention if you only want specific types of evidence (e.g., "only ICMs")

## Advanced Usage

### Fact-check from a document

```bash
/fact-check Based on the architecture doc at [URL], verify these 5 claims: [paste claims]
```

### Compare across clouds

```bash
/fact-check Compare feature X behavior: Commercial vs GCC vs GCCH
```

### Historical verification

```bash
/fact-check Was the web grounding issue in GCC resolved? Check ICMs from October 2025
```

## Integration with Other Skills

This skill works well with:
- **workiq-mcp**: Automatically queries M365 data for evidence
- Built-in tools: Uses Read, Grep, and Bash when checking code repositories

## Troubleshooting

**WorkIQ errors**: If queries fail, the skill will retry with simpler phrasing

**No evidence found**: Skill will clearly indicate when claims can't be verified

**Partial verification**: Skill distinguishes between fully verified and partially verified claims

## Version History

- **1.0.0** (2026-02-05): Initial release with systematic multi-source verification
