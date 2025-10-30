# Contributing to Claude Code Skills

Thank you for your interest in contributing! This repository welcomes contributions of new skills, improvements to existing skills, documentation enhancements, and bug fixes.

## Ways to Contribute

### 1. Add a New Skill

Create a new skill for a different domain or use case:

- Review [docs/skill-template.md](./docs/skill-template.md)
- Follow the directory structure pattern
- Include comprehensive documentation
- Provide 3-5 real-world examples
- Test thoroughly before submitting

### 2. Improve Existing Skills

Enhance current skills with:

- New modes or functionality
- Additional examples and use cases
- Performance improvements
- Bug fixes
- Documentation clarifications

### 3. Add Use Cases

Contribute real-world examples to [docs/use-cases.md](./docs/use-cases.md):

- Describe the problem
- List models/skills applied
- Show example invocation
- Explain the outcome

### 4. Documentation

Improve documentation by:

- Fixing typos or unclear explanations
- Adding diagrams or visual aids
- Expanding quick-start guides
- Translating to other languages

### 5. Report Issues

Help us improve by reporting:

- Bugs or unexpected behavior
- Performance issues
- Documentation gaps
- Feature requests

## Getting Started

### Prerequisites

- Git installed
- Claude Code (latest version)
- Python 3 (for mental-models skill)
- Familiarity with Claude Code skills system

### Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-code-skills.git
   cd claude-code-skills
   ```
3. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Adding a New Skill

### Step 1: Create Directory Structure

```bash
mkdir your-skill-name
cd your-skill-name
mkdir -p .skill/resources .skill/examples
```

### Step 2: Write SKILL.md

Create `.skill/SKILL.md` following the template in [docs/skill-template.md](./docs/skill-template.md):

```yaml
---
name: your-skill-name
description: Brief description and trigger keywords
version: 1.0.0
author: Your Name
---

# Skill Name

[Follow template structure]
```

### Step 3: Create README.md

Document your skill in `README.md`:

- Overview and features
- Installation instructions
- Usage examples
- Configuration options
- Troubleshooting

### Step 4: Add Examples

Create at least 3 example files in `.skill/examples/`:

- Show realistic scenarios
- Include both input and expected output
- Cover different modes if applicable

### Step 5: Create Resources

Add supporting files in `.skill/resources/`:

- Index files
- Quick reference guides
- Data files
- Templates

### Step 6: Test Thoroughly

Before submitting:

- [ ] Test all activation patterns
- [ ] Verify all modes work correctly
- [ ] Run examples to ensure they execute
- [ ] Check for conflicts with other skills
- [ ] Validate documentation accuracy

### Step 7: Update Root Documentation

Add your skill to:

- `README.md` (Available Skills section)
- `docs/use-cases.md` (with 2-3 examples)

## Improving Existing Skills

### Mental Models Skill

To add new mental models:

1. Create model file in appropriate `Mental_Models/Mental_Model_[Category]/` directory
2. Follow the structure:
   ```markdown
   ## Mental Model = [Name]

   **Category = [Category]**
   **Description:**
   [Explanation]

   **When to Avoid (or Use with Caution):**
   [Limitations]

   **Keywords for Situations:**
   [Comma-separated keywords]

   **Thinking Steps:**
   1. [Step 1]
   2. [Step 2]
   ...

   **Coaching Questions:**
   - [Question 1]
   - [Question 2]
   ...
   ```
3. Regenerate index:
   ```bash
   cd mental-models
   python3 generate_index.py
   ```
4. Test the new model with Quick-Apply mode

## Code Style

### SKILL.md Files

- Use YAML frontmatter for metadata
- Clear section headers (##)
- Consistent terminology
- Specific activation patterns
- Detailed process steps
- Example outputs in code blocks

### README Files

- Start with one-sentence description
- Include installation instructions
- Provide multiple usage examples
- Document configuration options
- Include troubleshooting section

### Documentation

- Use GitHub-flavored Markdown
- Code blocks with language specifiers
- Relative links to other docs
- Examples in code fences
- Clear, concise language

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature or skill
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat(mental-models): add cognitive bias detection mode

Added new mode that scans for common cognitive biases in decision-making.
Includes 15 bias patterns with detection logic.

Closes #42
```

```
docs(use-cases): add software engineering examples

Added 5 new use cases for code review, debugging, and architecture decisions.

```

```
fix(mental-models): correct path in generate_index.py

Fixed incorrect relative path that broke index regeneration after
repository reorganization.
```

## Pull Request Process

### Before Submitting

1. **Test thoroughly**: Verify all functionality works
2. **Update docs**: Ensure documentation is current
3. **Check examples**: Validate all examples run correctly
4. **Run linters**: Fix any linting issues
5. **Review checklist**: Complete the PR template checklist

### PR Template

When you create a PR, fill out this template:

```markdown
## Description
[Brief description of changes]

## Type of Change
- [ ] New skill
- [ ] Enhancement to existing skill
- [ ] Bug fix
- [ ] Documentation update
- [ ] Other (specify):

## Testing
- [ ] All modes tested
- [ ] Examples verified
- [ ] Documentation reviewed
- [ ] No conflicts with existing skills

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Examples added/updated
- [ ] Tests pass (if applicable)
- [ ] Commit messages follow guidelines
```

### Review Process

1. Maintainers will review within 5 business days
2. Address any requested changes
3. Once approved, maintainers will merge
4. Your contribution will be credited in release notes

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions
- No harassment or discrimination

### Communication

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, general discussion
- **Pull Requests**: Code contributions with context

### Getting Help

- Check existing documentation first
- Search existing issues
- Ask in GitHub Discussions
- Tag maintainers if urgent

## Recognition

Contributors are recognized in:

- README acknowledgments section
- Release notes
- Git commit history
- Contributors page (GitHub)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

- Open an issue with the `question` label
- Start a discussion in GitHub Discussions
- Review existing documentation in `docs/`

---

Thank you for contributing to Claude Code Skills! Your contributions help developers worldwide think better and work smarter.
