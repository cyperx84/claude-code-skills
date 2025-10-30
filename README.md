# Claude Code Skills Collection

A curated collection of Claude Code skills designed to enhance your workflow with structured thinking frameworks, cognitive tools, and domain expertise.

## Overview

This repository contains production-ready Claude Code skills that you can use to augment your development workflow, decision-making, and problem-solving capabilities. Each skill is battle-tested, well-documented, and includes comprehensive examples.

## Available Skills

### 🧠 Mental Models (v1.0.0)

Apply Charlie Munger's "latticework of mental models" to any problem using 98 cognitive frameworks from multiple disciplines.

**What it does**:
- **Quick-Apply Mode** (1-2 min): Instantly apply a specific model to your current context
- **Deep-Analysis Mode** (10-15 min): Comprehensive multi-model analysis with full synthesis
- **Discovery Mode** (30 sec): Search and browse 98 models by keywords
- **Interactive Mode** (2-3 min): Guided model selection through Q&A

**Use cases**:
- Code architecture decisions
- Product strategy and prioritization
- Career and personal decisions
- Team dynamics and management
- Bias detection and risk assessment

**[→ View Mental Models Documentation](./mental-models/)**

## Quick Start

### Installation

Clone this repository:
```bash
git clone https://github.com/cyperx84/claude-code-skills.git
cd claude-code-skills
```

### Using a Skill

#### Option 1: Local (Project-Specific)

Use skills directly from the repository when working in this directory. Claude Code will automatically detect skills in `.skill/` directories.

```bash
cd mental-models
# Skill is now available in this context
```

#### Option 2: Global Installation

Make a skill available across all projects by symlinking to your global Claude Code skills directory:

```bash
# Install mental-models globally
ln -s $(pwd)/mental-models/.skill ~/.claude/skills/mental-models

# Or copy instead of symlink
cp -r mental-models/.skill ~/.claude/skills/mental-models
```

### Example Usage

```
# Mental Models skill
"Apply bottlenecks model to our CI/CD pipeline"

"/mental-models - Should I accept this job offer?"

"What mental models help with scaling systems?"
```

## Repository Structure

```
claude-code-skills/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
├── docs/                        # Cross-skill documentation
│   ├── use-cases.md            # Real-world applications catalog
│   ├── skill-template.md       # Template for creating new skills
│   └── mental-models-guide.md  # Deep dive guide
├── .github/                     # GitHub templates
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
└── mental-models/               # Mental models skill
    ├── README.md
    ├── .skill/                  # Skill definition
    ├── Mental_Models/           # 98 model files
    ├── WorkSpace/               # Analysis artifacts
    └── ...
```

## Documentation

- **[Use Cases](./docs/use-cases.md)**: 27 real-world examples across domains
- **[Skill Template](./docs/skill-template.md)**: Guide for creating new skills
- **[Mental Models Guide](./docs/mental-models-guide.md)**: Comprehensive mental models documentation

## Creating Your Own Skills

Want to create a new skill? We've made it easy:

1. **Read the template**: Check out [docs/skill-template.md](./docs/skill-template.md)
2. **Create directory structure**: Use the template as guide
3. **Write SKILL.md**: Define your skill's behavior
4. **Add examples**: Show real usage patterns
5. **Document thoroughly**: README with installation and usage
6. **Test**: Verify all modes work correctly
7. **Submit PR**: Share with the community!

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

## Features

### Why Use These Skills?

- **Production-Ready**: Battle-tested in real workflows
- **Well-Documented**: Comprehensive guides and examples
- **Multiple Modes**: Quick application and deep analysis
- **Context-Aware**: Works with code, decisions, planning, any workflow
- **Extensible**: Easy to create new skills using templates

### Design Philosophy

1. **Quick + Deep**: Support both rapid insights and comprehensive analysis
2. **Discoverable**: Easy to find relevant tools for your problem
3. **Structured**: Systematic frameworks, not ad-hoc advice
4. **Evidence-Based**: Grounded in data and real-world examples
5. **Latticework**: Multiple perspectives reveal deeper insights

## Use Cases

Skills in this collection have been used for:

- **Software Engineering**: Architecture decisions, debugging, code review, system design
- **Product Management**: Feature prioritization, roadmap planning, competitive analysis
- **Business Strategy**: Market entry, pricing, resource allocation, risk assessment
- **Personal Development**: Career decisions, learning strategy, habit formation
- **Team Management**: Hiring, conflict resolution, performance feedback
- **Content Creation**: Writing structure, argumentation, technical documentation

[→ See 27 detailed use cases](./docs/use-cases.md)

## Requirements

- **Claude Code**: Latest version recommended
- **Git**: For cloning and updates
- **Python 3**: (Optional) For mental-models index regeneration

## Contributing

Contributions welcome! We're especially interested in:

- New skills for different domains
- Additional use cases and examples
- Improvements to existing skills
- Bug reports and fixes
- Documentation enhancements

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## Roadmap

### Planned Skills

- **Code Review Assistant**: Structured code review with bias detection
- **Architecture Patterns**: Design pattern recommendations with trade-off analysis
- **Learning Path Generator**: Personalized learning roadmaps based on goals
- **Decision Journal**: Track decisions and outcomes over time
- **Bias Detector**: Real-time cognitive bias identification

Want to help build these? Check out [CONTRIBUTING.md](./CONTRIBUTING.md)!

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/cyperx84/claude-code-skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cyperx84/claude-code-skills/discussions)
- **Documentation**: [docs/](./docs/)

## Acknowledgments

- **Mental Models**: Inspired by Charlie Munger's latticework approach and Farnam Street's work
- **Claude Code**: Built for Anthropic's Claude Code tool

## Changelog

### v1.0.0 (2025-10-31)
- Initial release with Mental Models skill
- 98 cognitive frameworks across 8 categories
- 4 operational modes (Quick-Apply, Deep-Analysis, Discovery, Interactive)
- Comprehensive documentation and 27 use cases
- Skill creation template and guidelines

---

**Start thinking better today.** Choose a skill above and enhance your workflow.
