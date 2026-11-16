# Domain concepts and decisions

For ambiguous terms, boundaries, or lifecycles, use real business scenarios to distinguish objects, identity, behavior, and valid states. Then compare code names and explain domain/implementation differences. Dictionary meanings and existing class names alone do not define the domain.

Reuse the project's terminology records for recurring business concepts, preferred names, meaning, and useful counterexamples. Specifications define product behavior; architectural decisions preserve consequential trade-offs and reasons. Do not merge these into a glossary. Avoid a new file when no recurring ambiguity exists, and keep transient conversation detail out of long-lived records.

The responsible owner still resolves key semantics. Upstream restraint around ADRs does not waive required records or approval. Once confirmed, align affected interfaces, plans, and tests. Preserve unresolved gaps without automatically renaming the repository.

Source: adapted from pinned Matt Pocock domain-modeling using existing project records rather than fixed GLOSSARY.md or docs/adr paths.
