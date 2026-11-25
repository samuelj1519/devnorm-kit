# DevNorm

A generated development-standard plugin with a main workflow skill and independently invocable helper skills, task-specific methods, and complete resources. Read the [installation guide](skills/devnorm/INSTALL.md) for installation, updates, and removal.

The main skill is [skills/devnorm/SKILL.md](skills/devnorm/SKILL.md). Its [provenance](skills/devnorm/provenance.json) and [notices](skills/devnorm/THIRD_PARTY_NOTICES.md) identify fixed sources, adaptations, and licenses. Original DevNorm content uses MIT. Third-party content retains its own licenses.

English is the generated package language. The Chinese technical-writing capability and its Chinese examples remain Chinese. The source repository keeps its original language. Regenerate after source changes rather than edit generated files.

## Development capabilities

One DevNorm entry selects requirements, module/domain design, task planning, implementation/simplification, diagnosis, review, actual verification, and delivery methods by project stage. UI, performance, and state modeling apply conditionally. No separate upstream skill bundles are required.

Decision interviews, history recovery, task refinement, verification-tool authoring/maintenance, project hooks/human-only guides, and external feedback triage require an explicit prompt. Natural language is sufficient: "Use DevNorm for this task; interview me about requirements, at most three rounds." Explicit invocation does not expand installation, account, or external-write authority.

See the [main entry](skills/devnorm/SKILL.md) and [capability index](skills/devnorm/references/capabilities.json). Upstream updates are scanned, analyzed, reviewed, and accepted centrally in the source project before package generation. This bundle does not update installed copies itself.

The skills table below is generated from the accepted entry declarations. Each helper includes its resources for independent installation. Shared source material is maintained once and copied by the generator.

## Skills

| Skill | Purpose | Invocation | Instructions |
| --- | --- | --- | --- |
| devnorm | Full project development workflow | By task | [Entry](skills/devnorm/SKILL.md) |
| devnorm-design | Design additions and changes to modules, interface contracts and shared state. | When applicable | [Entry](skills/devnorm-design/SKILL.md) |
| devnorm-debug | Reproduce defects and verify root causes and repairs. | When applicable | [Entry](skills/devnorm-debug/SKILL.md) |
| devnorm-review | Independently review a fixed candidate against standards and specifications. | When applicable | [Entry](skills/devnorm-review/SKILL.md) |
| devnorm-verify | Verify actual CLI, service, browser, and native behavior. | When applicable | [Entry](skills/devnorm-verify/SKILL.md) |
| devnorm-interview | Conduct a bounded requirements interview. | Explicit request | [Entry](skills/devnorm-interview/SKILL.md) |
| devnorm-recall | Recover historical context for a specified project and scope. | Explicit request | [Entry](skills/devnorm-recall/SKILL.md) |
| devnorm-tdd | Apply test-first cycles to defined logic and cheaply reproducible defects. | When applicable | [Entry](skills/devnorm-tdd/SKILL.md) |
| devnorm-sources | Manually check sources and analyze new capabilities. | Explicit request | [Entry](skills/devnorm-sources/SKILL.md) |
