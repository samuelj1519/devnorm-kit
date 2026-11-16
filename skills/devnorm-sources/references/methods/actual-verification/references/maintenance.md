# Create and maintain project verification

**Run only when the prompt explicitly requests verification instructions, scripts, or skill creation/maintenance.** Normal acceptance uses existing entries without generating a new skill.

1. Inspect the actual user surface, launch command, readiness signal, interaction tools, observable results, isolation, and cleanup. Reuse tests and controls first. Report missing launch prerequisites instead of inventing runnable steps.
2. Write minimal instructions or scripts in the project's existing location. Create a skill only when independent discovery is useful. Do not mandate a .cursor path or new tools. State exact commands, version checks, port/process/data ownership, failure stops, evidence locations, and cleanup scope.
3. Maintain a concise user-visible feature index with preconditions, real entry, action, and observable completion. Do not create empty files to fill a feature quota.
4. Actually run launch, readiness checks, a representative feature, valid/failure results, and cleanup. Verify evidence survives teardown. Separate tool tests from target-app acceptance and list unexecuted features.
5. Compare maintained instructions with code/features. Distinguish document drift, harness defects, and product regressions. Replay repaired tools/docs. Return regressions to implementation without deleting journeys or weakening assertions. Review model correspondence when state logic changes.

Generated but unexecuted instructions remain an unverified draft. Account, model, install, and service permissions retain task authorization. Clean up only resources owned by this run.

Source: adapted from pinned pstack create-verification-skill and maintain-verification-skill. Uses project locations, conditional tools, and real proofs without fixed roles, feature counts, or PR creation.
