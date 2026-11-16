# 1. Development principles

Deliver development work efficiently, correctly, and at low total cost. Build what the current task needs. Keep code understandable, verifiable, and maintainable. Count communication, tools, rework, and maintenance as costs. Correctness and safety come first, followed by maintainability and simplicity. Meet agreed performance requirements. Automate requirements that tools can check.

Use the [development workflow](3-development-workflow.md) and the [check schedule](#15-automated-check-schedule).

## 1.1 Requirements and scope

### 1.1.1 Design for current needs

State the goal and exclusions in the task brief. Add configuration, extension points, and dependencies only for demonstrated needs. Reading JSON does not require a plugin framework. Use tools to find unused code and dependencies.

Refactoring, tests, and build checks are maintenance work. The absence of a new feature does not justify removing them. Dependency additions and deletion of non-build files still require authorization.

### 1.1.2 Task boundaries and independent review

Give each task a clear goal and acceptance criteria. Plan large changes first. For the standard workflow, a fresh session that did not implement the work reviews the task brief, complete changes, and evidence. Resolve findings that affect correctness.

## 1.2 Code design and maintainability

### 1.2.1 Responsibilities and dependency rules

Document each module's responsibility, allowed dependencies, and forbidden dependencies. For example, business rules must not depend directly on UI or transport frameworks, and UI code must not write the database directly. Check dependencies automatically before development and merge. Compare the architecture description with actual code periodically.

Prove the dependency check rejects a real violation when adopting it.

### 1.2.2 Interfaces and information hiding

Expose only the contracts callers need. Review interfaces that leak database or framework types, require a hidden operation order, or create chains of forwarding modules.

Do not wrap a single SQLite implementation in a matching set of interfaces for a hypothetical database replacement. A single implementation or caller is a review clue, not a reason to remove a necessary interface or test boundary.

### 1.2.3 State modeling and input parsing

Parse external configuration, files, requests, and model output into explicit types before business logic. Represent mutually exclusive states with types. Avoid contradictory combinations of booleans and optional fields. Check every branch when adding an enum variant.

Before the main logic, define core data types, reads, writes, and state transitions, then choose data structures. Reuse suitable project types. Test the design with representative inputs without designing every detail in advance.

For example, do not freely combine `connected`, `sessionID`, and `disconnectedAt` into connection state. Internal calls need not repeat boundary validation. Verify the actual guarantees of types, exhaustive branches, and parsing tools in the project.

### 1.2.4 Complexity and shared state

Use clear names and signatures. Make data sources and writers traceable. Keep each rule in one place, remove useless forwarding, and control nesting, complexity, and duplication.

A chain such as `handler → service → manager → helper` adds reading cost when every step only forwards. Set size and complexity limits from project evidence and tighten them gradually.

When several actors may write shared state, first separate their write targets. Use a single writer, mutual exclusion, or atomic operations only where sharing is necessary. A verbal convention is not concurrency control.

Keep comments that explain design decisions, external limits, and public contracts. Remove comments that repeat code. Implement and verify structural protection before deleting a duplicate written constraint.

### 1.2.5 Errors and recovery

Handle errors explicitly. Empty `catch` blocks and defaults must not hide failures. For writes, sends, and other side effects, define and test partial failure, crashes, and repeated execution.

Verify end-to-end idempotency before retrying. Query the original operation when its result is unknown. Legitimate failures need an explicit rejection or recovery path.

## 1.3 Testing and acceptance

### 1.3.1 Behavior tests and defect detection

Test results and side effects, rather than copying the algorithm or only counting internal calls. Tests must survive a structural change that preserves behavior and fail when behavior is wrong.

Keep evidence of the original failure and successful repair. Verify critical protection against a runnable incorrect version. A compilation failure is not proof that a behavior check detected the defect. Use mutation testing at milestones where applicable.

### 1.3.2 Evidence and test protection

Record actual commands, exit codes, and raw logs. UI work needs corresponding real interactions and screenshots. Fast checks provide feedback. They do not replace full checks before merge, applicable runtime acceptance, or independent review in the standard workflow.

Authors must not make checks pass by changing assertions, skipping tests, disabling rules, or raising limits. Explain every test change for separate review. Explain new exemptions and obtain approval where required. Missing evidence or an unrun required check prevents completion.

### 1.3.3 Root causes and related defects

Reproduce the defect, find the first incorrect operation, and check related paths. Explain why an added null check, retry, or default fixes the cause. Keep protection for legitimate failure states.

Include recurring defects in periodic review and automate their detection where possible.

After two substantive repairs based on the same premise fail, state that premise and test it with a minimal experiment before continuing. This does not reset the rework budget. See [task-specific methods](3-workflow/3.5-implementation.md#351-task-specific-methods).

## 1.4 Documentation and standard maintenance

### 1.4.1 Documents and information structure

Keep current plans, architecture decisions, and constraints in the repository. Chat alone is insufficient. Entry documents provide common commands, constraints not apparent from code, and links to details. Keep the full standard out of `AGENTS.md`. Review links and stale content periodically.

### 1.4.2 Prevention and automated checks

When a reviewer finds a checkable defect, create a task to automate detection. Record why automation is unsuitable for other findings. By a second reviewer discovery of the same defect class, a corresponding task or specific explanation must already exist. Follow the implementation order below. Errors must explain the fix.

Reviewers focus on design and correctness. Tools handle style. Repair false positives as well. The requirements owner must approve any reduction in existing protection.

## 1.5 Automated check schedule

| Trigger | Required checks | Responsibility and failure handling |
| --- | --- | --- |
| While editing | Check authorization and forbidden actions before writes. Format and run fast code checks after edits, returning errors to the agent. | The project tooling owner configures checks. Implementers follow them. Block forbidden actions. Return code failures to section 3.5 and permission gaps to an authorized user. |
| Before commit | Format, code rules, spelling, and reasons for new exemptions, targeting feedback within seconds. | Git hooks run `scripts/check.sh --quick` or a verified equivalent. A failure prevents commit and returns to section 3.5. Passing does not authorize a commit. |
| Before merge | All applicable tests, dependency checks, security scans, and no coverage decline for the exact version. | A trusted check service or merge tool runs `scripts/check.sh --full` or a verified equivalent. Missing tools, unrun checks, or failures prevent merge. Complete sections 3.5 through 3.7. |
| At each milestone or agreed interval | The project's 3–5 architecture health checks, mutation testing, duplication, complexity, documentation, and quality data. | The assigned owner runs checks. Repair findings through the workflow, then recheck. Do not bypass the main workflow for repairs. |

Configure these commands or verified equivalents when adopting the standard, and prove they work. Before writes, check scope, protected files, and forbidden directories. Run commit hooks normally. Push only with authorization. A trusted check service or merge tool enforces final merge conditions.

Small changes may check affected areas first, with full checks before merge. Evidence may be reused for identical inputs. Consolidate milestone checks where appropriate. Re-review changed and affected areas after repairs and replay the original failure. Before consolidated checks, prepare only an isolated combined version. Do not merge first and check later. Simple low-risk tasks do not require a plan, task brief, or separate review, but an actual merge still requires full checks.

### 1.5.1 Selecting checks

Prefer an existing code rule, then a diff or regular-expression scan, then dependency rules or architecture tests. Reserve documented manual review for decisions that cannot be checked automatically. Scanners need positive, negative, and bypass cases. A keyword match does not prove complete coverage.

Required automated checks for forbidden actions, dependencies, full validation, and security cannot become manual approvals because tools are missing. Mark missing or unrun checks `not_run` and stop the affected operation. Follow the [new-check workflow](4-periodic-review.md#42-prevention-and-automated-checks) for review findings.

Errors identify the violated requirement, file or actual value, repair, recheck command, and raw log. For example: business rules import UI types; use business types and convert at the UI boundary, then rerun the dependency check. Reporting only an architecture error is insufficient.

### 1.5.2 Limits and exceptions

Record the baseline and existing findings. Do not redefine a new violation as baseline to clear a failure. Raising complexity limits, disabling rules, widening exclusions, lowering severity, or adding skip conditions reduces protection.

Before a reduction, provide the exact change, reason, replacement protection, counterevidence, recovery, and current architecture decision. Obtain a verifiable requirements-owner approval. An author's self-written approval is insufficient. The designated tooling owner implements the approved change, then runs trusted full checks and independent review.

If a specification change requires an old assertion to change, the author stops. The requirements owner assigns a separate task to a test or tooling owner. Keep the assertion until approved. Every approval applies only to its recorded scope.

## 1.6 Suggested tools

Choose tools for actual project needs. Verify versions and options, prove rejection with an incorrect example, then configure them.

| Purpose | Tools or capabilities |
| --- | --- |
| Dependencies | Go: `depguard`, `go-arch-lint`, `arch-go`. Rust: crate responsibilities, Cargo declarations, `cargo-deny`. TypeScript: `dependency-cruiser`, `eslint-plugin-boundaries`. |
| Unused code and dependencies | `unused`, `unparam`, `cargo-machete`, `knip`, Rust `dead_code`. |
| Types and branches | Rust exhaustive `match` and Clippy. TypeScript strict types, exhaustive `switch`, input parsing. Verify tools such as `exhaustive`. |
| Complexity and duplication | `gocognit`, `cyclop`, `funlen`, `nestif`, Clippy, ESLint `complexity`, `max-depth`, `max-lines-per-function`, `jscpd`. |
| Error handling | `errcheck`, `wrapcheck`, Clippy `unwrap_used` and `expect_used`, TypeScript `no-floating-promises` and `no-empty`. |
| Mutation testing | `cargo-mutants`, Stryker, `gremlins`. |
| Exemption reasons | `nolintlint`, Clippy `allow` reasons, `ban-ts-comment`. |
| Automatic triggers | Claude Code `PreToolUse` and `PostToolUse`, Codex approval rules, Git hooks such as `lefthook`. |

## 1.7 Manual review checklist

Standard-workflow reviewers record yes, no, or N/A for each item, with location or evidence. Separate errors from suggestions. Style suggestions do not block, but machine-reported errors still need repair. Direct tasks do not require a separate review because of this checklist.

1. The change serves the current requirement without hypothetical features.
2. Interfaces are clear and hide implementation details from callers.
3. Types exclude contradictory states and external inputs are parsed.
4. Names, data sources, and writers are clear.
5. Error handling is explicit and failures are not hidden by defaults or empty handlers.
6. Tests cover side-effect retries and recovery. Unknown results are queried first.
7. Tests detect incorrect behavior. Critical incorrect versions can run.
8. Actual commands, exit codes, raw output, and applicable UI evidence exist.
9. Original tests and assertions remain protected. Test changes receive separate review, and reductions have approval.
10. Defects have reproduction, root-cause analysis, and related-path checks.
11. Current decisions are documented and superseded decisions no longer guide execution.
12. Checkable defects have automation tasks. Other findings have specific reasons why automation is unsuitable.

## 1.8 Milestone checks

At each milestone, run full checks for the current version. Review dependencies, mutation testing, duplication and complexity changes, stale documents, exemptions, recurring defects, and four task metrics: rework count, review findings, post-merge regressions, and duplicate-code growth. Define 3–5 architecture health checks and their measurement rules in advance.

Keep unrun checks pending and unknown data unknown. Repair and recheck ordinary low-risk findings directly. Use a task brief and the main workflow for other findings.

## 1.9 Sources and applicability

Sources include vendor documentation, team experience, and research publications. External links have not all been individually verified. Verify tool capabilities and effects in the project. See [source metadata](../provenance.md).

| Source | Material type | Link |
| --- | --- | --- |
| OpenAI Ryan Lopopolo: Harness engineering | Team experience | [Source](https://openai.com/index/harness-engineering/) |
| Claude Code best practices | Vendor documentation | [Source](https://code.claude.com/docs/en/best-practices) |
| Anthropic: Effective harnesses for long-running agents | Team experiment | [Source](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
| Anthropic: Context engineering | Vendor experience | [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| Anthropic: Building effective agents | Vendor methods | [Source](https://www.anthropic.com/engineering/building-effective-agents) |
| Codex AGENTS.md guidance | Vendor documentation | [Source](https://developers.openai.com/codex/guides/agents-md) |
| Cursor Lee Robinson: Agent best practices | Vendor experience | [Source](https://cursor.com/blog/agent-best-practices) |
| xAI Lingxi Li: Engineering guide | Individual engineering experience | [Source](https://x.ai/bot/guides/grok-bot-for-engineering) |
| Simon Willison: Vibe engineering | Individual opinion | [Source](https://simonwillison.net/2025/Oct/7/vibe-engineering/) |
| Google code review standard | Review standard | [Source](https://google.github.io/eng-practices/review/reviewer/standard.html) |
| Google: Behavior testing | Testing practice | [Source](https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html) |
| Software Engineering at Google, chapter 11 | Engineering book | [Source](https://abseil.io/resources/swe-book/html/ch11.html) |
| Fowler: YAGNI | Design principle | [Source](https://martinfowler.com/bliki/Yagni.html) |
| Thoughtworks: Architectural fitness functions | Architecture evolution | [Source](https://www.thoughtworks.com/en-us/radar/techniques/architectural-fitness-function) |
| Clean Architecture dependency rule | Dependency rule | [Source](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) |
| Ousterhout book excerpts | Book excerpts; full book not read | [Source](https://web.stanford.edu/~ouster/cgi-bin/book.php) |
| Parnas 1972 | Research paper; full paper not read | [Source](https://doi.org/10.1145/361598.361623) |
| Minsky: Type design | Type design practice | [Source](https://blog.janestreet.com/effective-ml-revisited/) |
| Alexis King: Parse at boundaries | Parsing practice | [Source](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) |
| Stripe: Idempotent APIs | Interface practice | [Source](https://stripe.com/blog/idempotency) |
| Internal principles | Internal methods | Local reference material |
