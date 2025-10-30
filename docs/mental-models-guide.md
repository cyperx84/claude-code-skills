# Mental Models Skill: Complete Guide

A comprehensive guide to using the mental-models Claude Code skill for better decision-making and problem-solving.

## Table of Contents

1. [What Are Mental Models?](#what-are-mental-models)
2. [The Skill: Four Modes](#the-skill-four-modes)
3. [All 98 Models Cataloged](#all-98-models-cataloged)
4. [How to Choose the Right Model](#how-to-choose-the-right-model)
5. [Advanced Techniques](#advanced-techniques)
6. [Common Mistakes](#common-mistakes)
7. [Integration with Workflow](#integration-with-workflow)

---

## What Are Mental Models?

Mental models are cognitive frameworks that help you think more effectively. Charlie Munger, Warren Buffett's business partner, advocated building a "latticework of mental models" from multiple disciplines to make better decisions.

### Why Mental Models Matter

**Traditional Thinking**:
- Reactive, emotional decisions
- Single-perspective analysis
- Cognitive biases unchecked
- Shallow "first conclusion" thinking

**Mental Models Approach**:
- Structured, systematic analysis
- Multi-disciplinary perspectives
- Bias awareness and mitigation
- Deep, second and third-order thinking

### The Latticework Concept

The power comes from combining models:
- **Single Model**: One-dimensional view
- **2-3 Models**: Multi-dimensional analysis
- **Latticework**: Models weave together, revealing patterns invisible from single perspective

Example: Career decision analyzed through:
1. **Circle of Competence**: Am I ready?
2. **Second-Order Thinking**: Where does this lead?
3. **Trade-Offs**: What am I giving up?

Each model reveals different insights. Together, they form complete picture.

---

## The Skill: Four Modes

### Mode 1: Quick-Apply (1-2 minutes)

**When to Use**: You know which model you want, need fast insights

**How It Works**:
1. User specifies model + context
2. Skill loads model's Thinking Steps
3. Applies framework to your situation
4. Returns 3-5 actionable insights
5. Provides coaching questions

**Example**:
```
"Apply bottlenecks model to our deployment pipeline that takes 45 minutes"
```

**Best For**:
- Specific, focused problems
- Time-sensitive decisions
- Validating a hypothesis
- Quick sanity checks

### Mode 2: Deep-Analysis (10-15 minutes)

**When to Use**: Complex decision requiring comprehensive analysis

**How It Works**:
1. Problem diagnosis and clarification
2. Automatic model selection (max 3)
3. Systematic application of each model's Thinking Steps
4. Evidence gathering (web search if helpful)
5. Synthesis showing how models interconnect
6. Actionable recommendations
7. WorkSpace folder with all artifacts

**Example**:
```
"/mental-models - Should I leave my stable job for a startup?"
```

**Best For**:
- Major life decisions
- Strategic business choices
- High-stakes technical decisions
- Career crossroads
- Investment decisions

**Output**: WorkSpace folder with 6 files:
- `problem_diagnosis.md`
- `mental_models_selected.md`
- `reasoning_m##_[model1].md`
- `reasoning_m##_[model2].md`
- `reasoning_m##_[model3].md`
- `analysis_report.md`

### Mode 3: Discovery (30 seconds)

**When to Use**: Not sure which models apply to your problem

**How It Works**:
1. User provides keywords or problem description
2. Skill searches 98 models by keywords
3. Returns 5-7 most relevant matches
4. Explains why each matches
5. Offers to quick-apply or deep-analyze

**Example**:
```
"What mental models help with scaling distributed systems?"
```

**Best For**:
- Learning what models exist
- Exploring new domains
- Finding models you didn't know about
- Browsing by category

### Mode 4: Interactive (2-3 minutes + user input)

**When to Use**: Problem is ambiguous, need guidance choosing models

**How It Works**:
1. Skill asks 2-3 clarifying questions
2. Based on answers, scans all models
3. Recommends 3-5 best matches with rationale
4. User chooses one or more
5. Executes quick-apply or deep-analysis

**Example**:
```
"Which mental model should I use for this architecture decision?"
→ Skill asks about time horizon, constraints, concerns
→ Recommends Second-Order Thinking, Trade-Offs, Margin of Safety
→ User selects, skill applies
```

**Best For**:
- First-time users learning the system
- Ambiguous or ill-defined problems
- When you want guided assistance
- Learning which models fit which situations

---

## All 98 Models Cataloged

### General Thinking Tools (m01-m09)

Foundation models for clear thinking:

- **m01 - The Map Is Not the Territory**: Abstractions ≠ reality
- **m02 - Circle of Competence**: Know what you know (and don't)
- **m03 - First-Principle Thinking**: Break down to fundamentals
- **m04 - Thought Experiment**: Mental simulation
- **m05 - Second-Order Thinking**: Consider effects of effects
- **m06 - Probabilistic Thinking**: Think in likelihoods, not certainties
- **m07 - Inversion**: Think backward from failure
- **m08 - Hanlon's Razor**: Don't attribute to malice what's explained by incompetence
- **m09 - Occam's Razor**: Simplest explanation is usually correct

**When to Use**: Any situation requiring clear, structured thinking

### Science (m10-m29)

Natural laws applied to human systems:

**Physics & Chemistry**:
- m10 - Activation Energy
- m11 - Alloying
- m12 - Catalysts
- m17 - Friction and Viscosity
- m20 - Inertia
- m21 - Leverage
- m24 - Relativity
- m28 - Thermodynamics
- m29 - Velocity

**Biology & Evolution**:
- m13 - Cooperation
- m14 - Ecosystems
- m15 - Evolution (Natural Selection)
- m16 - Evolution (Adaptation & Red Queen Effect)
- m22 - Niches
- m23 - Reciprocity
- m25 - Replication
- m26 - Self-Preservation
- m27 - Minimize Energy Output

**Strategy & Structure**:
- m18 - Hierarchical Organization
- m19 - Incentives

**When to Use**: System design, organizational structure, understanding natural constraints

### Systems Thinking (m30-m40)

Understanding complex interconnected systems:

- **m30 - Feedback Loops**: Self-reinforcing or self-correcting systems
- **m31 - Equilibrium**: Balance points in systems
- **m32 - Bottlenecks**: Constraints limiting capacity
- **m33 - Scale**: Non-linear effects of size
- **m34 - Margin of Safety**: Engineer for error
- **m35 - Churn**: Turnover and replacement
- **m36 - Algorithms**: Systematic processes
- **m37 - Critical Mass**: Tipping points
- **m38 - Emergence**: Whole > sum of parts
- **m39 - Irreducibility**: Can't simplify further
- **m40 - Law of Diminishing Returns**: Decreasing marginal gains

**When to Use**: Technical architecture, process optimization, organizational design

### Mathematics (m41-m47)

Quantitative reasoning:

- **m41 - Sampling**: Representative data matters
- **m42 - Randomness**: Distinguish signal from noise
- **m43 - Regression to the Mean**: Extremes revert to average
- **m44 - Multiply by Zero**: Single failure point destroys everything
- **m45 - Equivalence**: Different forms, same value
- **m46 - Surface Area**: Exposure and complexity
- **m47 - Global and Local Maxima**: Optimization landscapes

**When to Use**: Data analysis, risk assessment, optimization problems

### Economics (m48-m59)

Resource allocation and market dynamics:

- **m48 - Scarcity**: Limited resources drive decisions
- **m49 - Supply and Demand**: Market forces
- **m50 - Optimization**: Do more with less
- **m51 - Trade-Offs**: Every choice has opportunity cost
- **m52 - Specialization**: Division of labor
- **m53 - Interdependence**: Connected systems
- **m54 - Efficiency**: Minimize waste
- **m55 - Debt**: Leverage and obligation
- **m56 - Monopoly and Competition**: Market structures
- **m57 - Creative Destruction**: Innovation replaces old
- **m58 - Gresham's Law**: Bad money drives out good
- **m59 - Bubbles**: Unsustainable price inflation

**When to Use**: Business strategy, pricing, resource allocation, market analysis

### Art (m60-m70)

Communication and creative frameworks:

- **m60 - Audience**: Know who you're serving
- **m61 - Genre**: Categories and conventions
- **m62 - Contrast**: Differences create meaning
- **m63 - Framing**: Context shapes perception
- **m64 - Rhythm**: Patterns and timing
- **m65 - Melody**: Core themes
- **m66 - Representation**: Symbols and abstractions
- **m67 - Plot**: Story structure
- **m68 - Character**: Identity and motivation
- **m69 - Setting**: Environment and context
- **m70 - Performance**: Execution matters

**When to Use**: Communication, presentations, writing, product design

### Warfare & Strategy (m71-m75)

Competitive and adversarial thinking:

- **m71 - Seeing the Front**: Ground truth vs reports
- **m72 - Asymmetric Warfare**: Use unique advantages
- **m73 - Two-Front War**: Don't fight multiple battles
- **m74 - Counterinsurgency**: Winning hearts and minds
- **m75 - Mutually Assured Destruction**: Deterrence through consequences

**When to Use**: Competitive strategy, conflict resolution, negotiation

### Human Nature & Judgment (m76-m98)

Cognitive biases and behavioral patterns:

**Trust & Social**:
- m76 - Trust
- m84 - Social Proof
- m93 - Sensitivity to Fairness

**Incentives & Motivation**:
- m77 - Bias from Incentives
- m78 - Pavlovian Association
- m79 - Envy and Jealousy
- m80 - Liking/Disliking Tendency

**Cognitive Biases**:
- m81 - Denial
- m82 - Availability Heuristic
- m83 - Representativeness Heuristic
- m88 - First-Conclusion Bias
- m89 - Overgeneralizing from Small Samples
- m91 - Commitment & Consistency Bias
- m92 - Hindsight Bias
- m94 - Fundamental Attribution Error
- m96 - Survivorship Bias
- m98 - Confirmation Bias

**Instincts**:
- m85 - Narrative Instinct
- m86 - Curiosity Instinct
- m87 - Language Instinct

**Other Tendencies**:
- m90 - Relative Satisfaction
- m95 - Influence of Stress
- m97 - Do-Something Tendency

**When to Use**: Decision-making, team dynamics, negotiations, self-awareness

---

## How to Choose the Right Model

### Decision Tree

**1. What type of problem?**

- **Decision** → m02, m05, m06, m07, m51
- **System/Process** → m30, m32, m33, m34, m38
- **Strategy** → m21, m22, m57, m72, m73
- **Communication** → m60, m63, m67, m85, m87
- **Risk** → m06, m07, m34, m44, m59
- **Team/People** → m13, m19, m76, m77, m93
- **Learning** → m01, m02, m03, m41, m42

**2. What's your time horizon?**

- **Immediate** → Quick, decisive models (m07, m09, m44)
- **Short-term** → Tactical models (m21, m32, m50)
- **Long-term** → Strategic models (m05, m33, m57)

**3. What's your main concern?**

- **Avoiding failure** → m07, m34, m44, m96, m98
- **Understanding complexity** → m01, m30, m38, m39, m53
- **Resource constraints** → m32, m48, m51, m54, m40
- **Competition** → m22, m56, m57, m72, m73
- **Bias/error** → m82, m84, m88, m91, m96, m98

### Starting Points by Experience Level

**Beginner** - Start with General Thinking (m01-m09):
- m01 - Map/Territory: Question assumptions
- m05 - Second-Order Thinking: Think beyond first effects
- m07 - Inversion: What could go wrong?

**Intermediate** - Add Systems Thinking (m30-m40):
- m32 - Bottlenecks: Find constraints
- m34 - Margin of Safety: Build in buffer
- m51 - Trade-Offs: Understand costs

**Advanced** - Combine 3 models (Latticework):
- Pick from different categories
- Show how they interconnect
- Synthesize insights

### Model Combinations That Work Well

**The Decision Triad**:
- m02 (Circle of Competence) - Know your limits
- m05 (Second-Order Thinking) - Long-term view
- m07 (Inversion) - Avoid failure

**The System Optimizer**:
- m32 (Bottlenecks) - Find constraint
- m30 (Feedback Loops) - Self-correction
- m34 (Margin of Safety) - Error tolerance

**The Bias Detector**:
- m82 (Availability) - Recent ≠ common
- m96 (Survivorship) - Selection effects
- m98 (Confirmation) - Seek disconfirmation

**The Strategic Planner**:
- m51 (Trade-Offs) - Opportunity costs
- m33 (Scale) - Growth effects
- m21 (Leverage) - High-impact actions

---

## Advanced Techniques

### Technique 1: Stacking Models

Apply models sequentially, each building on previous:

1. **Inversion** (m07): What would make this fail?
2. **Bottlenecks** (m32): What's the constraint?
3. **Leverage** (m21): Where's the highest-impact fix?

Result: Avoid disaster → Find constraint → Focus effort

### Technique 2: Contrasting Models

Use opposing models to find balance:

- **Specialization** (m52) vs **Interdependence** (m53)
- **Efficiency** (m54) vs **Margin of Safety** (m34)
- **Optimization** (m50) vs **Law of Diminishing Returns** (m40)

Sweet spot often lies between extremes.

### Technique 3: Cross-Domain Application

Apply model from one domain to another:

- **Leverage** (physics) → to business strategy
- **Ecosystems** (biology) → to organizations
- **Framing** (art) → to technical documentation

### Technique 4: Bias Hunting

When making important decision, systematically check biases:

1. **Confirmation Bias** (m98): Am I only seeing supporting evidence?
2. **Availability** (m82): Am I over-weighting recent events?
3. **First-Conclusion** (m88): Did I stop at first answer?
4. **Survivorship** (m96): Am I ignoring failures?
5. **Social Proof** (m84): Am I following the crowd?

### Technique 5: The Meta-Model

Use models to think about models:

- **Map/Territory** (m01): Models are maps, reality is territory
- **Circle of Competence** (m02): Which models do I understand well?
- **Trade-Offs** (m51): Which model to apply given time constraints?

---

## Common Mistakes

### Mistake 1: Analysis Paralysis

**Problem**: Using too many models, overthinking

**Solution**:
- Use Quick-Apply for small decisions
- Max 3 models for any analysis
- Time-box your thinking

### Mistake 2: Model Misapplication

**Problem**: Forcing model that doesn't fit

**Solution**:
- Check "When to Avoid" section
- Use Discovery mode to find better match
- Ask "Does this model illuminate or obscure?"

### Mistake 3: Shallow Application

**Problem**: Knowing model name without following Thinking Steps

**Solution**:
- Always follow the Thinking Steps exactly
- Use Coaching Questions to go deeper
- Apply to real context, not abstract

### Mistake 4: Ignoring Synthesis

**Problem**: Applying models separately without connecting

**Solution**:
- In Deep-Analysis, synthesis is most important section
- Show how models interact and weave together
- Look for patterns across models

### Mistake 5: Forgetting Map/Territory

**Problem**: Treating models as reality, not tools

**Solution**:
- Models simplify reality
- Always validate against actual evidence
- Don't let model override common sense

---

## Integration with Workflow

### For Software Engineers

**Code Review**:
```
"Apply confirmation bias model to this PR review"
```

**Architecture Decisions**:
```
"/mental-models - Microservices vs monolith for our team of 5"
```

**Debugging**:
```
"Quick-apply bottlenecks to production outage"
```

### For Product Managers

**Feature Prioritization**:
```
"Apply leverage and trade-offs to Q1 roadmap planning"
```

**User Research**:
```
"Apply survivorship bias to interpreting customer interviews"
```

**Strategy**:
```
"/mental-models - Should we expand to enterprise market?"
```

### For Managers

**Hiring**:
```
"Apply cognitive bias models to candidate evaluation"
```

**Team Issues**:
```
"Apply incentives model to understanding team conflict"
```

**Performance**:
```
"What mental models help with giving constructive feedback?"
```

### For Personal Use

**Career**:
```
"/mental-models - Job offer decision: FAANG vs startup"
```

**Learning**:
```
"Apply circle of competence to choosing what to learn next"
```

**Habits**:
```
"Apply activation energy to building exercise habit"
```

---

## Learning Path

### Week 1: Fundamentals
- Read all 9 General Thinking models (m01-m09)
- Practice Quick-Apply on small decisions
- Try Discovery mode to browse categories

### Week 2: Systems Thinking
- Focus on m30-m40
- Apply to technical problems at work
- Use Deep-Analysis for one medium decision

### Week 3: Bias Awareness
- Study Human Nature models (m76-m98)
- Hunt for biases in your thinking
- Apply to past decisions (hindsight analysis)

### Week 4: Domain Expansion
- Explore Science, Economics, or Art models
- Try cross-domain applications
- Practice stacking 2-3 models

### Ongoing: Latticework Building
- Deep-Analysis for major decisions
- Collect examples of model combinations
- Teach models to others (best way to learn)

---

## Resources

- **Use Cases**: See [use-cases.md](./use-cases.md) for 27 real-world examples
- **Quick Reference**: See `.skill/resources/quick-reference.md` for fast lookups
- **Model Files**: See `Mental_Models/` for full model descriptions
- **Examples**: See `.skill/examples/` for mode demonstrations

## Getting Help

- **Discovery Mode**: "What mental models apply to [problem]?"
- **Interactive Mode**: "Which mental model should I use?"
- **Quick Reference**: Check `resources/quick-reference.md`
- **Examples**: Browse `.skill/examples/` directory

---

Remember: The goal isn't to use every model, but to build a latticework that helps you think more clearly and decide more wisely. Start simple, practice regularly, and gradually expand your toolkit.
