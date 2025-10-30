# Interactive Mode Example

## User Request
"I'm stuck on this decision but not sure which mental model to use. Help me figure out the right approach."

## Assistant Response (Part 1: Clarifying Questions)

To recommend the best mental models for your situation, I need to understand your decision better:

### 1. What type of decision are you facing?
- [ ] Strategic/long-term planning (2+ years)
- [ ] Resource allocation (time, money, people)
- [ ] Technical/design choice
- [ ] Personal/career decision
- [ ] Risk assessment
- [ ] Process/system improvement
- [ ] Competitive/business strategy

### 2. What's your time horizon?
- [ ] Immediate (need decision today/this week)
- [ ] Short-term (1-3 months impact)
- [ ] Medium-term (3-12 months impact)
- [ ] Long-term (1+ years impact)

### 3. What's your biggest concern or constraint?
- [ ] Don't understand the problem deeply enough
- [ ] Multiple competing options, hard to choose
- [ ] Worried about unintended consequences
- [ ] Limited resources force trade-offs
- [ ] High uncertainty/risk
- [ ] Need to convince others/build consensus
- [ ] Trying to optimize existing system

Please select the options that best match your situation.

---

## User Answers

1. **Type**: Technical/design choice + Long-term planning
2. **Time horizon**: Long-term (1+ years impact)
3. **Concern**: Multiple competing options + Worried about unintended consequences

---

## Assistant Response (Part 2: Recommendations)

Based on your answers, here are the 3 best mental models for your situation:

### 🎯 Primary Recommendation: Second-Order Thinking (m05)

**Why this fits your situation**:
- You selected "worried about unintended consequences" ← Direct match
- Long-term time horizon means ripple effects matter
- Technical decisions compound over time
- This model forces you to think beyond immediate effects to 2nd and 3rd order consequences

**What it provides**:
"Always consider the effects of the effects." Don't just ask "What happens if we choose X?" Ask "What happens after what happens? And then what?"

**Example application**: If choosing microservices architecture:
- 1st order: More flexible, scalable services
- 2nd order: Increased operational complexity, distributed debugging
- 3rd order: Team structure changes, hiring profile changes, long-term maintenance burden

---

### 🔄 Also Consider: Trade-Offs (m51)

**Why this fits your situation**:
- You have "multiple competing options" ← Direct match
- Technical choices always involve trade-offs
- Long-term decisions mean opportunity costs matter more

**What it provides**:
Every choice means saying no to alternatives. Understand what you're giving up (opportunity cost) by choosing each option.

**Example application**: Choosing between three database options
- Option A gains: Speed / Option A gives up: Flexibility
- Option B gains: Flexibility / Option B gives up: Simplicity
- Option C gains: Simplicity / Option C gives up: Speed
→ Which matters most aligns with which trade-off to accept

---

### 🔍 Alternative Angle: Inversion (m07)

**Why this fits your situation**:
- Technical + long-term = high cost if wrong
- "Worried about unintended consequences" suggests fear of failure
- Sometimes easier to identify what would be a disaster than what would be optimal

**What it provides**:
Instead of "What makes this choice succeed?" ask "What makes this choice fail catastrophically?" Avoid ruin first, then optimize.

**Example application**: For architecture decision
- What would make this choice fail in 2 years?
- What would make this unmaintainable?
- What would make this impossible to scale?
→ Eliminate options that have unacceptable failure modes first

---

## How These Models Work Together

If you use 2-3 of these in combination:

1. **Inversion**: Eliminate catastrophically bad options first
2. **Trade-Offs**: Understand what you're gaining/giving up with remaining options
3. **Second-Order Thinking**: Evaluate long-term ripple effects of finalist choices

This gives you a structured decision framework:
- Avoid disaster (Inversion)
- Weigh costs/benefits (Trade-Offs)
- Project long-term effects (Second-Order Thinking)

---

## Next Steps - Your Choice

**Option A**: Quick-apply one model to your specific decision
- "Apply second-order thinking to [your specific situation]"
- Fast, 2-3 minutes

**Option B**: Deep-analysis with 2-3 models
- I'll create a comprehensive analysis in a WorkSpace folder
- Full synthesis with all three models working together
- 10-15 minutes, produces detailed report

**Option C**: Explore a model first
- "Show me the full thinking steps for second-order thinking"
- "What are the coaching questions for trade-offs?"
- See if it resonates before committing

**What would you like to do?**

---

## Key Characteristics of Interactive Mode

1. **Clarifying questions** adapt to user's situation
2. **Model recommendations** reference user's specific answers
3. **Explain WHY** each model was chosen (transparent reasoning)
4. **Show how models combine** for comprehensive approach
5. **Offer next steps** with clear options
6. **User maintains control** of depth/direction

**Execution Time**: 2-3 minutes + user response time
