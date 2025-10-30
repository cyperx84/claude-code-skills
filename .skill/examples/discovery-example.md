# Discovery Mode Example

## User Request
"What mental models apply to scaling distributed systems?"

## Assistant Response

### Mental Models for: Scaling Distributed Systems

Found 8 relevant models across multiple categories:

---

### 1. Bottlenecks (m32)
**Category**: Systems Thinking
**Summary**: A choke point that limits system capacity—the weakest link. Identify and elevate constraints to improve throughput.
**Why relevant**: Direct match to "process optimization", "workflow efficiency" keywords. Scaling means finding what limits capacity.

### 2. Scale (m33)
**Category**: Systems Thinking
**Summary**: Size changes everything. Effects are non-linear—10x bigger ≠ 10x the same. Different rules apply at different scales.
**Why relevant**: Exact keyword match to "scale". Core model for understanding how systems behave differently at size.

### 3. Feedback Loops (m30)
**Category**: Systems Thinking
**Summary**: Output influences input. Reinforcing loops amplify, balancing loops stabilize. Essential for self-correcting systems.
**Why relevant**: Distributed systems need auto-scaling, circuit breakers, and self-healing—all feedback loop mechanisms.

### 4. Margin of Safety (m34)
**Category**: Systems Thinking
**Summary**: Engineer room for error. Build redundancy for the unexpected. Robustness over efficiency at critical points.
**Why relevant**: Distributed systems must handle failures gracefully—fault tolerance is a margin of safety principle.

### 5. Law of Diminishing Returns (m40)
**Category**: Systems Thinking
**Summary**: Each additional input yields less output. Eventually optimization stops paying off. Know when to stop.
**Why relevant**: Adding more servers doesn't scale linearly forever. Coordination costs eventually dominate.

### 6. Multiply by Zero (m44)
**Category**: Mathematics
**Summary**: A single failure point can destroy everything. Entire system reliability = product of component reliabilities.
**Why relevant**: One service timing out can cascade and bring down the whole system. Identify single points of failure.

### 7. Interdependence (m53)
**Category**: Economics
**Summary**: Components depend on each other. Complexity grows exponentially with connections. Tight coupling = fragility.
**Why relevant**: Microservices are interdependent. Understanding dependencies is crucial for distributed architecture.

### 8. Leverage (m21)
**Category**: Science (Physics)
**Summary**: Small inputs → large outputs with the right lever. Find high-leverage intervention points in systems.
**Why relevant**: In scaling, find the 20% changes that deliver 80% improvement. Caching, indexing, CDNs are leverage.

---

## Quick Pattern Recognition

These models cluster into themes:

**Finding Constraints** (What's limiting us?):
- m32_bottlenecks
- m40_law_of_diminishing_returns

**Handling Size** (How does scale change things?):
- m33_scale
- m53_interdependence

**Building Resilience** (How to handle failure?):
- m34_margin_of_safety
- m44_multiply_by_zero
- m30_feedback_loops

**Optimizing Effort** (Where to focus?):
- m21_leverage

---

## Suggested Next Steps

**For Quick Insights**: Pick one model to quick-apply
- "Apply bottlenecks to our current architecture"
- "Use scale model to analyze our database layer"

**For Comprehensive Analysis**: Deep-analysis with 2-3 models
- Bottlenecks + Scale + Margin of Safety would work well together
- Shows constraints, non-linear effects, and failure planning

**For Exploration**: Read a specific model
- "Show me the full thinking steps for m33 scale"
- "What are the coaching questions for bottlenecks?"

---

**What would you like to do next?**

---

**Execution Time**: 30 seconds
**Models Searched**: 98
**Relevant Matches**: 8
