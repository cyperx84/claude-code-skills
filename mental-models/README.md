# Mental Models Skill

Apply Charlie Munger's "latticework of mental models" to enhance decision-making, problem-solving, and structured thinking in any workflow.

## Overview

The Mental Models skill provides instant access to 98 curated cognitive frameworks from multiple disciplines including General Thinking, Science, Economics, Mathematics, Systems Thinking, Human Nature, Warfare/Strategy, and Art. Use these frameworks to think more clearly, avoid cognitive biases, and make better decisions.

## Features

- **98 Mental Models** across 8 categories
- **4 Operational Modes**: Quick-Apply, Deep-Analysis, Discovery, Interactive
- **Context-Aware**: Works with code, business decisions, personal choices, any workflow
- **Structured Frameworks**: Each model includes Description, Thinking Steps, Coaching Questions
- **Latticework Approach**: Combine 2-3 models for multi-dimensional analysis
- **WorkSpace Integration**: Deep-analysis mode creates comprehensive analysis artifacts

## Installation

### Local Installation (Recommended for First-Time Users)

Use the skill directly from this directory:

```bash
cd mental-models
# Skill is now available when working in this directory
```

### Global Installation

Make the skill available across all projects:

```bash
# Symlink (recommended - updates automatically)
ln -s $(pwd)/.skill ~/.claude/skills/mental-models

# Or copy (static - needs manual updates)
cp -r .skill ~/.claude/skills/mental-models
```

## Quick Start

###Use the skill with simple natural language:

```
"Apply second-order thinking to this code refactoring"

"/mental-models - Should I accept this job offer or stay at current company?"

"What mental models help with scaling distributed systems?"

"Which mental model should I use for this architecture decision?"
```

## Four Modes

### 1. Quick-Apply Mode (1-2 minutes)

**When**: You know which model to use, need fast insights

**Example**:
```
"Apply bottlenecks model to our deployment pipeline that takes 45 minutes"
```

**Output**: 3-5 actionable insights, relevant coaching questions, inline response

### 2. Deep-Analysis Mode (10-15 minutes)

**When**: Complex decision requiring comprehensive multi-model analysis

**Example**:
```
"/mental-models - Should we migrate from monolith to microservices?
We have 8 engineers, 50K users, growing 20%/month."
```

**Output**: WorkSpace folder with 6 files including problem diagnosis, model selection rationale, detailed reasoning, and synthesis report

### 3. Discovery Mode (30 seconds)

**When**: Not sure which models apply to your problem

**Example**:
```
"What mental models help with team conflict resolution?"
```

**Output**: 5-7 relevant models with explanations, offer to apply them

### 4. Interactive Mode (2-3 minutes + user input)

**When**: Problem is ambiguous, need guidance

**Example**:
```
"Help me choose the right mental model for this decision"
→ Skill asks clarifying questions
→ Recommends 3-5 models with reasoning
→ User selects, skill applies
```

## The 98 Mental Models

### General Thinking Tools (m01-m09)
Foundation models for clear thinking:
- m01 - The Map Is Not the Territory
- m02 - Circle of Competence
- m03 - First-Principle Thinking
- m05 - Second-Order Thinking
- m07 - Inversion
- m06 - Probabilistic Thinking
- And 3 more...

### Science (m10-m29)
Natural laws applied to human systems:
- m10 - Activation Energy
- m20 - Inertia
- m21 - Leverage
- m13 - Cooperation
- m14 - Ecosystems
- And 15 more...

### Systems Thinking (m30-m40)
Understanding complex interconnected systems:
- m30 - Feedback Loops
- m32 - Bottlenecks
- m33 - Scale
- m34 - Margin of Safety
- m38 - Emergence
- And 6 more...

### Mathematics (m41-m47)
Quantitative reasoning frameworks:
- m41 - Sampling
- m42 - Randomness
- m43 - Regression to the Mean
- m44 - Multiply by Zero
- And 3 more...

### Economics (m48-m59)
Resource allocation and market dynamics:
- m48 - Scarcity
- m49 - Supply and Demand
- m51 - Trade-Offs
- m57 - Creative Destruction
- m59 - Bubbles
- And 7 more...

### Art (m60-m70)
Communication and creative frameworks:
- m60 - Audience
- m62 - Contrast
- m63 - Framing
- m67 - Plot
- m85 - Narrative Instinct
- And 6 more...

### Warfare & Strategy (m71-m75)
Competitive and adversarial thinking:
- m71 - Seeing the Front
- m72 - Asymmetric Warfare
- m73 - Two-Front War
- And 2 more...

### Human Nature & Judgment (m76-m98)
Cognitive biases and behavioral patterns:
- m82 - Availability Heuristic
- m84 - Social Proof
- m91 - Commitment & Consistency Bias
- m96 - Survivorship Bias
- m98 - Confirmation Bias
- And 18 more...

[→ See complete catalog in docs/mental-models-guide.md](../docs/mental-models-guide.md)

## Use Cases

### Software Engineering
- **Code Review**: Apply cognitive bias models to spot blind spots
- **Architecture Decisions**: Use second-order thinking and trade-offs
- **Debugging**: Apply bottlenecks and first-principles
- **System Design**: Use scale, bottlenecks, and margin of safety

### Product & Business
- **Feature Prioritization**: Apply leverage and trade-offs
- **Strategy**: Use competitive models and second-order thinking
- **Risk Assessment**: Apply probabilistic thinking and inversion
- **Market Analysis**: Use supply/demand and bubbles

### Personal Development
- **Career Decisions**: Circle of competence, second-order thinking, trade-offs
- **Learning Strategy**: First-principles, circle of competence
- **Time Management**: Bottlenecks, leverage, diminishing returns
- **Habit Formation**: Activation energy, feedback loops

### Team & Management
- **Hiring**: Cognitive bias detection
- **Conflict Resolution**: Understanding incentives and motivations
- **Communication**: Framing, narrative, audience models
- **Performance**: Feedback loops, incentives

[→ See 27 detailed examples in docs/use-cases.md](../docs/use-cases.md)

## How Mental Models Work

### Single Model Application

```
Problem: "Our deployment pipeline is slow"
Model: Bottlenecks (m32)
Process:
1. Map the process flow
2. Identify the constraint
3. Exploit the bottleneck
4. Subordinate everything else
5. Elevate the bottleneck

Result: Found security scanning is the bottleneck (25 min),
optimized it, pipeline now 15 min
```

### Latticework (Multi-Model) Approach

```
Problem: "Should I leave stable job for startup?"
Models:
- Circle of Competence (m02): Am I ready?
- Second-Order Thinking (m05): Long-term consequences?
- Trade-Offs (m51): What am I giving up?

Result: Synthesis showing how models interconnect:
- COC: 60% ready, will learn rapidly
- SOT: Long-term career aligned with startup path
- Trade-Offs: $200K opportunity cost worth the learning

Recommendation: Accept startup role with conditions
```

The power comes from weaving models together—each reveals different insights, combined they form complete picture.

## Configuration

### Regenerating Model Index

After adding or updating mental model files:

```bash
cd mental-models
python3 generate_index.py
```

This scans all `Mental_Models/` files and updates `.skill/resources/model-index.json`.

### Customization

The skill reads models from `Mental_Models/` directory. To add custom models:

1. Create `.md` file following the template (see existing models)
2. Include: Description, When to Avoid, Keywords, Thinking Steps, Coaching Questions
3. Regenerate index: `python3 generate_index.py`

## Resources

- **Complete Guide**: [docs/mental-models-guide.md](../docs/mental-models-guide.md)
- **Use Cases**: [docs/use-cases.md](../docs/use-cases.md)
- **Quick Reference**: `.skill/resources/quick-reference.md`
- **Examples**: `.skill/examples/` directory

## Troubleshooting

### Skill Not Activating

- Verify `.skill/SKILL.md` exists
- Try explicit command: `/mental-models`
- Check you're in the mental-models directory (for local install)
- For global install, verify symlink: `ls -la ~/.claude/skills/mental-models`

### Models Not Found

- Check `Mental_Models/` directory exists
- Verify model files are `.md` format with proper structure
- Regenerate index: `python3 generate_index.py`
- Check `.skill/resources/model-index.json` was created

### WorkSpace Folders Not Created

- Deep-Analysis mode only creates folders
- Quick-Apply mode doesn't create files (by design)
- Check write permissions in `WorkSpace/` directory
- Folder naming: `YY-MM-DD_HH-MM-SS_<problem_name>`

## Contributing

Contributions welcome! Ways to help:

- Add new mental models
- Contribute use cases
- Improve documentation
- Report bugs or issues
- Suggest new modes or features

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](../LICENSE) for details.

## Changelog

### v1.0.0 (2025-10-31)
- Initial release
- 98 mental models across 8 categories
- 4 operational modes
- Comprehensive documentation
- 27 use case examples
- WorkSpace integration for deep analysis

## Related

- **Farnam Street**: Mental models blog that inspired this skill
- **Poor Charlie's Almanack**: Charlie Munger's essays on mental models
- **Thinking in Systems**: Donella Meadows' book on systems thinking

---

**Ready to think better?** Try your first model:

```
"/mental-models - I need help with [your problem]"
```

Or explore what's available:

```
"What mental models help with [your domain]?"
```
