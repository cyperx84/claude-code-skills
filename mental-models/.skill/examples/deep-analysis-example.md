# Deep-Analysis Mode Example

## User Request
"/mental-models - Should I stay at my current FAANG company (safe, high pay, boring work) or join a Series A startup (risky, lower pay, exciting mission)?"

## Assistant Process

### Step 1: Problem Diagnosis

Created folder: `WorkSpace/25-10-31_14-30-00_faang_vs_startup_decision/`

**problem_diagnosis.md**:
```
User is facing a career crossroads between stability and growth:

**Current Role (FAANG)**:
- Compensation: $400K total
- Role: Senior Engineer, established product
- Satisfaction: 5/10 - work is predictable but unstimulating
- Learning: Minimal - using existing skills
- Risk: Very low - company is stable

**Startup Opportunity (Series A)**:
- Compensation: $200K + equity (uncertain value)
- Role: Lead Engineer, building from scratch
- Excitement: 9/10 - greenfield project, impactful mission
- Learning: High - new challenges daily
- Risk: High - 50-60% failure rate for Series A

**User Profile**:
- 5 years experience
- Age: 28
- Financial runway: 6 months savings
- Family: Single, no dependents
- Career goal: Eventually start own company
- Risk tolerance: Moderate-high (when younger)
```

### Step 2: Mental Model Selection

**Clarifying Questions** (saved in `questionnaire.md`):
1. What matters more right now: financial security or personal growth?
2. What does your Circle of Competence say - are you ready to lead at a startup?
3. If the startup fails in 18 months, would you regret the experience?

**User Answers**:
1. Growth matters more at this life stage
2. Strong technical skills but limited leadership experience
3. No regrets - the learning would be valuable

**mental_models_selected.md**:
```
From initial scan of 15 candidates, evaluated 6 deeply, selected 3 final models:

1. **m02_circle_of_competence** (Primary)
2. **m05_second-order_thinking** (Secondary)
3. **m51_trade-offs** (Tertiary)

**Rationale**:
- Circle of Competence: User is at career inflection point - need to understand what they know/don't know and how to expand circle
- Second-Order Thinking: This decision has 2-5 year consequences, not just immediate effects
- Trade-Offs: Classic opportunity cost scenario - giving up significant income for growth potential
```

### Step 3: Structured Analysis

**reasoning_m02_circle_of_competence.md** (excerpt):
```
## Thinking Steps Applied:

1. **Define Your Circle**: What do you truly know well?
   - Strong: Backend systems, scaling, code architecture
   - Moderate: Team collaboration, code review
   - Weak: Leadership, hiring, company building, product decisions

2. **Acknowledge the Boundary**: Startup lead role requires:
   - Technical excellence ✓ (inside circle)
   - Team leadership ? (boundary)
   - Strategic product decisions ✗ (outside circle)
   - Hiring/building team ✗ (outside circle)

3. **Expand Deliberately**: Startup is high-stakes learning
   - Pro: Rapid expansion opportunity
   - Con: Learning on hard mode with real consequences
   - Risk: May expand circle too fast and fail

**Insight**: You're 60% ready. The role stretches you but isn't completely outside your circle.
```

**reasoning_m05_second-order_thinking.md** (excerpt):
```
## First-Order Effects:
- FAANG: Keep $400K, stay comfortable, continue boredom
- Startup: Drop to $200K, exciting work, high uncertainty

## Second-Order Effects:
- FAANG path in 2 years: Still $400K, deeper in golden handcuffs, skills atrophy, harder to leave
- Startup path in 2 years (success): $250K + valuable equity, leadership skills, network, career options multiplied
- Startup path in 2 years (failure): Back to job market, but with leadership experience and lessons learned

## Third-Order Effects:
- FAANG path in 5 years: Potentially trapped, watching others build companies, regret not taking risk when young
- Startup path in 5 years: Whether success or failure, you've learned company-building and can apply to own venture

**Key Insight**: The second and third-order effects heavily favor the startup path given your long-term goal of starting your own company.
```

**reasoning_m51_trade-offs.md** (excerpt):
```
## Opportunity Cost Analysis:

**Choosing FAANG** means giving up:
- Leadership development opportunity
- Company-building experience
- Career risk-taking in optimal time window (age 28, no dependents)
- Network in startup ecosystem
- Story/credibility for future ventures

**Choosing Startup** means giving up:
- $200K/year in guaranteed income
- Resume prestige of FAANG tenure
- Low-stress work environment
- Financial security buffer
- Learning from established systems

**Aligning with Priorities**: User's stated goal is "eventually start own company"
- FAANG: Misaligned - doesn't teach company building
- Startup: Aligned - direct apprenticeship in building companies

**The Trade-Off**: $200K/year x 2 years = $400K opportunity cost to learn company building
- Is that tuition worth it? YES, given your goals.
```

### Step 4: Synthesis & Report

**analysis_report.md** (excerpt):

```markdown
# Career Decision Analysis: FAANG vs Startup

## Executive Summary

After analyzing this decision through Circle of Competence, Second-Order Thinking, and Trade-Offs models, the recommendation is: **Join the startup**, with important caveats.

The latticework reveals: (1) You're sufficiently competent but will grow rapidly, (2) Long-term effects strongly favor startup experience, (3) The trade-off is aligned with your goals. Age 28 with no dependents is the optimal risk-taking window.

## Problem Statement

Career crossroads: Safe $400K FAANG role vs. risky $200K startup lead position, evaluated against goal of eventually founding a company.

## Synthesis & Integrated Insights

**How the Models Weave Together**:

Circle of Competence says you're 60% ready - at the boundary but not completely outside. Second-Order Thinking reveals that staying at FAANG has worse long-term consequences despite feeling "safer" now. Trade-Offs confirms the $400K opportunity cost is actually an investment in learning aligned with your goals.

**The Latticework Pattern**:
All three models point in the same direction but for different reasons:
- COC: You're ready enough to learn successfully
- SOT: Time horizon favors growth over security
- Trade-Offs: Sacrifice aligns with priorities

**The Hidden Risk**: The models reveal the REAL risk is NOT the startup failing—it's staying at FAANG and waking up at 35 having never taken the leap, with golden handcuffs tighter and startup ecosystem moved on.

## Actionable Recommendations

### Recommended Path: Join the Startup

**With These Conditions**:
1. Extend financial runway to 12 months before starting
2. Negotiate for more equity if possible (you're cheap at $200K)
3. Set explicit learning goals: hiring, product strategy, fundraising
4. Build relationships with technical advisors for outside-circle challenges
5. Give it 18-24 months as your "startup MBA"

**Decision Rule**: If still excited about mission in 2 weeks, accept. If doubts emerge, that's your gut telling you something.

### Alternative Path: One More Year at FAANG

**Only if**:
- You need to build larger financial safety net
- There's a specific skill gap to fill first
- Startup opportunity will still exist in 12 months

## References

- Series A failure rates: Approximately 50-60% fail to reach Series B
- FAANG compensation data: levels.fyi
- Career risk-taking research: Optimal window is late 20s before family commitments
```

**Total Files Created**: 6 files in WorkSpace folder
**Execution Time**: 12 minutes

---

## Key Characteristics of Deep-Analysis Mode

1. **Multiple models** working together (max 3)
2. **Thinking Steps followed exactly** from each model
3. **Synthesis section** shows how models interconnect
4. **Evidence-based** with external data
5. **Actionable recommendations** not just analysis
6. **WorkSpace folder** preserves analysis for future reference
