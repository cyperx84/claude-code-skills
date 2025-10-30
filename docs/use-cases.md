# Mental Models Skill: Use Cases & Applications

This document catalogs real-world use cases for the mental-models Claude Code skill across different domains. Each use case shows how to apply mental models to solve practical problems.

## Table of Contents

- [Software Engineering](#software-engineering)
- [Product & Business Strategy](#product--business-strategy)
- [Personal Development](#personal-development)
- [Team & Management](#team--management)
- [Content Creation & Communication](#content-creation--communication)
- [Financial & Investment Decisions](#financial--investment-decisions)
- [Learning & Education](#learning--education)

---

## Software Engineering

### 1. Code Review with Cognitive Bias Detection

**Problem**: Code reviews often suffer from confirmation bias, anchoring to first impressions, and availability heuristic (over-weighting recent bugs).

**Mental Models to Apply**:
- m98_confirmation_bias - Actively seek reasons the code might fail
- m88_first-conclusion_bias - Don't stop at first issue found
- m82_availability_heuristic - Don't over-react to recent incidents

**Example Invocation**:
```
"Apply confirmation bias model to this pull request review.
I think the code looks good but want to ensure I'm not missing issues."
```

**Outcome**: More thorough reviews, fewer bugs in production

---

### 2. Architecture Decision: Microservices vs Monolith

**Problem**: Team debating whether to break monolith into microservices. High stakes, long-term impact, multiple trade-offs.

**Mental Models to Apply**:
- m05_second-order_thinking - What happens after we migrate?
- m51_trade-offs - What do we gain vs give up?
- m07_inversion - What would make this migration catastrophic?

**Example Invocation**:
```
"/mental-models - Should we migrate from monolith to microservices?
We have 8 engineers, 50K users, growing fast, but team is split on approach."
```

**Outcome**: Deep-analysis mode creates WorkSpace folder with comprehensive evaluation, synthesis of 3 models, actionable recommendation

---

### 3. Debugging a Production Incident

**Problem**: Service is down, team scrambling. Need structured thinking under pressure.

**Mental Models to Apply**:
- m32_bottlenecks - Where is the constraint causing failure?
- m44_multiply_by_zero - Single point of failure took down everything?
- m01_map_is_not_the_territory - Don't trust dashboards, check actual systems

**Example Invocation**:
```
"Quick-apply bottlenecks model to our production outage.
API latency spiked from 100ms to 10s, database CPU at 100%."
```

**Outcome**: Rapid identification of constraint, structured incident response

---

### 4. API Design Review

**Problem**: Designing public API that will be hard to change once released. Need to consider long-term implications.

**Mental Models to Apply**:
- m46_surface_area - More endpoints = more maintenance burden
- m34_margin_of_safety - Design for misuse and edge cases
- m05_second-order_thinking - How will this API evolve over time?

**Example Invocation**:
```
"Apply surface area and margin of safety to this API design"
[paste API spec]
```

**Outcome**: Simpler API with fewer endpoints, better error handling, versioning strategy

---

### 5. Technical Debt Prioritization

**Problem**: 50 items in tech debt backlog. Limited engineering time. Which to tackle first?

**Mental Models to Apply**:
- m21_leverage - Which fixes give biggest impact for least effort?
- m51_trade-offs - Opportunity cost of fixing X vs building feature Y
- m40_law_of_diminishing_returns - When to stop refactoring?

**Example Invocation**:
```
"What mental models help prioritize technical debt?"
[Discovery mode suggests leverage, trade-offs, bottlenecks]
"Apply leverage model to our tech debt backlog"
```

**Outcome**: Clear prioritization framework, focus on high-leverage improvements

---

### 6. System Design Interview Preparation

**Problem**: Preparing for system design interview. Need structured thinking frameworks.

**Mental Models to Apply**:
- m32_bottlenecks - Identify system constraints
- m33_scale - How does system behave at 10x, 100x, 1000x?
- m34_margin_of_safety - Build redundancy and fault tolerance
- m30_feedback_loops - Auto-scaling and circuit breakers

**Example Invocation**:
```
"Apply scale and bottlenecks models to designing Instagram-like photo sharing service for 100M users"
```

**Outcome**: Structured approach to system design, demonstrates deep thinking

---

## Product & Business Strategy

### 7. Feature Prioritization for Product Roadmap

**Problem**: 20 feature requests, limited eng resources. Stakeholders pushing different priorities.

**Mental Models to Apply**:
- m51_trade-offs - Choosing X means not choosing Y
- m21_leverage - Which features multiply value?
- m37_critical_mass - What's the minimum set to reach tipping point?

**Example Invocation**:
```
"/mental-models - Help me prioritize our Q1 product roadmap.
We have 20 features requested but can only build 5-7 this quarter."
```

**Outcome**: Data-driven roadmap, clear rationale for stakeholders, focus on leverage

---

### 8. Pricing Strategy for SaaS Product

**Problem**: Launching new pricing tier. Unsure how to price without leaving money on table or scaring customers.

**Mental Models to Apply**:
- m49_supply_and_demand - Market dynamics
- m84_social_proof - How do customers anchor to competitors?
- m63_framing - $99/month vs $3.30/day perception

**Example Invocation**:
```
"Apply supply and demand + framing models to our SaaS pricing strategy"
```

**Outcome**: Pricing tiers that balance growth and revenue, effective positioning

---

### 9. Market Entry Strategy

**Problem**: Evaluating whether to enter new geographic market. High investment, uncertain returns.

**Mental Models to Apply**:
- m02_circle_of_competence - Do we understand this market?
- m07_inversion - What would make this expansion fail?
- m06_probabilistic_thinking - What's the actual likelihood of success?

**Example Invocation**:
```
"/mental-models - Should we expand to European market?
Current revenue $10M/year in US, EU market 2x size but different regulations."
```

**Outcome**: Risk assessment, go/no-go decision framework, mitigation strategies

---

### 10. Competitive Analysis

**Problem**: New competitor launched similar product at half our price. Team panicking.

**Mental Models to Apply**:
- m72_asymmetric_warfare - Compete on different dimensions
- m22_niches - Find underserved segments
- m05_second-order_thinking - Can they sustain low pricing?

**Example Invocation**:
```
"Apply asymmetric warfare model to competitor threat.
They launched at $49/mo vs our $99/mo, but no customer support."
```

**Outcome**: Strategy to compete on service/quality, not price. Focus on high-value customers.

---

### 11. Product-Market Fit Assessment

**Problem**: Launched MVP, some traction but unclear if we have PMF. Should we double down or pivot?

**Mental Models to Apply**:
- m30_feedback_loops - Are users coming back organically?
- m37_critical_mass - Are we approaching tipping point?
- m96_survivorship_bias - Are we over-indexing on vocal happy customers?

**Example Invocation**:
```
"Apply feedback loops and survivorship bias to evaluate our product-market fit.
20% of users return weekly, NPS is 40, churn is 8%/month."
```

**Outcome**: Honest assessment of PMF status, data to guide pivot/persevere decision

---

## Personal Development

### 12. Career Change Decision

**Problem**: Offered promotion at current company vs. job at startup. Life-changing decision with long-term consequences.

**Mental Models to Apply**:
- m02_circle_of_competence - Am I ready for this challenge?
- m05_second-order_thinking - Where does each path lead in 3-5 years?
- m51_trade-offs - What's the opportunity cost?

**Example Invocation**:
```
"/mental-models - Promotion to VP at FAANG ($500K) vs. Head of Eng at Series B startup ($250K + equity). Age 32, no dependents."
```

**Outcome**: Deep-analysis with WorkSpace folder, comprehensive evaluation of both paths, aligned with long-term goals

---

### 13. Learning a New Technical Skill

**Problem**: Want to learn Rust, but limited time. Should I commit or focus on deepening Python expertise?

**Mental Models to Apply**:
- m02_circle_of_competence - Expand strategically vs randomly
- m51_trade-offs - Time spent on Rust = time not spent on Python
- m21_leverage - Which skill multiplies my value more?

**Example Invocation**:
```
"Apply circle of competence and leverage to learning Rust vs deepening Python.
I'm a senior backend engineer, Python expert, work in ML/data space."
```

**Outcome**: Strategic learning plan, focus on high-leverage skill development

---

### 14. Time Management & Productivity

**Problem**: Always busy but not making progress on important projects. Feeling overwhelmed.

**Mental Models to Apply**:
- m32_bottlenecks - What's limiting my output?
- m21_leverage - Which activities give 10x return?
- m40_law_of_diminishing_returns - When to stop optimizing?

**Example Invocation**:
```
"Apply bottlenecks model to my time management.
I work 10hr/day but only 2hrs feel productive. Lots of meetings, emails, slack."
```

**Outcome**: Identify time bottlenecks (meetings), eliminate low-leverage activities, batching strategy

---

### 15. Building Better Habits

**Problem**: Want to exercise regularly but keep falling off after 2-3 weeks.

**Mental Models to Apply**:
- m10_activation-energy - Reduce friction to start
- m30_feedback_loops - Create positive reinforcement
- m91_commitment_and_consistency_bias - Use small commitments

**Example Invocation**:
```
"Apply activation energy and feedback loops to building exercise habit"
```

**Outcome**: Strategies to reduce startup friction (gym clothes ready), create feedback (tracking app), tiny commitments (just 10 min)

---

### 16. Financial Planning & Budgeting

**Problem**: Not sure how to allocate income between savings, investments, and lifestyle spending.

**Mental Models to Apply**:
- m34_margin_of_safety - Emergency fund is financial margin
- m51_trade-offs - Spending now vs future wealth
- m55_debt - Understand leverage and compounding

**Example Invocation**:
```
"Apply margin of safety and trade-offs to personal budgeting.
Income $150K, expenses $80K, no debt, $20K saved."
```

**Outcome**: Budget framework with emergency fund, investment allocation, conscious trade-off decisions

---

## Team & Management

### 17. Hiring Decision

**Problem**: Two strong candidates for senior role. Different strengths, hard to choose.

**Mental Models to Apply**:
- m80_liking/disliking_tendency - Don't hire based on personality fit alone
- m94_fundamental_attribution_error - Situational vs dispositional traits
- m07_inversion - What would make this hire a disaster?

**Example Invocation**:
```
"Apply cognitive bias models to hiring decision between two candidates"
[describe candidates]
```

**Outcome**: Structured evaluation, awareness of biases, focus on job requirements

---

### 18. Team Conflict Resolution

**Problem**: Two engineers in conflict over technical approach. Affecting team morale.

**Mental Models to Apply**:
- m01_map_is_not_the_territory - They have different mental models
- m19_incentives - What are their underlying motivations?
- m13_cooperation - Find win-win solution

**Example Invocation**:
```
"Apply map/territory and incentives models to team conflict.
Engineer A wants microservices, Engineer B wants monolith. Both digging in."
```

**Outcome**: Understand root causes, reframe as shared problem, facilitation strategy

---

### 19. Meeting Efficiency

**Problem**: Team spending 20hrs/week in meetings. Productivity suffering.

**Mental Models to Apply**:
- m32_bottlenecks - Meetings are the constraint
- m51_trade-offs - Meeting time = less coding time
- m54_efficiency - Minimize waste

**Example Invocation**:
```
"Apply bottlenecks to our meeting overload problem"
```

**Outcome**: Meeting audit, eliminate low-value meetings, time-boxing, async alternatives

---

### 20. Performance Review & Feedback

**Problem**: Need to give difficult feedback to underperforming team member.

**Mental Models to Apply**:
- m93_sensitivity_to_fairness - Frame feedback fairly
- m85_narrative_instinct - Use stories to illustrate
- m63_framing - Growth opportunity vs criticism

**Example Invocation**:
```
"Apply framing and fairness models to delivering constructive feedback"
```

**Outcome**: Feedback approach that's direct but respectful, actionable, growth-oriented

---

## Content Creation & Communication

### 21. Technical Blog Post Structure

**Problem**: Writing technical article but structure feels scattered. Hard to follow.

**Mental Models to Apply**:
- m67_plot - Story arc for articles
- m01_map_is_not_the_territory - Don't assume reader knowledge
- m85_narrative_instinct - People learn through stories

**Example Invocation**:
```
"Apply narrative and plot models to structuring my technical blog post about Kubernetes scaling"
```

**Outcome**: Clear structure with setup/conflict/resolution, concrete examples, reader-focused

---

### 22. Persuasive Argument Construction

**Problem**: Need to convince leadership to invest in infrastructure. Proposal keeps getting rejected.

**Mental Models to Apply**:
- m05_second-order_thinking - Show long-term consequences of inaction
- m63_framing - Frame as risk mitigation, not cost
- m84_social_proof - Industry leaders are doing this

**Example Invocation**:
```
"Apply second-order thinking and framing to my infrastructure investment proposal"
```

**Outcome**: Compelling narrative focused on business impact, risk mitigation framing, executive-level reasoning

---

### 23. Documentation Strategy

**Problem**: Engineers complain docs are outdated/unhelpful. Low adoption.

**Mental Models to Apply**:
- m60_audience - Who are we writing for?
- m01_map_is_not_the_territory - Docs are map, code is territory
- m30_feedback_loops - Create doc maintenance loops

**Example Invocation**:
```
"What mental models apply to documentation strategy?"
[Discovery mode suggests audience, map/territory, feedback loops]
```

**Outcome**: User-focused docs, embedded in workflow, automated freshness checks

---

## Financial & Investment Decisions

### 24. Stock Investment Analysis

**Problem**: Considering investing in hyped tech stock. FOMO driving decision.

**Mental Models to Apply**:
- m59_bubbles - Is this a bubble?
- m84_social_proof - Everyone buying = not a reason to buy
- m82_availability_heuristic - Recent gains ≠ future performance
- m06_probabilistic_thinking - What are actual odds?

**Example Invocation**:
```
"Apply bubbles and availability heuristic to evaluating NVDA stock investment"
```

**Outcome**: Rational evaluation, awareness of emotional drivers, risk-adjusted decision

---

### 25. Real Estate Purchase Decision

**Problem**: Buying first home. Emotional purchase, biggest financial decision of life.

**Mental Models to Apply**:
- m34_margin_of_safety - Don't max out budget
- m05_second-order_thinking - How does this affect life in 5-10 years?
- m51_trade-offs - Monthly payment vs other financial goals

**Example Invocation**:
```
"/mental-models - Should I buy this house?
$800K house, $160K down payment (50% of savings), $4K/month mortgage vs $2.5K rent."
```

**Outcome**: Financial analysis with safety margin, lifestyle trade-offs, decision framework

---

## Learning & Education

### 26. Choosing Online Course or Bootcamp

**Problem**: 10 courses on same topic. Unclear which to invest time/money in.

**Mental Models to Apply**:
- m96_survivorship_bias - Success stories hide failures
- m41_sampling - Review sample is biased
- m02_circle_of_competence - Match course to current skill level

**Example Invocation**:
```
"Apply survivorship bias to evaluating online course reviews"
```

**Outcome**: Skeptical review reading, seek out dropout rates, better course selection

---

### 27. Research Strategy for Deep Dive

**Problem**: Learning complex topic (e.g., distributed systems). Overwhelming amount of material.

**Mental Models to Apply**:
- m03_first-principles_thinking - Start with fundamentals
- m18_hierarchical_organization - Learn bottom-up
- m21_leverage - Find 20% of concepts that explain 80%

**Example Invocation**:
```
"Apply first-principles thinking to learning distributed systems from scratch"
```

**Outcome**: Structured learning path, foundation-first approach, core concepts identified

---

## Quick Reference: Problem → Models

**Decision-Making**: m02, m05, m06, m07, m51
**System Analysis**: m32, m33, m34, m38, m40
**Bias Awareness**: m82, m84, m91, m96, m98
**Strategy**: m21, m22, m51, m57, m72
**Communication**: m01, m60, m63, m67, m85
**Risk Assessment**: m06, m07, m34, m44, m59
**Optimization**: m21, m32, m40, m50, m54
**Team Dynamics**: m13, m19, m76, m77, m93
**Learning**: m02, m03, m10, m30, m41

---

## How to Use This Guide

1. **Find your domain**: Navigate to relevant section
2. **Match the problem**: Find similar use case
3. **Note the models**: See which models were applied
4. **Try the invocation**: Use similar prompt with your context
5. **Adapt to your situation**: Customize for your specific problem

## Contributing Use Cases

Have a use case not listed here? Contribute by:
1. Fork the repository
2. Add your use case to this file
3. Include: Problem, Models Applied, Example Invocation, Outcome
4. Submit pull request

The mental-models skill becomes more powerful with diverse real-world examples!
