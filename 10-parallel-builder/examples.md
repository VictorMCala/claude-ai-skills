# Parallel Builder - Examples

## Example 1: Chrome Extension

**User Goal**: Build Chrome extension for article summarization

**Parallel Approaches**:
1. **Brain Dump**: "Build extension that summarizes articles"
   - Result: Basic structure, ugly design, missing features
   - Score: 6/10

2. **Structured**: Detailed manifest v3 specs, API details
   - Result: Technically correct, but bland
   - Score: 7/10

3. **Design-First**: Used Mobbin popup designs as reference
   - Result: Beautiful UI, clear UX, missing save feature
   - Score: 9/10 ⭐ WINNER

4. **Code Template**: Started from Chrome extension boilerplate
   - Result: Solid structure, generic look
   - Score: 7/10

**Winner**: Approach 3 (Design-First) with save functionality from Approach 2

**Time Saved**: 3 hours of iteration trying to fix ugly UI

---

## Example 2: Dashboard App

**User Goal**: Analytics dashboard for SaaS product

**Parallel Approaches**:
1. **Brain Dump**: Quick description, voice input
   - Result: Basic layout, missing charts
   - Score: 5/10

2. **Structured**: Detailed chart specs, data structure
   - Result: Functional but looks like 2010
   - Score: 6/10

3. **Design-First**: shadcn/ui dashboard template as reference
   - Result: Modern, beautiful, but complex
   - Score: 8/10

4. **Code Template**: v0.dev dashboard code
   - Result: Clean, simple, extensible
   - Score: 9/10 ⭐ WINNER

**Winner**: Approach 4 (Code Template) with data structure from Approach 2

**Time Saved**: 4 hours of reinventing dashboard patterns

---

## Example 3: Landing Page

**User Goal**: Product landing page for AI tool

**Parallel Approaches**:
1. **Brain Dump**: "Build a landing page for AI writing tool"
   - Result: Generic template, boring
   - Score: 5/10

2. **Structured**: Detailed sections, copy, CTA placement
   - Result: Complete but generic design
   - Score: 6/10

3. **Design-First**: Dribbble AI product landing pages
   - Result: Stunning, modern, on-brand
   - Score: 9/10 ⭐ WINNER

4. **Hybrid**: Structured copy + design references
   - Result: Great but took longer
   - Score: 8/10

**Winner**: Approach 3 (Design-First) with copy from Approach 2

**Time Saved**: 2 hours of trying to "make it look modern"

---

## Example 4: API Service

**User Goal**: REST API for task management

**Parallel Approaches**:
1. **Brain Dump**: "Build task management API"
   - Result: Basic CRUD, no structure
   - Score: 4/10

2. **Structured**: Detailed OpenAPI spec, endpoints, schemas
   - Result: Well-structured, complete
   - Score: 9/10 ⭐ WINNER

3. **Code Template**: Express.js REST API boilerplate
   - Result: Good structure, generic
   - Score: 7/10

4. **Design-First**: (Skipped - no UI needed)

**Winner**: Approach 2 (Structured) with boilerplate patterns from Approach 3

**Time Saved**: 2 hours of API design decisions

**Learning**: For backend/API projects, structured approach often wins (no UI to show)

---

## Common Patterns

### When Design-First Wins
- UI-heavy projects
- Brand/aesthetics matter
- User experience critical
- Modern look required

### When Structured Wins
- Backend/API projects
- Complex business logic
- Clear requirements exist
- Technical precision needed

### When Code Template Wins
- Similar patterns exist
- Don't reinvent wheel
- Standard implementations
- Time-sensitive projects

### When Brain Dump Wins
- Very simple projects
- Idea is crystal clear in your head
- Rapid prototyping
- You're experienced with the tools

---

## Anti-Patterns

### ❌ Don't:
- Spend >10 minutes per approach
- Get attached to first version
- Try to perfect each version
- Skip comparison step
- Only do 1-2 approaches

### ✅ Do:
- Keep each version quick (7-10 min)
- Compare all versions
- Rate honestly
- Pick winner decisively
- Mix and match best elements
