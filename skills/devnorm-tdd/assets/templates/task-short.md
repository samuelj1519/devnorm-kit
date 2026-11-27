# Minimum formal-task record

For formal tasks, update this same record throughout. Simple tasks need no brief. Add applicable fields from the [full brief](task.md) when more detail is required. Reference project policy once and retain review conclusions and evidence here rather than in duplicate ledgers. Reuse an existing task record covering these six items instead of rewriting this form; the items specify content, not a format to refill every round.

1. **Goal and impact** <user or caller situation and observable outcome, hard constraints and goals to optimize, evidence of impact and recoverability, affected contracts and guarantees, trade-offs and basis of approval, whether prior review applies and who decided>
2. **Scope:** <allowed files/interfaces, existing work ownership, authorization and prohibited actions>
3. **Exact inputs:** <candidate/base/hashes; project version, checks and policy references>
4. **Checks and stopping:** <key commitments, acceptance criteria, expected results, chosen verification methods and actual evidence; applicable test scenarios and real entry points; original failure and replay; cumulative budget, escalation, and stop conditions>
5. **Independent review:** <one qualified non-author reviewer; exact behavior unit and combination candidate; where applicable, upfront design and test design inputs, conclusion and evidence; candidate and personally run key paths, current conclusion/open items, and original-log references; original failure replay and cumulative budget>
6. **Result and limits:** <changes, actual checks, unverified items/next action; Git operation and objects or N/A>

Choose checks at each stage based on the affected behavior. Run quick checks on the exact staged version before task-branch commits. Before updating an integration target, run [trusted full checks](../../references/standard/3-workflow/3.8-integration-and-completion.md) on the exact combination. Record who triggers the check, the trusted entry point, the fixed target baseline, and where to find the result. Review, acceptance, and integration reference the same result while it remains valid. Expand controls when real models, terminal input, installation or cleanup apply. A short brief cannot omit an actual risk.
