# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a mental models knowledge repository containing structured documentation of cognitive frameworks and decision-making tools. The repository operates as an AI-assisted decision analysis system that helps users make well-informed decisions by applying Charlie Munger's "latticework of mental models" approach.

## Repository Structure

- **Mental_Models/**: Mental model files organized by category in subfolders (98 models total)
  - Mental_Model_General/ (9 models: m01-m09)
  - Mental_Model_Science/ (20 models: m10-m29)
  - Mental_Model_SysThinking/ (11 models: m30-m40)
  - Mental_Model_Math/ (7 models: m41-m47)
  - Mental_Model_Economics/ (12 models: m48-m59)
  - Mental_Model_Art/ (11 models: m60-m70)
  - Mental_Model_War/ (5 models: m71-m75)
  - Mental_Model_HumanNature/ (23 models: m76-m98)
- **WorkSpace/**: Contains analysis job folders for user decision problems
- **Additional_Info/**: Supporting documentation including agent process modes
- **.skill/**: Mental models skill system for Claude Code integration
  - SKILL.md - Main skill definition with 4 modes
  - resources/model-index.json - Searchable index of all 98 models
  - resources/quick-reference.md - Common patterns and quick lookups
  - examples/ - Sample invocations for each mode

## Mental Model File Conventions

Mental model files follow the naming pattern: `m##_snake_case_title.md` where ## is a zero-padded number.

Each mental model file follows this standardized structure:
- **Description**: Core concept explanation
- **When to Avoid (or Use with Caution)**: Limitations and warnings
- **Keywords for Situations**: Potential application contexts
- **Thinking Steps**: Step-by-step reasoning framework
- **Coaching Questions**: Prompts for applying the model

## Analysis Job Workflow

When creating an analysis job in WorkSpace/:

1. **Folder Naming**: Use format `YY-MM-DD_HH-MM-SS_<problem_name>`
   - Example: `25-07-18_16-30-00_nvidia_investment_decision`

2. **Required Files Structure**:
   - `problem_diagnosis.md` - Understanding of the user's problem
   - `questionnaire.md` - Information gathering questions (max 5)
   - `mental_models_selected.md` - Selection process and rationale
   - `reasoning_<mental_model_name>.md` - One file per applied model
   - `analysis_report.md` - Final synthesized analysis

3. **Mental Model Selection Process**:
   - First scan Mental_Models/ directory filenames to create candidate list
   - Read full .md files for deep evaluation
   - Select maximum of 3 most relevant models
   - Document selection funnel and rationale

4. **Analysis Report Structure**:
   - Executive Summary
   - Problem Statement
   - Individual Model Analysis (one section per model)
   - Synthesis & Integrated Insights (critical section showing interconnections)
   - Actionable Options & Recommendations
   - References

## Working with Mental Models

When reading mental model files:
- Focus on the "Thinking Steps" section for structured application
- Check "When to Avoid" to validate appropriateness
- Use "Keywords for Situations" to match to user's context
- Reference "Coaching Questions" for user engagement

## Important Constraints

- Maximum 3 mental models per analysis (quality over quantity)
- Maximum 5 questions in questionnaire
- Must follow ranking order when applying multiple models
- All analysis must be evidence-based and grounded in model frameworks

## Process Modes

The repository includes two process documentation files:
- `Additional_Info/agent-process-deep-mode.md` - Comprehensive analysis workflow
- `Additional_Info/agent-process-quick-mode.md` - Streamlined analysis workflow

Reference GEMINI.md for the complete agent process definition and behavioral guidelines.

## Mental Models Skill System

This repository includes a Claude Code skill that makes mental models accessible during any workflow.

### Skill Location
The skill is stored in this repository at `.skill/SKILL.md` rather than in the global `~/.claude/skills/` directory.

### Activation Patterns
The skill activates when users:
- Use `/mental-models` command
- Say "help me think", "apply mental model", "what mental models..."
- Mention specific model names (e.g., "second-order thinking", "inversion")
- Request decision analysis or cognitive frameworks

### Four Modes

1. **Quick-Apply Mode** (1-2 min)
   - Instantly apply a specific model to current context
   - Example: "Apply bottlenecks to our CI/CD pipeline"
   - No files created, inline response

2. **Deep-Analysis Mode** (10-15 min)
   - Comprehensive analysis using max 3 models
   - Creates WorkSpace folder with full synthesis
   - Modernized workflow from GEMINI.md
   - Example: "/mental-models - Should I switch careers?"

3. **Discovery Mode** (30 sec)
   - Search and browse models by keywords or categories
   - Example: "What mental models apply to scaling systems?"
   - Returns 5-7 relevant matches with rationale

4. **Interactive Mode** (2-3 min + user input)
   - Guided selection through clarifying questions
   - Example: "Which mental model should I use?"
   - Recommends 3-5 models with reasoning

### Key Resources

- **model-index.json**: Searchable index of all 98 models with metadata
- **quick-reference.md**: Common problem patterns → recommended models
- **examples/**: Sample invocations showing each mode in action

### Regenerating Index

After adding or updating mental model files, regenerate the index:
```bash
python3 generate_index.py
```

This scans all Mental_Models/ files and updates `.skill/resources/model-index.json`.
