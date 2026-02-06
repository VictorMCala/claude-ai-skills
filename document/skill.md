# Documentation Generator

Generate or update documentation for code, features, and projects.

## Your Responsibilities

1. **Understand What to Document**
   - Read recent changes or target code
   - Identify what needs documentation
   - Determine documentation type needed

2. **Generate Documentation**
   - README files
   - API documentation
   - Code comments/docstrings
   - Usage guides
   - Architecture docs

3. **Update Existing Docs**
   - Keep docs in sync with code
   - Update examples
   - Add new sections
   - Fix outdated information

## Documentation Types

### 1. README Files
- Project overview
- Installation instructions
- Usage examples
- Configuration
- Contributing guidelines

### 2. API Documentation
- Function/method signatures
- Parameters and return values
- Usage examples
- Error handling

### 3. Code Comments
- Inline explanations
- Complex logic clarification
- TODO/FIXME notes
- Architecture decisions

### 4. Guides
- Getting started
- Tutorials
- Best practices
- Troubleshooting

## Documentation Standards

### README Template
```markdown
# Project Name

Brief description of what this does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\`\`\`bash
# Installation commands
\`\`\`

## Usage

\`\`\`language
// Usage example
\`\`\`

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| option1 | string | "value" | What it does |

## API Reference

### `functionName(param1, param2)`

Description of what this function does.

**Parameters:**
- `param1` (type): Description
- `param2` (type): Description

**Returns:** Description of return value

**Example:**
\`\`\`language
const result = functionName('value1', 'value2');
\`\`\`

## Contributing

Guidelines for contributors.

## License

License information.
```

### API Doc Template (JSDoc/TSDoc)
```typescript
/**
 * Brief description of function
 *
 * Longer description if needed with more context.
 *
 * @param param1 - Description of first parameter
 * @param param2 - Description of second parameter
 * @returns Description of what is returned
 * @throws {ErrorType} When this error occurs
 *
 * @example
 * ```typescript
 * const result = myFunction('value1', 'value2');
 * console.log(result); // Output description
 * ```
 */
function myFunction(param1: string, param2: number): ReturnType {
  // Implementation
}
```

## Process

### Step 1: Analyze Code
```
1. Read the code that needs documentation
2. Understand what it does
3. Identify public APIs
4. Note configuration options
5. Find usage patterns
```

### Step 2: Determine Scope
```
1. What needs documentation?
   - New feature?
   - Changed behavior?
   - New file?
   - Project setup?

2. What level of detail?
   - Quick reference?
   - Comprehensive guide?
   - API docs?
```

### Step 3: Generate/Update Docs
```
1. Create new documentation OR
2. Update existing documentation
3. Include examples
4. Add relevant context
5. Keep it concise but complete
```

### Step 4: Verify Quality
```
1. Examples are correct
2. Links work
3. Formatting is clean
4. No outdated information
5. Clear and understandable
```

## Available Tools

- **Read**: Read existing code and docs
- **Edit**: Update existing documentation
- **Write**: Create new documentation files
- **Bash**: Test examples, check links
- **Glob**: Find all files needing docs

## Output Format

Provide documentation ready to use or commit:

```markdown
# Documentation Generated

## Files Created/Updated:

### 📄 README.md
[Full content of README]

### 📄 API.md
[Full content of API docs]

### 💬 Code Comments
**File**: `src/auth.ts`
**Lines**: 42-58

Added JSDoc comments for authentication functions.

---

## Summary:
- ✅ Created comprehensive README
- ✅ Documented all public APIs
- ✅ Added usage examples
- ✅ Updated configuration docs

## Next Steps:
- Review documentation for accuracy
- Test all code examples
- Commit: `git commit -m "Add documentation for auth feature"`
```

## Documentation Principles

### 1. Write for Your Audience
- **Beginners**: Step-by-step, explain concepts
- **Experienced**: Quick reference, advanced features
- **Contributors**: Architecture, design decisions

### 2. Show, Don't Just Tell
```
❌ Bad: "Use the function to process data"
✅ Good:
```
```typescript
// Process user data
const result = processData(userData);
```
```

### 3. Keep It Updated
- Update docs with code changes
- Mark deprecated features
- Remove outdated examples

### 4. Be Concise
- Short paragraphs
- Bullet points
- Clear headings
- Scannable format

### 5. Include Examples
- Real-world use cases
- Common scenarios
- Edge cases
- Error handling

## Common Documentation Needs

### After Feature Implementation
```
1. Update README with new feature
2. Add API documentation
3. Include usage examples
4. Update configuration docs
```

### New Project
```
1. Create README.md
2. Add LICENSE
3. Write CONTRIBUTING.md
4. Create basic examples
```

### API Changes
```
1. Update function signatures
2. Add/update JSDoc comments
3. Update API reference
4. Add migration guide if breaking
```

### Bug Fix
```
1. Update relevant docs
2. Add example of fix
3. Note in CHANGELOG
4. Update troubleshooting if applicable
```

## Example Usage

### User Input
```
/document the multi-language feature we just implemented
```

### Skill Output
```
# Documentation Generated

## Files Updated:

### 📄 README.md (Updated)

Added section for multi-language support:

\`\`\`markdown
## Multi-Language Support

Hey Tito now supports speech recognition in 10+ languages!

### Supported Languages

- English (en-US)
- Spanish (es-ES)
- French (fr-FR)
- German (de-DE)
- Japanese (ja-JP)
- Chinese (zh-CN)
- Portuguese (pt-BR)
- Italian (it-IT)
- Korean (ko-KR)
- Russian (ru-RU)

### Configuration

1. Open VS Code settings
2. Search for "Hey Tito"
3. Set `heyClaude.language` to your preferred language code

Or run the setup command:

\`\`\`bash
Cmd+Shift+P → "Hey Tito: Setup Azure Config"
\`\`\`

The setup wizard will prompt you to select your language.

### Usage

Once configured, Hey Tito will recognize speech in your selected language.

\`\`\`typescript
// Example: Spanish speech recognition
"Hola Claude, escribe una función..." → Recognized in Spanish
\`\`\`
\`\`\`

---

### 💬 Code Comments (Added)

**File**: `src/azureSpeech.ts:23`

\`\`\`typescript
/**
 * Initialize Azure Speech Service
 *
 * @param apiKey - Azure Speech API key from Azure Portal
 * @param region - Azure region (e.g., 'eastus', 'westeurope')
 * @param language - BCP-47 language code (e.g., 'en-US', 'es-ES')
 *                   Defaults to 'en-US' if not provided
 */
async initialize(apiKey: string, region: string, language?: string): Promise<void> {
  this.speechConfig = sdk.SpeechConfig.fromSubscription(apiKey, region);
  this.speechConfig.speechRecognitionLanguage = language || 'en-US';
  // ...
}
\`\`\`

---

## Summary:
- ✅ Updated README with multi-language section
- ✅ Added usage examples in multiple languages
- ✅ Documented configuration steps
- ✅ Added JSDoc comments to initialize method
- ✅ Listed all supported languages

## Next Steps:
- Review documentation for accuracy
- Test the examples
- Commit: `git commit -m "Document multi-language support feature"`
```

## Integration with Other Skills

- **After `/execute`**: Document what was implemented
- **After `/review`**: Ensure code is documented
- **Before committing**: Update relevant docs
- **With `/learning-opportunity`**: Document lessons learned

## Best Practices

1. **Document as you go**: Don't wait until the end
2. **Keep it simple**: Clear > comprehensive
3. **Test examples**: Ensure they work
4. **Use templates**: Consistency matters
5. **Update, don't duplicate**: Keep docs DRY
6. **Think about the reader**: What do they need to know?

## Tips for Good Documentation

### Do's ✅
- Use examples liberally
- Show common use cases
- Include troubleshooting
- Keep formatting consistent
- Link related docs
- Explain the "why"

### Don'ts ❌
- Don't assume knowledge
- Don't use jargon without explanation
- Don't write walls of text
- Don't skip examples
- Don't let docs go stale

## Next Steps After Documentation

1. **Review docs**: Read them yourself
2. **Test examples**: Run all code examples
3. **Get feedback**: Have someone else review
4. **Commit**: Add docs to version control
5. **Publish**: Deploy if applicable (e.g., docs site)

## Related Skills

- **`/execute`**: Implements before documenting
- **`/review`**: Reviews before documenting
- **`/learning-opportunity`**: Extracts learnings to document
