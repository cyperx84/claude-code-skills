# Claude Code Skill Template

Use this template when creating new skills for this repository.

## Directory Structure

```
your-skill-name/
├── README.md                    # Skill documentation
├── .skill/
│   ├── SKILL.md                # Main skill definition
│   ├── resources/              # Supporting files
│   │   └── [resource files]
│   └── examples/               # Usage examples
│       └── [example files]
├── [skill-specific files]      # Your skill's data/code
└── [supporting directories]    # Any additional structure
```

## SKILL.md Template

```markdown
---
name: your-skill-name
description: Brief description of what this skill does and when to use it. Include trigger keywords and example invocations.
version: 1.0.0
author: Your Name
---

# Skill Name

## Purpose

[Detailed explanation of what this skill does and why it's useful]

## When to Activate

Activate this skill when the user:
- [Trigger condition 1]
- [Trigger condition 2]
- [Trigger condition 3]
- Uses specific keywords: "keyword1", "keyword2"
- Types slash command: `/your-skill-name`

## Core Functionality

### Mode 1: [Mode Name]

**Purpose**: [What this mode does]

**When**: [When to use this mode]

**Process**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Output Format**:
```
[Show example output structure]
```

**Execution Time**: [Estimated time]
**Files Created**: [What files, if any]

### Mode 2: [Mode Name]

[Repeat structure for each mode]

## Examples

### Example 1: [Scenario Name]
```
User: "[Example user request]"
Assistant: [How skill responds]
```

### Example 2: [Scenario Name]
```
User: "[Example user request]"
Assistant: [How skill responds]
```

## Configuration

[Any configuration options, paths, or setup required]

## Important Guidelines

1. [Guideline 1]
2. [Guideline 2]
3. [Guideline 3]

## Error Handling

[How the skill handles common errors or edge cases]

## Maintenance

[Instructions for updating or maintaining the skill]

## Success Criteria

User successfully uses this skill when:
- [Success criterion 1]
- [Success criterion 2]
- [Success criterion 3]
```

## README.md Template

```markdown
# Skill Name

Brief one-sentence description of what this skill does.

## Overview

[2-3 paragraph explanation of the skill's purpose, capabilities, and value proposition]

## Features

- Feature 1
- Feature 2
- Feature 3
- Feature 4

## Installation

### Local Installation (Project-Specific)

Keep skill in project directory:
```bash
git clone https://github.com/yourusername/claude-code-skills.git
cd claude-code-skills/your-skill-name
```

The skill will be available when working in this directory.

### Global Installation

Make skill available across all projects:
```bash
# Copy skill to global Claude Code skills directory
cp -r .skill ~/.claude/skills/your-skill-name

# Or create symlink
ln -s $(pwd)/.skill ~/.claude/skills/your-skill-name
```

## Usage

### Quick Start

```
[Example invocation]
```

### Activation Patterns

The skill activates when you:
- Use `/your-skill-name` command
- Say "[trigger phrase 1]", "[trigger phrase 2]"
- Mention "[keyword 1]", "[keyword 2]"

### Modes

#### Mode 1: [Name]
[Brief description and example]

#### Mode 2: [Name]
[Brief description and example]

## Examples

### Example 1: [Scenario]
**Input:**
```
[User input]
```

**Output:**
```
[Skill output]
```

### Example 2: [Scenario]
[Repeat for each example]

## Configuration

[Any configuration steps needed]

## Resources

[Links to additional documentation, data sources, or related materials]

## Contributing

Contributions welcome! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

[License information - should match repository license]

## Changelog

### v1.0.0
- Initial release
- [List of features]

## Related Skills

- [Link to related skill 1]
- [Link to related skill 2]

## Support

For issues or questions:
- Open an issue: [GitHub Issues URL]
- Check documentation: [docs/ directory]
```

## Checklist for New Skills

Before submitting a new skill, ensure:

### Documentation
- [ ] SKILL.md follows template structure
- [ ] README.md is comprehensive and clear
- [ ] Examples provided for all major modes
- [ ] Use cases documented
- [ ] Installation instructions included

### Code Quality
- [ ] Skill activates correctly on trigger keywords
- [ ] Error handling implemented
- [ ] Edge cases considered
- [ ] Performance acceptable (< 30s for most operations)

### Testing
- [ ] Tested all activation patterns
- [ ] Verified all modes work correctly
- [ ] Examples run successfully
- [ ] Conflicts with other skills checked

### Resources
- [ ] All external resources documented
- [ ] File paths use absolute or relative paths correctly
- [ ] Dependencies listed
- [ ] Resource files included or linked

### Integration
- [ ] Added to main repository README
- [ ] Use cases added to docs/use-cases.md
- [ ] CONTRIBUTING.md guidelines followed
- [ ] Git commit follows conventions

## File Naming Conventions

- **Skill name**: lowercase-with-hyphens (e.g., `mental-models`, `code-reviewer`)
- **SKILL.md**: Always `SKILL.md` (uppercase)
- **README.md**: Always `README.md` (uppercase)
- **Resource files**: lowercase-with-hyphens.extension
- **Example files**: descriptive-name-example.md

## Skill Design Best Practices

1. **Clear Activation**: Make it obvious when skill should activate
2. **Multiple Modes**: Support both quick and deep workflows
3. **Examples**: Provide at least 3-5 realistic examples
4. **Documentation**: Over-document rather than under-document
5. **Error Handling**: Graceful failures with helpful messages
6. **Performance**: Fast for common operations
7. **Discoverability**: Use keywords users naturally think of
8. **Modularity**: Keep skills focused on specific domain
9. **Resource Management**: Document all external dependencies
10. **Versioning**: Use semantic versioning for updates

## Common Patterns

### Pattern 1: Quick vs Deep Modes
Many skills benefit from:
- **Quick Mode**: Fast, inline responses (1-2 min)
- **Deep Mode**: Comprehensive analysis with file creation (10-15 min)

### Pattern 2: Discovery + Application
Useful pattern:
- **Discovery Mode**: Search/browse available options
- **Application Mode**: Apply selected option

### Pattern 3: Interactive Guidance
For complex domains:
- **Interactive Mode**: Ask clarifying questions
- **Guided Mode**: Step-by-step assistance

## Resources for Skill Development

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Existing Skills](../) - Browse this repository for examples
- [Use Cases](./use-cases.md) - Real-world applications
- [Mental Models Guide](./mental-models-guide.md) - Example of comprehensive skill

## Getting Help

- Check existing skills for patterns to follow
- Review use-cases.md for application examples
- Open an issue if you have questions
- Join discussions in repository issues/discussions

---

Ready to create your skill? Start with:
1. Create directory structure
2. Write SKILL.md following template
3. Create README.md with documentation
4. Add examples showing usage
5. Test thoroughly
6. Submit PR with all checklist items completed
