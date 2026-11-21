# 6. Git and GitHub collaboration

Read this chapter for staging, commits, branches, pushes, pull requests (PRs), merges, or history editing. It applies throughout the [development workflow](3-development-workflow.md) without adding a stage. Simple low-risk tasks may still proceed directly, without a mandatory new branch, PR, or review.

## 6.1 Scope and project policy

Protect existing work, follow authorization, check the exact version, and retain traceable results. Recommendations apply where a project has no existing convention. Record project choices once in the [adoption template](../../assets/templates/project-adoption.md); tasks record only their differences. Stricter project rules still apply. Exceptions to common safeguards follow section 2.1.

| Project policy | Recommendation or selection criteria |
| --- | --- |
| Branches and isolation | Keep the main branch deliverable and use short-lived task branches. Give independent changes separate branches and writers; add release branches when maintaining multiple versions. |
| Commit format and language | Prefer existing conventions; otherwise consider Conventional Commits. The project chooses language, types, scopes, and subject length. |
| Merge method | Squash can suit an ordinary single-task PR. Do not squash when individual commits, branch relationships, or the ancestry needed for a fast-forward must be preserved. If a squash has already been done and a fast-forward is therefore impossible, apply only the unique commits onto the current target branch. Confirm traceability and subsequent branch use in advance. |
| Checks and approvals | Identify quick/full commands, trusted execution, required results, and actual approval accounts. Configure protection using capabilities available to the repository. |
| Releases and retention | Define version tags, artifacts, retention of unique evidence, cleanup scope, and owners. Adopt signing and merge queues when needed. |

Adoption does not automatically install hooks, change remote protection, or add approvers. Resolve missing policy needed for the current action. Do not request existing authorization again.

## 6.2 Starting work and branches

[Read this section](6-version-control/6.2-starting-work-and-branches.md).

## 6.3 Staging and commits

[Read this section](6-version-control/6.3-staging-and-commits.md).

## 6.4 Pushes and pull requests

[Read this section](6-version-control/6.4-pushes-and-pull-requests.md).

## 6.5 Review and merge

[Read this section](6-version-control/6.5-review-and-merge.md).

## 6.6 Undoing changes and editing history

[Read this section](6-version-control/6.6-undo-and-history.md).

## 6.7 Sensitive information and cleanup

[Read this section](6-version-control/6.7-sensitive-information-and-cleanup.md).

## 6.8 References

These sources describe command semantics and collaboration practices. Authorization, evidence, and role requirements come from this development standard. Confirm current platform capabilities during project adoption.

- [Pro Git: contributing to a project](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project), [Git commit](https://git-scm.com/docs/git-commit), [Git worktree](https://git-scm.com/docs/git-worktree)
- [Git revert](https://git-scm.com/docs/git-revert), [Git reset](https://git-scm.com/docs/git-reset), [Git rebase](https://git-scm.com/docs/git-rebase), [Git push](https://git-scm.com/docs/git-push)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow), [Helping others review changes](https://docs.github.com/en/pull-requests/concepts/helping-others-review-your-changes)
- [GitHub merge methods](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github), [Required status checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks), [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub PR approval limits](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews), [Sensitive data removal](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), [DORA: trunk-based development](https://dora.dev/capabilities/trunk-based-development/)
