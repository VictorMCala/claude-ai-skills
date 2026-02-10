# 👔 CTO (Chief Technology Officer) Advisor Skill

Your AI technical advisor for brainstorming, validating, and refining product ideas before any code is written.

## Overview

The `/cto` skill acts as an experienced CTO to help you:
- Brainstorm product ideas
- Refine requirements and scope
- Get technical consultation
- Assess feasibility and risks
- Define MVP features
- Choose the right tech stack
- Prepare for implementation

**This is Step 0 in your development workflow** - use it before you start building anything.

## Prerequisites

- A product idea (even if it's not fully formed)
- Willingness to discuss and refine
- Openness to questions and feedback

## Usage

### Start a Consultation
```
/cto
```

Begins interactive CTO consultation session.

### With Initial Idea
```
/cto I want to build a Chrome extension that summarizes web pages
```

Jump-starts consultation with your idea.

### For Feature Validation
```
/cto Help me think through adding real-time collaboration to my app
```

Get technical guidance on specific features.

## What Happens in a Consultation

### 1. Discovery Phase (5-10 questions)
The CTO asks about:
- The problem you're solving
- Target users
- Core value proposition
- Success metrics
- Existing alternatives

### 2. Feature Discussion
Collaboratively explore:
- Must-have vs. nice-to-have features
- User flows
- Technical requirements
- Integration needs

### 3. Technical Consultation
Get advice on:
- Architecture approach
- Tech stack recommendations
- Scalability considerations
- Security and compliance

### 4. Risk Assessment
Identify:
- Technical challenges
- Resource requirements
- Timeline realities
- Potential blockers

### 5. Product Brief
Receive comprehensive document with:
- Product vision
- MVP feature list
- Technical approach
- Risk mitigation
- Ready-to-use text for `/create-issue`

## Example Consultation

### Input
```
/cto I want to build a tool that helps developers learn by turning their code into teaching material
```

### CTO Response
```
Excellent idea! Let me understand this better:

1. Who are your target users?
   - Junior developers learning to code?
   - Senior developers teaching others?
   - Bootcamp instructors?
   - All of the above?

2. What kind of "teaching material"?
   - Step-by-step code explanations?
   - Video tutorials?
   - Interactive exercises?
   - Documentation?

3. Where does the code come from?
   - Users paste their own code?
   - Analyze GitHub repositories?
   - IDE integration?

4. What makes this different from just using ChatGPT on code?
   - Specialized output format?
   - Better for learning specifically?
   - Integration with learning platforms?

[... interactive discussion continues ...]
```

### Final Output
```markdown
# Product Brief: CodeTeach

## 📋 Overview
**Product Vision**: Transform working code into comprehensive teaching materials automatically

**Target Users**: Developers who want to share knowledge and learners who want real-world examples

**Core Problem**: Creating good teaching materials from code is time-consuming

**Success Metrics**:
- Users create 10+ lessons per week
- 80% of generated content needs minimal editing
- 50% user retention after first month

---

## 🎯 MVP Features (v1.0)

### Must Have
1. **Code Input**
   - Description: Paste code or upload files
   - User Value: Easy to get started
   - Complexity: S

2. **Explanation Generation**
   - Description: AI breaks down code into steps with explanations
   - User Value: Core teaching value
   - Complexity: M

3. **Export to Markdown**
   - Description: Download as formatted markdown
   - User Value: Share anywhere
   - Complexity: S

---

## 🏗️ Technical Approach

### Recommended Architecture
Web application with AI backend

### Tech Stack
- **Frontend**: Next.js + React (fast development, great SEO)
- **Backend**: Next.js API routes (keep it simple)
- **AI**: Anthropic Claude API (best for code explanation)
- **Database**: Supabase (quick setup, auth included)
- **Deployment**: Vercel (zero-config deployment)

### Why This Stack?
- Rapid MVP development (2-3 weeks)
- Low operational overhead
- Excellent developer experience
- Easy to scale later

---

[... rest of comprehensive brief ...]

## 📋 Ready for `/create-issue`

```
Title: Build CodeTeach - AI-powered code teaching material generator

## Problem
Developers spend hours manually creating teaching materials from working code.
Need automated way to transform code into comprehensive, easy-to-understand lessons.

## Proposed Solution
Web app that takes code input and generates step-by-step explanations,
visual diagrams, and practice exercises automatically using AI.

## Target Users
- Developers teaching others
- Technical writers
- Bootcamp instructors
- Open source maintainers

## MVP Features
1. Code input (paste or upload)
2. AI-generated step-by-step explanations
3. Export to markdown
4. Basic syntax highlighting
5. Simple share links

## Technical Approach
Next.js web app with Claude API for explanations, Supabase for data

## Success Metrics
- 10+ lessons created per user per week
- 80% content quality (needs minimal editing)
- 50% user retention after 30 days

## Estimated Complexity
M (Medium) - 2-3 weeks for MVP
```
```

## CTO Consultation Principles

### 1. Ask Before Assuming
Understand the vision before suggesting solutions.

### 2. Start Simple
MVP should be achievable, not ambitious.

### 3. Provide Options
Offer 2-3 approaches with clear trade-offs.

### 4. Be Realistic
Honest about complexity, timeline, and risks.

### 5. Think User-First
Every feature should have clear user value.

### 6. Document Decisions
Capture the "why" behind recommendations.

## Common Use Cases

### New Product Idea
```
/cto
→ Full discovery and planning
→ Comprehensive product brief
→ Ready to create issue
```

### Major Feature
```
/cto Should I add real-time collaboration?
→ Feasibility assessment
→ Architecture advice
→ Complexity estimate
```

### Technical Decision
```
/cto Should I use REST API or GraphQL?
→ Compare approaches
→ Recommend based on your needs
→ Explain trade-offs
```

### MVP Scoping
```
/cto Help me define v1.0
→ Distinguish must-have vs. nice-to-have
→ Identify quick wins
→ Plan phased rollout
```

## Workflow Integration

```
COMPLETE DEVELOPMENT WORKFLOW:

0. /cto                      ← START HERE
   ↓ [Product Brief Created]

1. /create-issue            ← Capture in Linear
   ↓ [Issue: LINEAR-123]

2. /explore LINEAR-123      ← Technical research
   ↓ [Exploration Report]

3. /create-plan LINEAR-123  ← Implementation plan
   ↓ [Detailed Plan]

4. /execute                 ← Build it
   ↓ [Code Complete]

5. /review                  ← Quality check
   ↓ [Review Findings]

6. /peer-review            ← Multi-model feedback
   ↓ [Consensus Review]

7. /document               ← Update docs
   ↓ [Documentation Updated]

8. /learning-opportunity   ← Extract lessons
   ↓ [Learning Report]
```

## Tips for Great Consultations

### Do's ✅
- Share your full vision, even if unclear
- Ask questions if recommendations aren't clear
- Be honest about constraints (time, budget, skills)
- Challenge suggestions if they don't feel right
- Think about users throughout

### Don'ts ❌
- Don't skip the discovery phase
- Don't rush to implementation
- Don't ignore technical debt warnings
- Don't be afraid to say "I don't know"
- Don't oversimplify complex problems

## Output Types

### Product Brief
Comprehensive document with vision, features, tech approach, risks.

**When**: New products or major features

### Technical Recommendation
Specific advice on architecture or technology choices.

**When**: Technical decisions needed

### Feasibility Assessment
Analysis of whether an idea is achievable.

**When**: Validating ambitious ideas

### MVP Scope Definition
Clear list of what's in/out for first version.

**When**: Need to scope down to essentials

## Real-World Examples

### Example 1: Chrome Extension
```
Idea: "Summarize web pages with AI"

CTO Output:
- MVP: One-click popup with bullet points
- Tech: Manifest V3 + Claude API
- Risk: Chrome Web Store approval delay
- Timeline: 2-3 weeks
- Complexity: M
```

### Example 2: SaaS Product
```
Idea: "Project management for remote teams"

CTO Output:
- MVP: Kanban board + real-time updates
- Tech: Next.js + Supabase + WebSockets
- Risk: Real-time scaling challenges
- Timeline: 6-8 weeks
- Complexity: L
```

### Example 3: Developer Tool
```
Idea: "CLI that refactors code automatically"

CTO Output:
- MVP: Single language support + basic patterns
- Tech: Node.js CLI + AST parsing + Claude API
- Risk: Code correctness critical
- Timeline: 3-4 weeks
- Complexity: M
```

## Benefits

### For Non-Technical PMs
- Translate ideas into technical plans
- Understand feasibility and complexity
- Make informed technical decisions
- Communicate effectively with developers

### For Technical Founders
- Validate architecture choices
- Get second opinion on approach
- Identify risks early
- Define clear MVP scope

### For Everyone
- Start with clarity, not confusion
- Avoid common pitfalls
- Build the right thing
- Save time and resources

## When NOT to Use

❌ **Small bug fixes** - Just fix it
❌ **Obvious improvements** - Use `/create-issue` directly
❌ **Well-defined tasks** - Skip to `/create-plan`
❌ **Urgent hotfixes** - No time for consultation

## Success Criteria

Consultation is successful when:
- ✅ You understand what you're building and why
- ✅ MVP is scoped to essentials
- ✅ Technical approach is sound
- ✅ Risks are known with mitigation plans
- ✅ You're confident to proceed
- ✅ Next steps are crystal clear

## Related Skills

- **`/create-issue`**: Create Linear issue from CTO brief
- **`/explore`**: Validate technical approach
- **`/create-plan`**: Execute the strategy

## Version History

- **1.0.0** (2026-02-10): Initial release - AI CTO advisor for product ideation and technical consultation

---

**Remember**: Every successful product starts with clear thinking. Take the time to consult your CTO before you build.
