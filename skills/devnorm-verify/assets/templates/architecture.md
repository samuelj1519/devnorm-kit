# <Project> architecture

Describe code responsibilities, dependencies, and constraints under the [workflow](../../references/standard/3-development-workflow.md).

## Responsibilities and dependencies

| Path or package | Responsibility and owner | Public interface | Allowed dependencies | Forbidden dependencies and reasons |
| --- | --- | --- | --- | --- |
| <path> | <responsibility and owner> | <interface> | <module> | <module and reason> |

## Current decisions and invariants

<List approved decisions and exact versions. Examples require project confirmation before adoption: UI accesses storage through application services; generated protocol code has one source.>

<Explain core types, reads, writes, and state owners. Separate concurrent write targets where possible. Identify synchronization where sharing is necessary. Reference existing exact descriptions rather than copying code.>

## Three to five architecture health checks

| Check | Baseline, limit, and approval | Tool and command | Repair and owner | Evidence |
| --- | --- | --- | --- | --- |
| Responsibilities and dependencies | <allowed and forbidden edges> | <project-selected Go depguard/arch-go, Rust crate boundaries/cargo-deny, TypeScript dependency-cruiser, or equivalent> | <violated rule and replacement interface or module> | <path> |
| Duplicate-code growth | <predetermined baseline and criteria> | <selected tool> | <consolidate shared responsibilities or remove duplication, preserving behavior> | <path> |
| Package/file size or critical latency | <project budget; select 3–5 checks total> | <existing tool or actual measurement> | <separate responsibilities or diagnose bottleneck; preserve samples> | <path> |

## Security scans

<Project-selected gosec, cargo-audit, semgrep, or existing equivalent. Record version, command, scope, false-positive handling, and stop conditions. Missing required tools remain not_run and block milestone acceptance. Dependency installation needs authorization.>

## Periodic review and issue tracking

<Milestone or interval, owner, checks, and repair tasks. Repair and recheck ordinary low-risk findings directly. Return other findings to the main workflow for risk classification. Record rework, review findings, post-merge regressions, and duplicate-code growth. Do not close before recheck.>

## Limits and automation

<Set evidence-based baselines and tighten limits gradually. A reduction requires requirements-owner approval, independent review, and trusted full checks. Apply the four [check triggers](../../references/standard/1-principles.md#15-automated-check-schedule).>
