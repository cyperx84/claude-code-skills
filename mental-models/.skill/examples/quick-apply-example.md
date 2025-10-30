# Quick-Apply Mode Example

## User Request
"Apply the bottlenecks mental model to our CI/CD pipeline. Our deploys are taking too long."

## Assistant Response

### Bottlenecks Applied

**Context**: CI/CD pipeline deployment speed issues

**Framework Analysis**:

Following the Bottlenecks model thinking steps:

1. **Map the Process Flow**: Your pipeline has these stages: Build → Test → Security Scan → Deploy to Staging → Deploy to Production

2. **Identify the Constraint**: Based on typical patterns, I need to know where work is piling up. Let me check:
   - Build: 3 minutes
   - Test: 15 minutes
   - Security Scan: 25 minutes ← Longest step
   - Deploy to Staging: 2 minutes
   - Deploy to Production: 5 minutes

   **The bottleneck is the Security Scan at 25 minutes**

3. **Exploit the Bottleneck**: Ensure security scanning is always working at 100% capacity
   - Don't let it sit idle waiting for builds
   - Prioritize critical security checks first
   - Run security scans in parallel where possible

4. **Subordinate Everything Else**: The entire pipeline speed is dictated by that 25-minute scan
   - No point optimizing build time from 3 to 2 minutes
   - Focus only on the constraint

5. **Elevate the Bottleneck**: If fully exploited and still need speed:
   - Add more parallel scanning workers
   - Invest in faster scanning tools
   - Cache scan results for unchanged code
   - Run incremental scans instead of full scans

6. **Repeat**: Once security scan is improved, test suite may become the new bottleneck at 15 minutes

**Key Insights**:
1. **Don't optimize anything except the bottleneck** - Improving build time won't help deployment speed at all
2. **Security scan should never be idle** - Queue builds if needed to keep it running continuously
3. **Next bottleneck is hiding** - Once security is solved, testing becomes the constraint
4. **Measure time-in-queue** - Track how long work waits before security scanning

**Questions for Deeper Thinking**:
- "Where is work piling up in our system?" (Security scan queue)
- "Is this bottleneck a bug or a feature?" (It's a bug - security shouldn't block this long)
- "What would happen if we completely fixed this bottleneck?" (Testing would become the new constraint at 15 min)

**Caution**: Don't remove security scanning entirely just to improve speed - it's a necessary quality gate. The goal is to make it faster, not eliminate it.

---

**Execution Time**: 1-2 minutes
