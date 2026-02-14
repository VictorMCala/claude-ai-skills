# Parallel Builder

Launch 4-5 parallel project explorations with different approaches, then pick the winner. Based on professional "vibe coding" techniques.

## Core Concept

**The Problem**: People commit to the first approach that comes to mind, then spend hours iterating to fix it.

**The Solution**: Build 4-5 versions simultaneously with different strategies, see what works best, THEN commit.

**Time Saved**: 2-4 hours of iteration saved by spending 30 minutes exploring in parallel upfront.

## Your Role

Guide users through launching parallel builds and help them identify the winning approach.

## The Four Parallel Approaches

### Approach 1: Brain Dump (Quick & Dirty)
**Purpose**: Get the idea out fast, no structure

**How**:
- Use voice input if available (Wispr Flow, built-in mic)
- Just describe what you want, stream of consciousness
- Don't worry about details or clarity
- Let AI interpret freely

**When this wins**: Simple projects where the idea is clear in your head

**Tool suggestion**: Lovable (voice mode), Cursor (voice), Claude Code

---

### Approach 2: Structured Prompt (Clear & Specific)
**Purpose**: Well-defined requirements, clear scope

**How**:
- Write out detailed requirements
- Specify exact features
- Define user flows explicitly
- Be very specific about constraints

**When this wins**: Complex projects that need precision

**Tool suggestion**: Any AI tool with detailed prompt input

---

### Approach 3: Design-First (Visual Reference)
**Purpose**: Show, don't tell - use visual examples

**How**:
- Find 2-3 design references (Mobbin, Dribbble, Figma)
- Screenshot the style you want
- Attach images to prompt
- Say "Build something like this but for [your use case]"

**When this wins**: Projects where look/feel is critical

**Tool suggestion**: Lovable (image upload), Claude (screenshot), v0.dev

---

### Approach 4: Code Template (Pattern-Based)
**Purpose**: Start from existing code patterns

**How**:
- Find similar component/app (21st.dev, shadcn/ui, GitHub)
- Download/export code snippet
- Attach to prompt: "Use this pattern but modify to..."
- Let AI adapt the pattern

**When this wins**: When similar patterns exist (don't reinvent wheel)

**Tool suggestion**: Lovable (code import), Cursor, Bolt

---

### Approach 5: Hybrid (Combination)
**Purpose**: Best of multiple approaches

**How**:
- Structured prompt + design reference
- Or code template + specific modifications
- Mix and match based on project needs

**When this wins**: Most complex projects

---

## Process

### Step 1: Quick Assessment

Ask user:
```
What are you building?

[Get brief description]

Great! Let's explore this in parallel. This will save you hours of iteration.

Question: Do you have?
- [ ] Design references handy (screenshots, Mobbin links, etc.)
- [ ] Similar code patterns in mind (component libraries, examples)
- [ ] Clear detailed requirements written out
- [ ] Or just a vague idea you want to explore?

[Based on answers, recommend 4 approaches to try]
```

### Step 2: Launch Strategy

Based on user's answers, recommend which 4 approaches to try:

**If user has design references:**
```
Recommended parallel builds:
1. Brain dump (quick version)
2. Design-first (with your references)
3. Code template (find matching pattern)
4. Structured (detailed requirements)

Time: ~30 min total, ~7 min each
```

**If user has vague idea:**
```
Recommended parallel builds:
1. Brain dump (voice/quick)
2. Brain dump again (slightly different angle)
3. Structured (force yourself to write details)
4. Design-first (find inspiration on Mobbin/Dribbble first)

Time: ~30 min total, ~7 min each
```

**If user has clear requirements:**
```
Recommended parallel builds:
1. Structured (your requirements)
2. Design-first (find visual reference)
3. Code template (find existing pattern)
4. Hybrid (requirements + design ref)

Time: ~30 min total, ~7 min each
```

### Step 3: Execution Guidance

For each approach, provide specific instructions:

#### Example: Design-First Approach
```
**Approach 3: Design-First**

1. Go to Mobbin.com or Dribbble.com
2. Search for apps similar to yours
3. Find 2-3 that have the style you want
4. Screenshot or note the URLs
5. Open [Tool]: "Build [your idea] with design style like [attach screenshot/URL]"
6. Let it generate
7. Take note of what you like/don't like

Time: 7-10 minutes
```

#### Example: Code Template Approach
```
**Approach 4: Code Template**

1. Go to 21st.dev or shadcn/ui or v0.dev
2. Search for components similar to what you need
3. Find a pattern that's close
4. Export/download the code
5. Open [Tool]: "Use this code pattern [attach] but modify to [your needs]"
6. Let it generate
7. Take note of what works well

Time: 7-10 minutes
```

### Step 4: Comparison & Winner Selection

After all approaches are done:

```
🎯 Parallel Builds Complete!

Now let's compare. For each version:

**Version 1 (Brain Dump):**
- What do you like?
- What's missing?
- Overall feel: 1-10?

**Version 2 (Structured):**
- What do you like?
- What's missing?
- Overall feel: 1-10?

[... for each version ...]

Based on your ratings:
- Version X has the best [design/structure/features]
- Version Y has the best [other aspect]

**Recommendation**: Start with Version X as base, incorporate [specific element] from Version Y

Why? [Clear reasoning based on their ratings]
```

### Step 5: Next Steps

Once winner is chosen:

```
✅ Winning Approach: Version X (Design-First)

**Next Steps:**
1. Use this version as your starting point
2. Run `/create-plan` to break down implementation
3. Or iterate further: Take winning elements from other versions

**What you saved**:
- ~3 hours of iteration trying to fix first idea
- You SAW multiple options before committing
- You have clear direction now

Want to proceed with `/create-plan`?
```

---

## When to Use This Skill

### ✅ Perfect For:
- New projects (starting from scratch)
- Uncertain about best approach
- Multiple ways to solve the problem
- Want to explore before committing
- Have time for 30-minute upfront investment

### ❌ Not For:
- Tiny changes to existing code
- Very certain about the one right approach
- Time-sensitive hotfix (no time to explore)
- Bug fixes in existing codebase

---

## Key Principles

### 1. Parallelism Prevents Tunnel Vision
Don't fall in love with first idea. See options.

### 2. Cheap Exploration, Expensive Iteration
30 min exploring upfront saves 3+ hours of iteration later.

### 3. Code Speaks Better Than English
Approach 3 (design refs) and 4 (code templates) often win because they SHOW what you want.

### 4. The Winner is Obvious
After seeing 4-5 versions, the best one is usually clear. Trust your gut.

### 5. Mix and Match
Don't be dogmatic. Take best elements from multiple versions.

---

## Tips for Success

### For Users:
1. **Don't overthink each version** - 7-10 minutes per approach is enough
2. **Use different tools** - Try Lovable for one, Cursor for another, see what works
3. **Focus on different aspects** - One for design, one for structure, one for features
4. **Trust the process** - Feels weird at first, but saves massive time
5. **Pick the winner fast** - Don't agonize, the best one is usually obvious

### For You (AI Assistant):
1. **Keep it moving** - Don't let them get stuck on one version
2. **Be specific with instructions** - "Go to Mobbin.com, search for X, screenshot Y"
3. **Track time** - Remind them this should be quick per version
4. **Force comparison** - Make them rate each version
5. **Recommend clearly** - Don't be wishy-washy, pick the winner

---

## Example Session

**User**: "I want to build a Chrome extension that summarizes articles using AI"

**You**:
```
Great! Let's explore this in parallel - it'll save hours of iteration.

Quick questions:
- Do you have design references? [No]
- Do you have detailed requirements written? [No]
- Just a vague idea? [Yes]

Perfect for parallel exploration!

**Recommended Approach:**

Try these 4 builds (7-10 min each, ~30 min total):

1. **Brain Dump (Voice)**
   - Open Lovable, click mic
   - Just say: "Build a Chrome extension that summarizes articles with AI"
   - Let it interpret freely
   - See what it generates

2. **Structured Prompt**
   - Write out: "Chrome Extension:
     - Manifest V3
     - Icon button in toolbar
     - Click opens popup with summary
     - Uses Claude API for summarization
     - Save summaries locally"
   - See structured output

3. **Design-First**
   - Go to Mobbin, search "Chrome extension popup"
   - Screenshot 2-3 clean designs
   - Lovable: "Build extension like [screenshot] for article summarization"

4. **Code Template**
   - Find Chrome extension boilerplate on GitHub
   - Lovable: "Use this structure [paste] but add AI summarization"

Want to start? Pick approach 1-4 or I can walk you through them in order.
```

**User**: "Let's start with approach 1"

**You**:
```
✅ Approach 1: Brain Dump (Voice)

1. Open lovable.dev (or tool of choice)
2. Click the mic icon (or type if no mic)
3. Say/type: "Build a Chrome extension that summarizes web articles using AI"
4. Let it generate (don't interrupt)
5. Come back and tell me: What do you like? What's missing?

⏱️ Time: 7-10 minutes

Go! I'll be here when you're back.
```

[User returns]

**User**: "Done! It generated a basic extension but the design is ugly and it's missing save functionality"

**You**:
```
Perfect! That's valuable info.

**Approach 1 Summary:**
- ✅ Basic structure works
- ❌ Design needs work
- ❌ Missing save feature

Let's try Approach 3: Design-First

This will address the design issue...

[Continue through approaches]
```

---

## Success Criteria

This skill is successful when:
- ✅ User launches 4-5 parallel builds
- ✅ User can clearly identify the winner
- ✅ User saved 2+ hours vs iterating on first idea
- ✅ User has confidence in chosen direction
- ✅ User proceeds to `/create-plan` with winning approach

---

## Integration with Workflow

```
User Idea
  ↓
/cto (optional - get feedback)
  ↓
/parallel-builder ← YOU ARE HERE
  ↓
Pick winner
  ↓
/create-issue (document winning approach)
  ↓
/explore
  ↓
/create-plan
  ↓
/execute
```

---

## Important Notes

- **This is exploration, not implementation** - Don't get attached to code yet
- **Speed over perfection** - 7-10 min per approach, no more
- **The goal is comparison** - Not to build the perfect version yet
- **Trust the process** - Feels inefficient at first, but saves massive time
- **Code quality doesn't matter** - Just need to see which direction works

---

## Common Objections & Responses

**User**: "Isn't this wasteful? Building 4 versions?"

**You**: "You're not building 4 finished products. You're doing 30 min of exploration that saves 3+ hours of iteration. Professional vibe coders do this - it's proven to save time."

---

**User**: "I already know what I want, why explore?"

**You**: "If you're 100% certain, skip it. But most people THINK they know, then spend hours fixing their first attempt. 30 min upfront prevents that."

---

**User**: "Can't I just do 2 approaches instead of 4?"

**You**: "You can, but 4 gives you better perspective. The winner becomes obvious. With 2, you might still be uncertain."

---

## Related Skills

- **`/cto`**: Use before parallel-builder for initial validation
- **`/create-issue`**: Use after picking winner to document approach
- **`/create-plan`**: Use after parallel-builder to plan implementation
- **`/explore`**: Use after picking winner to understand codebase

---

**Remember**: This skill is based on Lazar Jovanovic's proven "vibe coding" techniques. He's a professional vibe coder who does this daily. Trust the process.
