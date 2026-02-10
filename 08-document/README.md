# 📚 Document Skill

Generate and update comprehensive documentation for code, features, and projects automatically.

## Overview

The `/document` skill creates and maintains documentation by:
- Generating README files
- Writing API documentation
- Adding code comments (JSDoc/TSDoc)
- Creating usage guides
- Updating configuration docs
- Providing working examples

## Prerequisites

- Code to document (recently implemented or existing)
- Understanding of what changed or needs docs

## Usage

### Basic Usage
```
/document
```

Documents recent changes.

### Document Specific Feature
```
/document the authentication system
```

### Document Specific File
```
/document src/auth.ts
```

## What Gets Documented

### 1. README Files 📄
- Project overview
- Installation steps
- Usage examples
- Configuration options
- Troubleshooting

### 2. API Documentation 📋
- Function signatures
- Parameters and returns
- Usage examples
- Error handling

### 3. Code Comments 💬
- JSDoc/TSDoc annotations
- Complex logic explanations
- Architecture decisions
- TODO/FIXME notes

### 4. Guides 📖
- Getting started tutorials
- Best practices
- Common patterns
- Migration guides

## Documentation Templates

### README Template
```markdown
# Project Name

Description

## Features
- Feature list

## Installation
Installation steps

## Usage
Usage examples

## Configuration
Config options

## API Reference
API docs

## Contributing
Contribution guidelines
```

### API Doc Template (TypeScript)
```typescript
/**
 * Function description
 *
 * @param param1 - Parameter description
 * @param param2 - Parameter description
 * @returns Return value description
 *
 * @example
 * ```typescript
 * const result = myFunction('value1', 'value2');
 * ```
 */
```

## Example Output

### Input
```
/document the multi-language feature
```

### Output
```markdown
# Documentation Generated

## Files Updated:

### 📄 README.md

Added Multi-Language Support section:

## Multi-Language Support

Hey Tito now supports 10+ languages!

### Supported Languages
- English (en-US)
- Spanish (es-ES)
- French (fr-FR)
- [... more ...]

### Configuration
\`\`\`bash
Settings → Hey Tito → Language
\`\`\`

### Usage Example
\`\`\`typescript
// Spanish speech recognition
"Hola Claude, escribe..." → Recognized
\`\`\`

---

### 💬 Code Comments Added

**src/azureSpeech.ts:23**
\`\`\`typescript
/**
 * Initialize Azure Speech Service
 * @param language - BCP-47 code (e.g., 'en-US')
 */
async initialize(apiKey, region, language?) {
  // ...
}
\`\`\`

---

## Summary:
✅ Updated README
✅ Added usage examples
✅ Documented configuration
✅ Added JSDoc comments

## Next Steps:
- Review for accuracy
- Test examples
- Commit changes
```

## Documentation Principles

### 1. Write for Your Audience
- **Beginners**: Step-by-step, concepts explained
- **Experienced**: Quick reference, advanced features
- **Contributors**: Architecture, design decisions

### 2. Show, Don't Tell
Include working code examples, not just descriptions.

### 3. Keep It Updated
Update docs when code changes, mark deprecated features.

### 4. Be Concise
Short paragraphs, bullet points, scannable format.

### 5. Include Examples
Real-world use cases, common scenarios, error handling.

## Common Use Cases

### After Feature Implementation
```
1. Update README
2. Add API docs
3. Include examples
4. Update config docs
```

### New Project
```
1. Create README.md
2. Add LICENSE
3. Write CONTRIBUTING.md
4. Create examples/
```

### API Changes
```
1. Update signatures
2. Update JSDoc
3. Add migration guide
4. Update examples
```

### Bug Fix
```
1. Update relevant docs
2. Add fix example
3. Update troubleshooting
```

## Workflow Integration

```bash
# Typical flow
/execute all        # Implement
/review             # Review
/document          # Document ← YOU ARE HERE
git commit         # Commit
```

## Configuration

No configuration needed - works out of the box!

Automatically detects:
- Project language/framework
- Documentation style (JSDoc, TSDoc, etc.)
- Existing doc structure

## Tips for Good Documentation

### Do's ✅
- Use examples
- Show common use cases
- Include troubleshooting
- Keep formatting consistent
- Explain the "why"

### Don'ts ❌
- Don't assume knowledge
- Don't use unexplained jargon
- Don't skip examples
- Don't let docs go stale

## Example: Complete Workflow

```bash
# 1. Implement feature
/execute all

# 2. Review code
/review

# 3. Fix issues
[make fixes]

# 4. Document everything
/document

# 5. Commit
git add .
git commit -m "Add feature with full documentation"
```

## Related Skills

- **`/execute`**: Implements code to document
- **`/review`**: Reviews before documenting
- **`/learning-opportunity`**: Extracts learnings

## Version History

- **1.0.0** (2026-02-06): Initial release with README, API docs, and code comment generation
