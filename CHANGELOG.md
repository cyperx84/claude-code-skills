# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-31

### Added

**Mental Models Skill (Initial Release)**
- 98 mental models across 8 categories:
  - General Thinking Tools (9 models: m01-m09)
  - Science (20 models: m10-m29)
  - Systems Thinking (11 models: m30-m40)
  - Mathematics (7 models: m41-m47)
  - Economics (12 models: m48-m59)
  - Art (11 models: m60-m70)
  - Warfare & Strategy (5 models: m71-m75)
  - Human Nature & Judgment (23 models: m76-m98)

**Skill Features**
- 4 operational modes:
  - Quick-Apply Mode (1-2 min): Instant model application
  - Deep-Analysis Mode (10-15 min): Comprehensive multi-model analysis
  - Discovery Mode (30 sec): Search and browse by keywords
  - Interactive Mode (2-3 min): Guided model selection
- Searchable model index (.skill/resources/model-index.json)
- Quick reference guide for common patterns
- 4 detailed example files showing each mode

**Documentation**
- Comprehensive README with quick start guide
- Mental models skill README with full documentation
- docs/use-cases.md: 27 real-world examples across domains
- docs/skill-template.md: Template for creating new skills
- docs/mental-models-guide.md: Complete guide to all 98 models
- CONTRIBUTING.md: Contribution guidelines
- LICENSE: MIT License

**Repository Infrastructure**
- GitHub issue templates (bug report, feature request, new skill proposal)
- Pull request template
- .gitignore configured for Python and GitHub
- Multi-skill repository structure
- WorkSpace integration for deep analysis

**Tools**
- generate_index.py: Regenerate model index from Mental_Models/

### Technical Details

- Repository structure supports multiple skills (extensible)
- Skills stored in subdirectories with .skill/ folders
- Model files follow standardized template structure
- Git history preserved for all 98 models
- WorkSpace folders excluded from version control (may contain sensitive user data)

---

## Future Releases

### Planned Features
- [ ] Code Review Assistant skill
- [ ] Architecture Patterns skill
- [ ] Learning Path Generator skill
- [ ] Decision Journal skill
- [ ] Bias Detector skill

### Improvements Under Consideration
- [ ] Global vs. local skill installation documentation
- [ ] Video tutorials for each mode
- [ ] Community-contributed mental models
- [ ] Integration with other AI tools
- [ ] Mobile-friendly documentation

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on:
- Adding new skills
- Contributing use cases
- Improving documentation
- Reporting bugs

## Links

- [Repository](https://github.com/YOUR_USERNAME/claude-code-skills)
- [Issues](https://github.com/YOUR_USERNAME/claude-code-skills/issues)
- [Discussions](https://github.com/YOUR_USERNAME/claude-code-skills/discussions)
