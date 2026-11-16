<!-- DevNorm adaptation of pstack statechart/references/render.md. MIT; fixed source in provenance.json. No automatic Pele installation or required external renderer. -->

# Render statecharts

Provide Mermaid text, property results, and counterexamples to the behavior owner first. For SVG or other images, use an authorized renderer already available in the target environment. Pele is optional and not bundled or automatically installed.

Check nodes, arrows, and labels against model results. Keep necessary counterexamples visible. Image generation does not prove model success.

Preserve markers: `breaks` means a property violation, `mayBreak` means some underlying states in a merged state may violate it, `bugPath` marks a counterexample, and `repeats` marks a temporal cycle. Explain parallel combinations and omitted steps.

Use the installed Pele API and resource limits where available. Keep SVG with its Mermaid source and project theme. On rendering failure, retain text, actual error, and missing outputs. Do not download tools or relabel rendering failure as model failure.
