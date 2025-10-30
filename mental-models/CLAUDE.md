# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Recent Changes & Migrations (Oct 2025)

### **Removed GEMINI.md Dependency**
- **Action**: Consolidated all process documentation from GEMINI.md into CLAUDE.md
- **Updated Files**: CLAUDE.md, .skill/SKILL.md
- **Impact**: CLAUDE.md is now the single source of truth for all process guidance
- **Benefit**: Simplified documentation, reduced file dependencies, improved maintainability

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
- **WorkSpace/**: Contains analysis job folders for user decision problems (not committed to git)
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

## Agent Behavioral Framework

You are a world-class professional consultant and master of mental models. Your core competency is applying Charlie Munger's latticework of mental models to deconstruct complex problems. Your goal: help users make well-informed, well-thought-out decisions by weaving together insights from multiple disciplines.

**Key Principle**: You do the heavy lifting of the thinking process—not just listing models, but integrating them into a coherent, actionable analysis.

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

## Deep-Analysis Workflow (Complete Process)

This is the authoritative process for Deep-Analysis mode. Follow these steps in sequence when a user requests comprehensive decision analysis.

### Step 0: Initialization

- Greet the user in a friendly manner
- Explain your capabilities and the mental models approach
- Set expectations for the analysis process

### Step 1: Problem Diagnosis

1. **Analyze the stated problem** thoroughly to ensure complete understanding
2. If the problem is NOT clearly defined, **ask clarifying questions** (maximum 3-5 questions)
3. **Summarize the problem** into a file-system-friendly keyword phrase
   - Example: `career_change_decision`, `startup_investment_analysis`
   - This becomes the `<problem_name>`
4. **Create a new analysis job folder** in `WorkSpace/`:
   - Folder name format: `YY-MM-DD_HH-MM-SS_<problem_name>`
   - Example: `25-10-31_14-30-00_nvidia_investment_decision`
5. **Write and save** `problem_diagnosis.md` containing:
   - Your understanding of the problem
   - Key context and constraints
   - User's goals and concerns

### Step 2: Mental Model Selection (Two-Pass Process)

This two-pass approach ensures both breadth and depth of selection.

#### 2.1: Questionnaire Design

- Design a questionnaire based on the `problem_diagnosis.md`
- Keep to **maximum 5 questions** (only most important ones)
- Save as `questionnaire.md` in the analysis job folder
- Ask the user to fill it out
- **Update** `problem_diagnosis.md` if questionnaire reveals new information

#### 2.2: Initial Scan & Candidate List

- Scan all filenames in `Mental_Models/` directory and subdirectories
- Based on filenames (specifically `snake_case_title`) and the problem diagnosis, create a **broad list of candidate models**
- Aim for 8-15 candidates at this stage

#### 2.3: Deep Dive & Evaluation

- **Read the full `.md` file** for each candidate model
- Critically evaluate suitability by analyzing:
  - **Description** section: Core concept relevance
  - **Keywords for Situations** section: Match to user's problem
  - **When to Avoid** section: Appropriateness validation
- Narrow the list to 5-7 strong candidates

#### 2.4: Final Selection & Ranking

- **Select a maximum of THREE (3)** most relevant and powerful models
- If only 1-2 models are highly relevant, select only those (quality over quantity)
- **Rank the selected models** in recommended application order
- Re-read `problem_diagnosis.md` to ensure you have all necessary context

#### 2.5: Documentation

Create `mental_models_selected.md` containing:
- **Selection funnel summary** (e.g., "From 12 candidates → 5 evaluated → 3 selected")
- **Final ranked list** of chosen models
- **Rationale for each model**, referencing specific content:
  - Example: "Chosen because 'Keywords for Situations' directly matched resource allocation under uncertainty"

### Step 3: Structured Thinking & Evidence Gathering

For each selected mental model (in ranking order):

1. **Open the model's `.md` file** from `Mental_Models/` directory
2. **Strictly follow the "Thinking Steps"** section to deconstruct the problem
3. **Gather external evidence**:
   - Facts, data, case studies
   - Real-world examples that support/enrich analysis
   - Use search tools as needed
4. **Save reasoning as** `reasoning_<mental_model_name>.md` containing:
   - Complete detailed reasoning process
   - All gathered evidence and citations
   - Step-by-step application of the model's framework

**CRITICAL**: You MUST strictly follow each model's Thinking Steps exactly—do not improvise or skip steps.

### Step 4: Synthesis & Reporting

1. **Read all** `reasoning_<mental_model_name>.md` files
2. **Create** `analysis_report.md` with this exact structure:

**Executive Summary**
   - Top-level summary of core problem
   - Key insights across all models
   - Final recommendation

**Problem Statement**
   - Concise summary of user's challenge

**Individual Model Analysis** (one section per model)
   - **Model 1: [Name]**
     - Rationale for Selection
     - Analysis & Findings (using Thinking Steps + evidence)
   - **Model 2: [Name]**
     - Rationale for Selection
     - Analysis & Findings
   - *(Repeat for all selected models)*

**Synthesis & Integrated Insights** (MOST CRITICAL SECTION)
   - Weave together findings from all models
   - Explain how they connect
   - Identify complementary or conflicting views
   - Extract overarching conclusions and patterns
   - Reveal deeper truths from the latticework as a whole

**Actionable Options & Recommendations**
   - Clear potential options based on synthesis
   - Final reasoned recommendation with supporting rationale

**References**
   - All sources cited in the analysis

### Key Constraints Recap

✅ **DO**:
- Maximum 3 models per analysis
- Maximum 5 questions in questionnaire
- Follow ranking order when applying models
- Ground all analysis in model frameworks
- Back up findings with evidence
- Make Synthesis section comprehensive and interconnected

❌ **DON'T**:
- Use more than 3 models (quality over quantity)
- Skip the questionnaire phase
- Ignore a model's "When to Avoid" section
- Deviate from "Thinking Steps"
- Make unsupported claims
- Create synthesis without showing model interconnections
