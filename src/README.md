# README.md
```markdown
## Language Choice & Design Decisions

We chose **Python** for its readability, dynamic typing, and ease of prototyping. The classes directly reflect our UML class diagram from Assignment 9.

### Key Design Decisions
- Used underscores for private attributes.
- Used @property decorators for encapsulation.
- Used inheritance for `Analyst` and `Admin`.
- Composition is shown in `MitigationPlan` (has Tasks) and `RiskReport` (has entries).