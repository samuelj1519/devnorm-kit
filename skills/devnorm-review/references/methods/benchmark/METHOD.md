# Performance measurement

## Scope and inputs

Use before reporting or acting on speed, throughput, latency, or resource measurements. Fix the user workload, version, correctness conditions, environment, and measurement budget.

## Procedure

1. Name the measured work and limiting factor. Confirm that the full workload actually runs. Exclude cache-only work, empty input, early errors, reduced work, scheduler-only timings, and substitute returns.
2. Fix the correct baseline, data size, load, dependencies, hardware, concurrency, warmup, timeouts, and resource limits. Apply the same acceptance checks, workload, and exit conditions to both versions.
3. Record variables separately and change one comparison factor at a time. Choose repetitions by task cost. Preserve every raw result and failure instead of selecting the fastest run.
4. Check throttling, error rates, tail latency, cold start, and the actual target environment. Explain unexpected numbers and inspect the measurement before changing the product.
5. Report comparison method, sample size, distribution or interval, environment limits, and reproduction commands. Unexplained numbers cannot support a speedup claim. A local sample does not establish production behavior.

## Completion and stopping

Correctness matches, workloads are comparable, measurements repeat, and the limiting factor has evidence. Preserve failures. Discard conclusions from wrong baselines or incomplete work. Repair implementation or measurement, and record missing environment/budget.

## Source and adaptation

Adapted from pinned pstack benchmark-checklist. Retains limiter, tuning, error, repeatability, relevance, and actual-work checks, integrated with the standard baseline and evidence requirements.
