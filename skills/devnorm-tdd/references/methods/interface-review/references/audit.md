<!-- DevNorm adaptation of Impeccable skill/reference/audit.md, fixed source recorded in provenance.json. Apache-2.0; copyright and NOTICE retained. Removed unavailable detector, native platform routing and command placeholders; require actual host evidence. -->

# Web technical audit

Scope is verified Web code and embedded Web UI. This reference does not cover complete iOS/Android or native-system standards. Project capabilities own real native acceptance. Missing conditions remain unrun.

## Checks

1. Accessibility: semantics, headings, regions, names, labels, state, alternative text, keyboard order, visible/restored focus, traps, and error location. Apply the project's WCAG level. Normal text is at least 4.5:1 and large text 3:1 where applicable, with explicit exemptions. Reduced motion retains necessary state feedback without flashing or blocked actions.
2. Performance: layout read/write interleaving, layout-triggering animation, unbounded blur/effects, unused dependencies/assets. Measure the real task against a correct baseline first. Use `will-change`, caching, and memoization for actual bottlenecks.
3. Themes: consistent color roles, working theme changes, readability in dark/high-contrast modes. Check hardcoded values against project tokens and brand. Tokens alone do not prove correct results.
4. Responsive layout: narrow viewport, scaling, long text, overflow, and applicable touch-target rules. WCAG 2.5.8 AA normally requires 24×24 CSS px, with spacing, equivalent-control, inline, browser-default, and essential-size exceptions. A project may choose 44×44 as a higher target; it is not the universal AA minimum.
5. Touch: exercise dragging, scrolling, and interruption with real or synthesized touch. Check capture, cancel, lost focus, and `touch-action`. A narrow screenshot proves layout, not gestures.
6. Completeness: working controls, real content, explainable states, and consistent design system. Separate determinate code defects from visual judgment and review detector false positives.

## Evidence

Use available browsers, assistive tools, and project detectors. No external detector is assumed. Use only authorized local DevTools interfaces. Separate static and actual checks for environments such as WKWebView without CDP.

Report location, trigger, actual/expected result, user impact, applicable rule, and specific repair. Use P0–P3 or project priority. Retain working patterns and unrun scope. Do not invent a health score or compliance result without evidence. Review-only work does not change implementation.
